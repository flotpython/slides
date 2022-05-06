## read a file


def parse(filename):
    result = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            first, last, email, phone = line.strip().split()
            result.append((first, last, email, phone))
    return result


def parse_bis(filename):
    result = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            result.append(line.strip().split())
    return result


def parse_ter(filename):
    with open(filename, encoding="utf-8") as f:
        return [line.strip().split() for line in f]



## indexing


# first_name, last_name, email, phone = tup
# 0           1          2      3

def index(list_of_tuples):
    result = {}
    for tup in list_of_tuples:
        first, last, email, phone = tup
        result[email] = tup
    return result


def index_bis(list_of_tuples):
    return {t[2]: t for t in list_of_tuples}


# on the initial of first_name
def initial(list_of_tuples):
    result = {}
    for tup in list_of_tuples:
        first, last, email, phone = tup
        # note that it's a little dangerous to
        # override 'initial' here; fortunately
        # this is not a recursive function
        initial = first[0]
        if initial not in result:
            result[initial] = []
        result[initial].append(tup)
    return result


from collections import defaultdict
def initial_bis(list_of_tuples):
    result = defaultdict(list)
    for tup in list_of_tuples:
        first, last, email, phone = tup
        result[first[0]].append(tup)
    return result

# ... not easy to write as a comprehension as far as I can see 


## dataframe

###
import pandas as pd

def dataframe(list_of_tuples):
    return pd.DataFrame(
        list_of_tuples,
        columns=['first_name', 'last_name', 'email', 'phone']
    )


###
def group_parse(filename):
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
