def bsearch(list, value):

    list_size = len(list) - 1

    idx0 = 0
    idxn = list_size

    while idx0 <= idxn:
        midval = (idx0 + idxn)

        if list[midval] == value:
            return midval
        if value > list[midval]:
            idx0 = midval + 1
        else:
            idxn = midval - 1

    if idx0 > idxn:
        return None

list = [2, 7, 19, 34, 53, 72]

print(bsearch(list,72))
print(bsearch(list,11))