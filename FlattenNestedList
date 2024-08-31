def flatten_recursively(lst_in):
    lst_out = []
    for i in lst_in:
        if type(i) == list:
            for j in flatten_recursively(i):
                lst_out.append(j)
        else:
            lst_out.append(i)
    return lst_out

inputList = [1,[2,3, [4, 5]],[6,7, [8, 9]]]

print(flatten_recursively(inputList))
