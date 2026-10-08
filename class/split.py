import re

text = "apple,orange;banana grape"
# Splits by a comma, a semicolon, or a whitespace character
result = re.split(r'[,;\s]', text)
# result  = text.split()
print(result)
# Output: ['apple', 'orange', 'banana', 'grape']
