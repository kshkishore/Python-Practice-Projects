import re

print('Enter your Input: ')
test_string = input()

print ("The original string is : " + test_string)

res = len(re.findall(r'\w+', test_string))

print ("The number of words in string are : " + str(res))