# recurSort(list) -> recursive function that sorts a list.
# Base case for your recursion; if empty or one element, return the list
# Input :[8,-1,2,4]
# Output: [-1,2,4,8]
# Challenge:

# Ngl, I copy the same code in Lab6.
# With a few mix
def recurSort(list1):
    Copy = list(list1)
    i = len(Copy)
    # base case:
    if len(list1) == 1:
        return [Copy[0]]
    while i > 0:
        # list.pop remove the element, return a whole new list.
        y = max(Copy) # or # y = min(Copy)
        Copy.remove(y)
        # Len(C) is less than previous list 1 element, making it recursive.
        return recurSort(Copy) + [y]

sample = [8,-1,2,4]
# print('Sample: ',sample )
# print('Recursive sort: ',recurSort(sample))

def quickSort(list1):
    Copy = list(list1)
    i = len(Copy)
    # base case:
    if len(list1) == 0:
        return []
    while i > 0:
        pivot = Copy[0]
        smallList = [i for i in Copy if pivot > i]
        bigList = [j for j in Copy if j>pivot]
        return quickSort(smallList) + [pivot] + quickSort(bigList)
sample = [8,-1,2,4,6,10,12,13]
print('Sample: ',sample )
print('Recursive quick sort: ',quickSort(sample))
