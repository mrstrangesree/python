input = input("Enter the value: ")
x= list(set(list(input)))
x.sort()

def findOccurrence(inputValue):
    output = ''
    for i in inputValue:
        output = output + 'Char: ' + i + ' Occurrence: '+ str(input.count(i)) + '\n'
    return output

#Output
print(findOccurrence(x))

"""

Sample 1:
#Input:
1111333555
aaaabbbccdd
#Output:
Char: 1 Occurrence: 4
Char: 3 Occurrence: 3
Char: 5 Occurrence: 3

Sample 2:
#Input:
aaaabbbccdd
#Output:
Char: a Occurrence: 4
Char: b Occurrence: 3
Char: c Occurrence: 2
Char: d Occurrence: 2

Sample 3:
#Input:
fff00045
#Output:
Char: 0 Occurrence: 3
Char: 4 Occurrence: 1
Char: 5 Occurrence: 1
Char: f Occurrence: 3
"""
