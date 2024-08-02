# Reverse a tuple using slicing technique

def reverseTuple(tuples):
    result = tuples[::-1]
    return result
     
#Input
inputTuple = (1,2,3,4,5,6,7,8,9)

#Function call and store result
result = reverseTuple(inputTuple)

#Print results
print("Original Input: ",inputTuple)
print("Reversed Tuple Output: ",result)
