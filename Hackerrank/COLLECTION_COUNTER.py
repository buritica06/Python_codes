'''
https://www.hackerrank.com/challenges/collections-counter/problem
'''

import re
from collections import Counter

if __name__ == '__main__':
    shoes_qty, shop_slist, usrs_qty = (input(), Counter(list(map(int, input().split()))), input())
    earned = 0
    if re.match(r'^[1-9][0-9]{0,3}', shoes_qty) and re.match(r'^[1-9][0-9]{0,2}|^1000', usrs_qty):
        for usr in range(0, int(usrs_qty)):
            usr_size, usr_price = map(int, input().split())
            if shop_slist[usr_size] > 0: 
                earned += usr_price
                shop_slist[usr_size] -=1
            
    print(earned)


student = int(input()) 
i = 0 
dic = {} 
while student > i: 
    name = input().split() 
    name1 = name[0] 
    marks1 = float(name[1]) 
    marks2 = float(name[2]) 
    marks3 = float(name[3]) 
    percent = format(((marks1 + marks2 + marks3) / 3),'.2f') 
    dic[name1] = percent 
    i += 1 
    query = input() 
    print(dic[query])