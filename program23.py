#Date: 28-07-18
#Author: A.Suraj Kumar
#Roll Number: 181046037
#Assignment 10
#Python Program to check whether a full pattern (not sub string) is present in the given sentence.

import re
ph = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = ph.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())






