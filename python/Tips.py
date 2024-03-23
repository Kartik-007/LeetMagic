"Loops:"

Reverse For loop->
for i in range (5,1,-1):
  print(i)
  
Res ->
5
4
3
2



"Math:"

"Division" ->
print(5/2) -> 2.5
print(5//2) -> 2 
print(-3//2) -> -2 ("always rounds down unlike in other languages where it would be -1")
print(int(-3/2)) -> -1

"Mod" ->
print(10%3) -> 1
print(-10%3) -> -2 ("different from c-based langs")

import math
print(math.mod(-10,3)) -> -1

"Important math functions" ->
math.floor(3/2)
math.ceil(3/2)
math.sqrt(2)
math.pow(2,3)

"Max and Min nums" ->
float("inf")
float("-inf")



"Arrays:"

initialize ->
n = 5
arr = [1] * n
arr = [1,1,1,1,1]

slicing ->
arr = [1,2,3,4]
print(arr[1:3]) -> [2,3]

unpacking ->
a,b,c = [1,2,3]
a = 1, b = 2, c = 3

"looping arrays" ->
"Will print index i and the number n"
for i, n in enumerate(nums):
  print(i, n)

"looping through multiple arrays:" ->
nums1 = [1,3,5]
nums2 = [2,4,6]

for n1, n2 in zip(nums1, nums2):
  print(n1,n2)

res->
12
34
56

"sorting arrays" ->
arr.sort(), arr.sort(reverse=True)

custom sort->
arr.sort(key=lambda x:len(x)) -> "sorts by length in ascending order"



"List Comprehension:"
  
arr = [i for i in range(5)] -> [0, 1, 2, 3, 4]


       
"2d array:"

arr = [[0] * 2 for i in range(2)] -> [[0,0], [0,0]]



"Strings:"

print(ord("a")) -> 97 aka ascii value

combining strings ->
strings = ["ab", "cd", "ef"]
print("".join(strings)) -> abcdef



"Queues:"

from collections import deque
queue = deque()
queue.append(1)
queue.appendleft(2)
queue.pop()
queue.popleft()



"Hashsets:"

myset = set()
myset.add(1)
myset.add(2)
myset.remove(2)
print(1 in myset) -> True
myset = {i for i in range(5)}


"Hashmaps:"
mymap = {}
mymap = {"bob" : 10, "cat" : 2}
mymap["bob"] = 10

"comprehension" ->
mymap = {i : 2*i for i in range(3)}


"Tuples:"
"Useful as keys for hash maps"
t = (1,2,3)

