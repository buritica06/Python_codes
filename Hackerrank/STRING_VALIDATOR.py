'''
https://www.hackerrank.com/challenges/string-validators/problem?h_r=next-challenge&h_v=zen
'''

if __name__ == '__main__':
    s = input()
    func = [".isalnum()",".isalpha()",".isdigit()",".islower()",".isupper()"]
for i in func:
  eval("print (any(char" + i + " for char in s))")

