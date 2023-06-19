# (1)
'''n=int(input("enter n value:"))
for i in range(n):
    for j in range(i+1):
        print("* ",end='')
    print()'''
                    # or

'''n=int(input("enter n value:"))
for i in range(n):
    print("* "*(i+1))'''

#(2)
'''n=int(input("enter the n value:"))
for i in range(n):
    for j in range(n-i):
        print("* ",end="")
    print()'''
                    # or

'''n=int(input("enter the n value:"))
for i in range(n):
    print("* "*(n-i))'''

#(3)
'''n=int(input("enter the n value:"))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end="")
    for k in range(0,i+1):
        print("* ",end="")
    print()'''
                     # or
                                          
'''n=int(input("enter the n value:"))
for i in range(n):
    print(" "*(n-1-i)+"*"*(i+1))'''

#(4)
'''n=int(input("enter the n value:"))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end="")
    for k in range(n-i):
        print("*",end="")
    print()''' 
                   # or
'''n=int(input("enter n value:")) 
for i in range(n):
    print(" "*i+"*"*(n-i))'''

#(5)          
'''n=int(input("enter the n value:"))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end="")
    for j in range(i+1):
        print("* ",end="")
    print()'''
                    # or
'''n=int(input("enter the n value:"))
for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1))'''
                  

#(6)
'''n=int(input("enter the n  value:"))
for i in range(n):
    for j in range(i):
        print(' ',end="")
    for j in range(n-i):
        print("* ",end="")
    print()''' 
                  # or
'''n=int(input("entr the n value:"))
for i in range(n):
    print(" "*i+"* "*(n-i))'''

#(7) 
'''n=int(input("enter the n  value:"))
for i in range(n):
    
        print("  "*(n-i-1)+'* ',end='')
        if i>=1:
          print("  "*(2*i-1)+"* ",end="")  
        print()'''

#(8)   
'''n=int(input("enter the n value:"))
for i in range(n):
    print("  "*(i)+"* ",end="")
    if i<n-1:
        print("  "*(2*n-2*i-3)+"*",end='')
    print()'''

#(9) diamond
'''n=int(input("enter the n value:"))
for i in range(n):
    for i in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()    
for i in range(n-1):  
    for j in range(i+1):
        print(" ",end="")
    for j in range(n-i-1):
        print("* ",end="")    
    print()'''          
                     # or
'''n=int(input("enter hte n value:"))
for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1))
for i in range(n-1):
    print(" "*(i+1)+"* "*(n-i-1))   
print()'''

#(10) left side of dimond
'''n=int(input("enter the n value:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):    
        print("* ",end="")
for i in range(n-1):
    for j in range(i+1):
        print(" ",end="")
    for j in range(n-i-1):    
        print("* ",end="")
        print()'''
                     # or
'''n=int(input("enter the n value:"))
for i in range(n):
    print("  "*(n-i-1)+"* "*(i+1))
for i in range(n-1):
    print("  "*(i+1)+"* "*(n-i-1))'''
                
#(11) right side of diamond
'''n=int(input("enter the n value:"))
for i in range(n):
    for j in range(i+1):
        print("* ",end='')
    print()    
for i in range(n-1):
    for j in range(n-i-1):
        print("* ",end="")
    print()'''
                    # or
'''n=int(input("enter the n value:"))
for i in range(n):
    print("* "*(i+1))
for i in range(n-1):
    print("* "*(n-i-1))'''
                    

#(12) hallow diamond
#(13)number patterns:
'''n=int(input("enter the n value :"))
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    print()
    i+=1''' 

#(14)
'''n=int(input("enter the n value :"))
i=1
while i<=n:
    j=1
    while j<=n:
        print(j,end=" ")
        j=j+1
    print() 
    i+=1'''   

#(15)
'''n=int(input("enter the n value :"))
i=1
while i<=n:
    j=1
    while j<=i:
        print(i,end=" ")
        j+=1
    print()
    i=i+1'''

#(16)
'''n=int(input("enter the n value :"))
i=1
while i<=n:
    j=1
    while j<=i:
        print(i-j+1,end=" ")
        j=j+1
    print()
    i+=1'''

#(17)
'''n=int(input("enter the n value:"))
i=1
while i<=n:
    j=1
    while j<=i:
        print(i,end=" ")
        j=j+1
    print()
    i+=1'''

#(18)
'''n=int(input("enter the n value:"))
for i in range(n):
    print(" "*(n-i-1)+(str(i+1)+" ")*(i+1))'''

#(19)
'''n=int(input("enter n value: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=' ')   
    for j in range(i+1):
        print(j+1,end=" ")
    print()''' 

#(20)                
'''n=int(input("enter the n value:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(n-i,end=" ")
    print()'''

#(21)
'''n=int(input("enter the n value:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1,0,-1):
        print(n-j+1,end=" ")
    print()'''

#(22)   
'''n=int(input("enter n value:"))
a=1
for i in range(n):
    for j in range(i+1):
        print(a,end=" ")
        a=a+1
    print()'''

#(23)
'''n=int(input("enter n value:"))
a=15
for i in range(n):
    for j  in range(i+1):
        print(a,end=" ")
        a-=1
    print()'''

#(24)
'''n=int(input("enter n value:"))
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(2*(n-i-1)+1):
        print(j+1,end=" ")
    print()'''

#(25)
n=int(input("enter n value:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        print(j+1,end=" ")
    print()


    

