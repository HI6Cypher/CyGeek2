import string

def cyc_ceasar(k, text) -> tuple :
    list_one = string.printable
    list_two = list()
    for i in list(text) :
        hop = list_one.index(i) + k
        if hop >= len(list_one) :
            hop -= len(list_one)
        list_two.append(list_one[hop])
    return (list_two, "".join(list_two), len(list_two))