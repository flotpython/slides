---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
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

# génération de facture

+++

## le problème

+++

on veut automatiser la rédaction de factures à partir d'une liste d'items et de prix

+++

exemple d'utilisation, imaginons qu'on a les données suivantes :

```python

company_address = """Tribeca Inc.,
Somerset House – New Wing
Lancaster Place
London WC2R 1LA
"""

thanks_message = "Thanks for shopping with us today!"

currency = '€'

shitems = [
    ("Books", 25.0, 2),
    ("Monitor", 250.0, 1),
    ("Computer", 500.0, 1),
]
```

+++

à partir de ces données on pourrait imaginer plusieurs APIs pour produire des factures comme ceci

+++

### v0 : une fonction

+++

l'API la plus simple évidemment ce serait tout simplement ceci

+++

```python
invoice = generate_invoice(
    items, company_address, thanks=thanks_message, currency='$', items)
print(invoice)
```

+++

### v1 : une classe

+++

mais on peut aussi imaginer ceci par exemple

+++

```python
generator = InvoiceGenerator(address=company_address, thanks=thanks_message)
print(generator.invoice(items))
```

+++

### exemple de résultat

+++

ce qui dans les deux cas produirait une sortie dans le genre de la suivante

+++

```
**************************************************
                  Tribeca Inc.,                   
            Somerset House – New Wing             
                 Lancaster Place                  
                 London WC2R 1LA                  
++++++++++++++++++++++++++++++++++++++++++++++++++
     Product Name     #  Item Price       
            Books     2  25.0             
          Monitor     1  250.0            
         Computer     1  500.0            
--------------------------------------------------
            Total        800.00$
++++++++++++++++++++++++++++++++++++++++++++++++++
        Thanks for shopping with us today!        
**************************************************

```

+++

## une solution v1

```{code-cell} ipython3
# let's take advantage of Python 3.9's new
# type hinting capabilities

UnitPrice = float
NumberItems = int
Item = tuple[str, UnitPrice, NumberItems]

class InvoiceGenerator:
    
    width = 50
    
    def __init__(self, address, thanks, currency='$'):
        self.address = address
        self.thanks = thanks
        self.currency = currency
        
    def invoice(self, items: list[Item]):
        """
        items is expected to be a list of tuples of the form
        (label, unit_price, number_items)
        """
        
        result = self.width * '*' + "\n"

        result += "\n".join(f"{line:^{self.width}}" 
                            for line in company_address.strip().split("\n"))
        
        result += "\n" + self.width * '+' + "\n"
        width2 = self.width // 2 - 8

        # using litterals inside another litteral 
        # thanks to the 2 kinds of quotes
        result += f"{'Product Name':>{width2}}{'#':>6}  {'Item Price':<{width2}}\n"
        
        total = 0
        for (label, unit_price, number_items) in items:
            total += unit_price * number_items
            result += f"{label:>{width2}}{number_items:>6}  {unit_price:<{width2}}\n"

        result += self.width * '-' + "\n" 
        result += f"{'Total':>{width2}}{' ':8}{total:.2f}{self.currency}\n"

        result += self.width * '+' + "\n" 
        result += f"{self.thanks:^{self.width}}\n"

        result += self.width * '*'
        return result
```

### essayons

```{code-cell} ipython3
company_address = """Tribeca Inc.,
Somerset House – New Wing
Lancaster Place
London WC2R 1LA
"""

thanks_message = "Thanks for shopping with us today!"

currency = '€'

generator = InvoiceGenerator(address=company_address, thanks=thanks_message)

items = [
    ("Books", 25.0, 2),
    ("Monitor", 250.0, 1),
    ("Computer", 500.0, 1),
]

invoice = generator.invoice(items)
```

```{code-cell} ipython3
print(invoice)
```

***
