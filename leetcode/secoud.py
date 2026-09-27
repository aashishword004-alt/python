'''Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s'''
a = 'ab'
b = 'pqrs'

list3 = a+b
new_list = ''.join(list3)

print(new_list)

