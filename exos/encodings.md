---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.1
kernelspec:
  display_name: jupytext-dev
  language: python
  name: jupytext-dev
---

# ASCII

```{code-cell} ipython3
text1 = "abcd\nefgh\n"
```

<https://www.man7.org/linux/man-pages/man7/ascii.7.html>

```{code-cell} ipython3
for c in text1:
    print(f"{c} -> {ord(c)}")
```

## write into a text file

```{code-cell} ipython3
from pathlib import Path
```

```{code-cell} ipython3
with Path('encodings1-utf8').open('w') as f:
    f.write(text1)
```

inspect that file with a hex editor - e.g. you can use vs-code and install the **HEX Editor** extension

you will see that with ASCII-only characters your file has exactly one byte ber character

+++

# non-ASCII & UTF-8

```{code-cell} ipython3
text2 = "abçd\néfgh\n"
```

## inspection

```{code-cell} ipython3
for c in text2:
    print(f"{c} -> {ord(c)}")
```

we have 2 characters whose encoding is > 127

```{code-cell} ipython3
hex(231), hex(233)
```

```{code-cell} ipython3
bin(231), bin(233)
```

note that `chr()` and `ord()` are the inverse of one another

```{code-cell} ipython3
chr(231), ord('ç')
```

## write into a text file

```{code-cell} ipython3
with Path('encodings2-utf8').open('w') as f:
    f.write(text2)
```

## read back

```{code-cell} ipython3
with Path('encodings2-utf8').open('rb') as f:
    raw = f.read()
```

**NOTE** we read bytes here, and we have more than the initial text had characters

```{code-cell} ipython3
len(raw), len(text2)
```

it makes sense, since the 2 characters will need 2 bytes each to be encoded

+++

## visual check

+++

remember the logic of the UTF-8 encoding

+++

![](../media/unicode-decode-example.png)

+++

let's check that

```{code-cell} ipython3
ccedilla = raw[2:4]
eaccent = raw[6:8]
```

```{code-cell} ipython3
for b in ccedilla:
    print(f"byte {b} {hex(b)} {bin(b)}")
```

```{code-cell} ipython3
for b in eaccent:
    print(f"byte {b} {hex(b)} {bin(b)}")
```

sounds good

+++

## decode manually ?

```{code-cell} ipython3
# we want 5 bits from the first byte and 6 from the second byte
on2bytes_0_len = 5
on2bytes_1_len = 6
# and that's what should occur in the remaining (left-hand-side) bits
on2bytes_0_pad = 0b110
on2bytes_1_pad = 0b10
```

```{code-cell} ipython3
def mask_from_len(length):
    """
    for e.g. len == 5, we compute a mask that has
    3 bits set and 5 bits unset (because 3+5=8)
    """
    return 2**8 - 2**length
```

```{code-cell} ipython3
# e.g. for byte0
# the result allows to separate 
# the (3-bits) padding from 
# the (5-bits) payload
bin(mask_from_len(5))
```

```{code-cell} ipython3
# with that we can manually decode 2-bytes UTF-8 !

on2bytes_0_mask = mask_from_len(on2bytes_0_len)
on2bytes_1_mask = mask_from_len(on2bytes_1_len)

def decode(on2bytes):
    b0, b1 = on2bytes
    # check masks
    # e.g. check that the 3 high bits in 0xc9 are indeed 0b110
    assert (b0 & on2bytes_0_mask) >> on2bytes_0_len == on2bytes_0_pad
    # same on byte 1
    assert (b1 & on2bytes_1_mask) >> on2bytes_1_len == on2bytes_1_pad
    # extract meaningful bits
    # for that we just need to invert the mask
    bits0 = b0 & ~ (on2bytes_0_mask)
    bits1 = b1 & ~ (on2bytes_1_mask)
    # asemble bits into codepoint
    # b0 has the high bits so it needs to be shifted
    # by the number of meaningful bits in byte1
    codepoint = bits1 | bits0 << on2bytes_1_len
    return chr(codepoint)
```

```{code-cell} ipython3
# and indeed 
decode(eaccent), decode(ccedilla)
```

## exercise

+++

use this table to write a complete UTF-8 decoder 

![](../slides/media/unicode-utf8-areas.png)

+++

# UTF-32

+++

## write with UTF-32

```{code-cell} ipython3
with Path("encodings2-utf32").open('w', encoding='utf-32') as f:
    f.write(text2)
```

## size and BOM

```{code-cell} ipython3
with Path("encodings2-utf32") as p:
    print(f"file has {p.stat().st_size} bytes")
```

```{code-cell} ipython3
len(text2)
```

44 is because 

* 4 * 10 chars = 40 bytes
* *plus* 4 bytes for the BOM located in the first 4 bytes

```{code-cell} ipython3
with Path("encodings2-utf32").open('rb') as f:
    raw = f.read()
```

```{code-cell} ipython3
raw[:4]
```

which indeed matches the UTF-32 little-endian (LE) BOM as shown on <https://en.wikipedia.org/wiki/Byte_order_mark>

+++

## decoding is way easier

+++

with that in mind it is easier to

* compute the location of a given character from its rank in the string
* and to decode the raw binary stream

+++

for example: decode the `ç` in our initial string

```{code-cell} ipython3
text2[2]
```

so this means it gets encoded in the file on 4 bytes starting at offset 
4 + 4 * 2

```{code-cell} ipython3
offset = 4 + 4*2

b4 = raw[offset:offset+4]
```

because it is little endian - see <https://en.wikipedia.org/wiki/Endianness> - it means we have to mirror the data bytes to get the actual value

```{code-cell} ipython3
int.from_bytes(b4, 'little')
```

```{code-cell} ipython3
chr(231)
```
