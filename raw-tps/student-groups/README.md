- [synopsys](#synopsys)
  - [read a file](#read-a-file)
  - [indexing](#indexing)
  - [dataframe](#dataframe)
  - [groups](#groups)
  - [regexps](#regexps)

# synopsys

## read a file

works on: `list` `file` `tuple`

* the input file contains lines like
  ```
  first_name last_name email phone
  ```
* fields are separated by any number (but at least one) of spaces/tabs
* write a function `parse(filename)` for parsing this format
* expected output a list of 4-tuples

## indexing

works on hash-based types, comprehensions

* we need a fast way to
  * check whether an email is in the file
  * quickly retrieve the details that go with a given email
* what is the right data structure to implement that ?
* write a function
  ```python
  index(list_of_tuples)
  ```
  that builds and returns that data structure
* write a function
  ```python
  def initial(list_of_tuples):
  ```
  that indexes the data on the
  initial of the first name (what changes do we need to do on the resulting data
  structure ?)
## dataframe

we want to build a pandas dataframe to hold all the data

see [the documentation of
`pd.DataFrame()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)

observe that there are multiple interfaces to build a dataframe; we will xxx

## groups

works on sets

* the file now contains optional fields
  ```
  first_name last_name email phone [group1 .. groupn]
  ```
* we want to tweak `parse` and write
  ```python
  def group_parse(filename):
  ```
  so it now returns a 2-tuple with
  * the list of tuples as before
  * a dictionary of sets; the keys here will be the group names, and the
    corresponding value is a set of tuples corresponding to the students in that group


## regexps

* we now want to check the format for the input file:
  * first_name and last_name may contain letters and `-` and `_`
  * email may contain letters, numbers, dots, and must contain exactly one `@`
  * phone numbers may contain 10 digits, or `+33` followed by 9 digits
