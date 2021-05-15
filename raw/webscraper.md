---
jupytext:
  cell_metadata_filter: all, -hidden, -heading_collapsed, -run_control, -trusted
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,
    -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
    -language_info.file_extension, -language_info.mimetype, -toc
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
---

# fetch one web page

+++

https://docs.python-requests.org/en/master/

```{code-cell} ipython3
import requests
```

```{code-cell} ipython3
req = requests.get("https://r2lab.inria.fr")
```

```{code-cell} ipython3
# OK codes are in the 200-299 range
req.status_code // 100 == 2
```

```{code-cell} ipython3
# the actual page contents ends up in 
html_text = req.text
```

```{code-cell} ipython3
len(html_text)
```

# parse HTML & get hyperlinks

+++

https://www.crummy.com/software/BeautifulSoup/bs4/doc/

```{code-cell} ipython3
!pip install bs4
```

```{code-cell} ipython3
from bs4 import BeautifulSoup
```

```{code-cell} ipython3
soup = BeautifulSoup(html_text, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
```

# build next URL

+++

the logic that allows to build the actual URL to fetch when seeing a `href` inside an HTML page is actually quite convoluted (exercise: try to hand-code it yourself)

fortunately for us, it is already the purpose of this function in the standard library

https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urljoin

```{code-cell} ipython3
from urllib.parse import urljoin
```

in a nutshell, its behaviour answers this general question:

> assuming I am visiting url X, and I see an outgoing link to URL Y, what is the absolute URL I need to fetch to follow that link ?

```{code-cell} ipython3
# a full URL ignores the current one of course

urljoin("https://r2lab.inria.fr", "https://some-place-else/entirely") 
```

```{code-cell} ipython3
# an absolute URL starts with /
# it means to restart from the hostname
urljoin("https://r2lab.inria.fr/some/path/index.html", "/an/absolute/path")
```

```{code-cell} ipython3
# a relative URL starts in the same folder as the current page

urljoin("https://r2lab.inria.fr/some/path/index.html", "a/relative/path")
```

# let's pause a minute

+++

so here's what we know how to do 

1. fetch a page from its URL
1. inspect a page's content to find liks with their relative URL
1. combine the page URL with a relative URL to build an absolute URL

what remains is thus to

1. primarily keep track of the current URL - we need it to compute the next URL's
1. keep track of pages we have already seen; that probably means to ignore/remove trailing fragment

+++

# remove trailing fragments

+++

here we talk about URL's that look like this

```{code-cell} ipython3
# one of the immediate neighbours starting from r2lab.inria.fr

url_with_fragment = urljoin("https://r2lab.inria.fr", "tools.md#main")
url_with_fragment
```

the point being that this URL points at a specific location *inside* `https://r2lab/inria.fr/tools.md`

+++

so we have 2 options here:

1. use `urlparse`
1. use regexps to cancel off the trailing `#stuff`

+++

the second option may seem a little more brittle; we need to know if it is legal to use a `#` sign elsewhere in the URL (e.g. in the username or password section); so crafting one's regexp is likely to become tedious and fragile

let us go for the first option then

```{code-cell} ipython3
from urllib.parse import urlparse
```

```{code-cell} ipython3
urlparse(url_with_fragment)
```

we will ignore the `params` and `query` parts for now (these are used to pass parameters to dynamic pages

+++

with that in mind, we can sort-of canonicalize a URL by doing

```{code-cell} ipython3
def canonical_url(url):
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
```

```{code-cell} ipython3
canonical_url(url_with_fragment)
```

# putting it together - v0

```{code-cell} ipython3
class Scraper:
    
    def __init__(self, url0):
        self.url0 = url0

    # returns a list of URLs for now
    def neighbours(self, url):
        req = requests.get(url)
        html_text = req.text
        soup = BeautifulSoup(html_text, 'html.parser')
        return [
            canonical_url(urljoin(url, link.get("href"))) for link in soup.find_all('a')
        ]        
    
    def scan(self, max_pages=100):
        """
        recursively scan pages until that many different pages have been found
        """
        to_scan = [canonical_url(self.url0)]
        scanned = set()
        
        while to_scan and len(scanned) < max_pages:
            current_page = to_scan.pop()
            scanned.add(current_page)
            for next_page in self.neighbours(current_page):
                if next_page in scanned or next_page in to_scan:
                    continue
                to_scan.append(next_page)
                print(f"{len(scanned):3d} down - {len(to_scan):3d} to go - {current_page} → {next_page}")
            print(f"--- {current_page} DONE")
            
        # print(f"------{len(to_scan)} unfinished business")
        
```

```{code-cell} ipython3
s = Scraper("https://r2lab.inria.fr")    

s.scan(3)
```

# v1: how about using generators...

+++

in your opinion

* would it make sense to inject some iterators/generators in this mix ?
* where ?
* what would be the pros and cons ?

other miscell questions

* is this anywhere close to being optimal in terms of your CPU usage ?
* completely different but, do you see an easy way to alter the scanning logic (depth-first-scan, breadth-first-scan) ?
