'''Q-1 Write a Python program to input a sentence and a positive integer from the user.
 Perform the following tasks:
1.	Display all words having more consonants than vowels 
2.	Count the number of words containing at least one repeated character. 
3.	Find how many times the largest digit occurs in the given number. 
4.	Create a new number by removing all odd digits from the given number. 
Example:
Input  : 5728463
Output : 2846
for i in n:
  new = int(i)
  if new%2 == 0:
    print(new)
'''
n = input('Enter the number : ')
mx = 0
for i in n:
    count = 0
    new = int(i)
    if new > mx:
          mx = new

new = int(i)
while new > 0:
    count = 0
    digit = new % 10
    if digit == mx:
     count+=1
    new = new // 10   
 
     

print(mx)
print(count)

