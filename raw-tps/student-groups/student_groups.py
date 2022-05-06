## read a file


def parse(filename):
    """
    parse the file and returns a list of 4-tuples
    """
    result = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            first, last, email, phone = line.strip().split()
            result.append((first, last, email, phone))
    return result


def parse_bis(filename):
    """
    almost the same
    shorter, but no control that each line has exactly 4 fields
    """
    result = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            result.append(line.strip().split())
    return result


def parse_ter(filename):
    """
    even shorter
    is that really more readable ?
    """
    with open(filename, encoding="utf-8") as f:
        return [line.strip().split() for line in f]



## indexing


# first_name, last_name, email, phone = tup
# 0           1          2      3

def index(list_of_tuples):
    """
    build a dictionary of those tuples, keyed on the email
    the tedious but safe way
    """
    result = {}
    for tup in list_of_tuples:
        first, last, email, phone = tup
        result[email] = tup
    return result


def index_bis(list_of_tuples):
    """
    a little more pythonic
    use unpacking to separate fields
    """
    result = {}
    for tup in list_of_tuples:
        # unpacking
        *_, email, _ = tup
        result[email] = tup
    return result


def index_ter(list_of_tuples):
    """
    with a comprehension
    no unpacking means we need to use
    a constant index in t[2]
    """
    return {t[2]: t for t in list_of_tuples}


def index_quater(list_of_tuples):
    """
    comprehension and unpacking
    """
    return {email: (*start, email, end)
            for *start, email, end in list_of_tuples}




# on the initial of first_name
def initial(list_of_tuples):
    """
    indexing on the first name's initial letter

    so this time the values in the output dict
    must be LISTS
    """
    result = {}
    for tup in list_of_tuples:
        first, last, email, phone = tup
        # note that it's a little dangerous to
        # override 'initial' here
        # this is NOT a recommended pratice !
        # fortunately we do not need to
        # refer to the function in the function body
        # (not a recursive function)
        initial = first[0]
        # beware that we need to check for the presence
        # of the key before we can refer to the value
        if initial not in result:
            result[initial] = []
        # now it's OK
        result[initial].append(tup)
    return result


from collections import defaultdict
def initial_bis(list_of_tuples):
    """
    thanks to defaultdict we can spare
    the existence of the key in the dict
    """
    result = defaultdict(list)
    for tup in list_of_tuples:
        # unpacking
        first, *_ = tup
        result[first[0]].append(tup)
    return result

# ... not easy to write as a comprehension as far as I can see


## dataframe

###
import pandas as pd

def dataframe(list_of_tuples):
    """
    clearly that's the way to go with this kind of data...
    """
    return pd.DataFrame(
        list_of_tuples,
        columns=['first_name', 'last_name', 'email', 'phone']
    )


## group_parse

def group_parse(filename):
    """
    returns a tuple with
    * a list of tuples, like what parse() returns
    * the groups as a dictionary
      groupname -> set of tuples
    """
    persons = []
    groups_by_name = defaultdict(set)
    with open(filename, encoding="utf-8") as feed:
        for line in feed:
            fi, la, em, ph, *groups = line.strip().split()
            person = (fi, la, ph, em)
            persons.append(person)
            for group in groups:
                groups_by_name[group].add(person)
    return persons, groups_by_name


# same using type hints to describe the types
def group_parse_bis(filename) -> tuple[
    list[tuple],
    dict[str, set[tuple]]
]:
    return group_parse(filename)


## check_values

import re

# let's consider several variants that all share the same structure

def _check_values(L, re_n, re_e, re_p):
    for first_name, last_name, email, phone in L:
        if not re_n.match(first_name):
            print(f"incorrect first_name {first_name}")
        if not re_n.match(last_name):
            print(f"incorrect last_name {last_name}")
        if not re_e.match(email):
            print(f"incorrect email {email}")
        if not re_p.match(phone):
            print(f"incorrect phone {phone}")


# first rough approx.
re_names = re.compile("^[-_a-zA-Z]+$")
re_email = re.compile("^[-a-zA-Z0-9.]+@[-a-zA-Z0-9.]+$")
# we need to escape the + because otherwise it means repetition
re_phone = re.compile("^(0|\+33)[0-9]{9}$")


def check_values(L: list) -> None:
    return _check_values(L, re_names, re_email, re_phone)


# using \w is tempting, but it will allow for _
# and we dont want that...

re_names_bis = re.compile("^[-_\w]+$")
re_email_bis = re.compile("^[-\w0-9.]+@[-\w0-9.]+$")

def check_values_bis(L: list) -> None:
    return _check_values(L, re_names_bis, re_email_bis, re_phone)


# the safe way imho
letters = "a-zàâçéèêëîïôûùüÿæœ"
re_names_ter = re.compile(f"^[-_{letters}]+$", re.IGNORECASE)
re_email_ter = re.compile(f"^[-{letters}0-9.]+@[-{letters}0-9.]+$", re.IGNORECASE)


def check_values_ter(L: list[tuple]) -> None:
    return _check_values(L, re_names_ter, re_email_ter, re_phone)
