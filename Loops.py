if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i**2)
        
        
#instantiating a variable i in a of 0 and n then printing the square of i

#you could use a much shorter way like this
[print(i**2) for i in range(n)]
