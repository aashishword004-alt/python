'''Example 1:
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s


Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged'''

#Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
word1 = 'abc'
word2 = 'pqr'
def marge(word,word2):
    new_str = "".join(a + b for a,b in zip(word1,word2))
    return new_str

print(marge(word1,word2))