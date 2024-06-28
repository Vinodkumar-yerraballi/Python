'''
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Function Description

Complete the split_and_join function in the editor below.

split_and_join has the following parameters:

string line: a string of space-separated words
Returns

string: the resulting string
Input Format
The one line contains a string consisting of space separated words.

Sample Input 
this is a string   

Sample Output

this-is-a-string
'''

def split_and_join(line):
    a=line.split(" ")
    return "-".join(a)

print(split_and_join('this is a string'))