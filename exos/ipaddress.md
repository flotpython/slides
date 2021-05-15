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

# analyse adresse IP

+++

## le problème

+++

Une adresse IP v4 se présente sous la forme d'une chaine contenant 4 octets (de 0 a 255 donc) en décimal séparés par des `.`

```{code-cell} ipython3
# exemples

ip1 = "192.168.0.9"
```

On vous demande d'écrire une fonction qui transforme ceci en un entier sur 32 bits; par exemple pour `ip1` on doit obtenir ceci

```{code-cell} ipython3
hex(192), hex(168), hex(0), hex(9)
```

```{code-cell} ipython3
0xc0a80009
```

```{code-cell} ipython3
# exemple 2

ip2 = "138.96.19.1"

hex(138), hex(96), hex(19), hex(1)
```

```{code-cell} ipython3
0x8a601301
```

## solution 1

+++

un peu poussif, mais qui fonctionne

```{code-cell} ipython3
def ipv4_to_int32_v1(ip):
    result = 0
    # the first byte needs to be shifted by 2**24
    # the second one will be shifted by only 2**16, ...
    rank = 24
    for x in ip.split('.'):
        result += int(x) * 2**rank
        rank -= 8
    return result
```

```{code-cell} ipython3
ipv4_to_int32_v1(ip1)
```

```{code-cell} ipython3
ipv4_to_int32_v1(ip2)
```

## solution 2

```{code-cell} ipython3
def ipv4_to_int32_v2(ip):
    bytes4 = [int(x) for x in ip.split('.')]
    shifted = [b<<(8*i) for (i, b) in enumerate(bytes4[::-1])]
    return sum(shifted)
```

```{code-cell} ipython3
ipv4_to_int32_v2(ip1)
```

```{code-cell} ipython3
ipv4_to_int32_v2(ip2)
```
