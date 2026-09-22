# Problem statement

You are given an array of characters which represents a string s. Write a function which reverses a string.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["n","e","e","t"]

Output: ["t","e","e","n"]
Example 2:

Input: s = ["r","a","c","e","c","a","r"]

Output: ["r","a","c","e","c","a","r"]
Constraints:

1 <= s.length < 100,000

s[i] is a printable ascii character.

# Array

- create a temp list
- iterate s backwards and add characters into temp
- iterate s, replace s[i] with temp[i]

```
def reverseString(self, s: List[str]) -> None:
    reversed = []

    for i in range(len(s) - 1, -1, -1):
        reversed.append(s[i])
    
    for i in range(len(s)):
        s[i] = reversed[i]
```

TC: O(n) 

SC: O(n)

# DFS
create a DFS (l, r) that swaps characters at l and r while l < r
call dfs(0, len(s) - 1)

```
def reverseString(self, s: List[str]) -> None:
    def dfs(l, r):
        if l < r:
            s[l], s[r] = s[r], s[l]
            dfs(l + 1, r - 1)
    dfs(0, len(s) - 1)
```


TC: O(n) 

SC: O(n)

# Stack

Stack is LIFO (Last In First Out) -> put all characters of s into stack, pop each and replace current characters in s one by one

```
def reverseString(self, s: List[str]) -> None:
    stack = []

    for c in s:
        stack.append(c)
    
    for i in range(len(s)):
        s[i] = stack.pop()
```

TC: O(n) 

SC: O(n)

# Two Pointers

Use two pointers l = 0 and r = len(s) - 1, while l < r we swap characters at those pointers, move them towards mid

```
def reverseString(self, s: List[str]) -> None:
    l, r = 0, len(s) - 1

    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
```

TC: O(n) 

SC: O(1)

