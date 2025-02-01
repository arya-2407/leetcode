'''
Objective:
Given a list of key-value pairs, sort the list by key using Insertion Sort. 
Return a list of lists showing the state of the array after each insertion. 
If two key-value pairs have the same key, maintain their relative order in the sorted list.
'''

'''
Input:
pairs = [(5, "apple"), (2, "banana"), (9, "cherry")]

Output:
[[(5, "apple"), (2, "banana"), (9, "cherry")], 
 [(2, "banana"), (5, "apple"), (9, "cherry")], 
 [(2, "banana"), (5, "apple"), (9, "cherry")]]
 '''

 # Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        for i in range(len(pairs)):
            j = i - 1
            while (j>=0 and pairs[j+1].key < pairs[j].key):
                temp = pairs[j+1]
                pairs[j+1] = pairs[j]
                pairs[j] = temp
                j-=1
            res.append(pairs[:])  #clones current state of list
        return res

