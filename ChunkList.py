InputList = [1,2,3,4,5,6,7]
chunk = 3

def ChunkList(InputList, chunk):
    result, tmp = [], []
    for value in InputList:
        if len(tmp) == chunk:
            result.append(tmp)
            tmp = []
        tmp.append(value)

    if tmp:  # add last bucket
        result.append(tmp)
    return result


print(ChunkList(InputList, chunk))

"""
Output:
[[1, 2, 3], [4, 5, 6], [7]]
"""