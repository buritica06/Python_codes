#impresion de codigo lineal en terminal

if __name__ == '__main__':
    n = int(input())
      
print(*range(1, n+1), sep='')

print(*range(1, int(input())+1), sep='')