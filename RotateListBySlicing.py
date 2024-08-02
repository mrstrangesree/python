#Rotate a list using Slicing technique

#define the rotate function
def listRotate(list, key):
    list = list[key:] + list[:key]
    return list

inputList = ['Apple','Bat','Cat','Dog','Elephant','Fan']
keyValue = 1

#Function call
result = listRotate(inputList,keyValue)

#print results
print('Input: ',inputList)
print('Output: ',result)