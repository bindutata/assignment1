#(1)Calculate the sum of all numbers from 1 to a given number.
'''n=int(input("enter the n value:"))
sum=0
for x in range(1,n):
    sum=sum+x
print("the sum of n numbers is:",sum)'''

#(2)Write a program to print multiplication table of a given number.
'''n=int(input("enter the n value:"))
i=1
while i<=10:
    product=i*n
    print("{}*{}={}".format(i,n,i*n))
    i+=1'''

#(3)Display numbers from a list using loop
'''n=eval(input("enter the list members:"))
l=[]
for x in n:
    l.append(x)
for x in l:
    print("the numbers present in the list are :",x)'''

#(4)Count the total number of digits in a number.
'''n=int(input("enter the number:"))
count=0
while n>0:
    n//=10
    count=count+1
print("the number of digits in a number is :",count)'''
                  

#(5)Print list in reverse order using a loop.
'''n=eval(input("enter the members of list:"))
l=[]
for x in n:
    l.append(x)
for x in l:
    l1=l[::-1]
print("the reverse of list is :",l1)'''

#(6)Display numbers from -10 to -1 using for loop.
#n=n=int(input("enter the members of list:"))
'''i=-10
while i<=-1:
    print(i)
    i+=1'''

#(7)Use else block to display a message “Done” after successful execution of for loop.
'''n=int(input("enter n value:"))
for i in range(0,n+1):
    if i!=5:
        print("i!=5 and further execution continues")
        continue
    else:
        print("done")'''

#(8)Write a program to display all prime numbers within a range.
#(9)Display Fibonacci series up to 10 terms.
'''n=int(input("enter the n value:"))
n1=0
n2=1
print(n1,n2)
for  x in range(2,n+1):
    sum=n1+n2
    n1=n2
    n2=sum
    print(n1,n2,sum)'''

#(10)Find the factorial of a given number.
'''n=int(input("enter the number:"))
fact=1
while n>0:
        fact=fact*n
        n=n-1
print("factorial of a given number is:",fact)'''

#(11)Reverse a given integer number.
'''n=int(input("enter the number:"))
reverse=0
while n>0:
    last_digit=n%10
    reverse=(reverse*10)+last_digit
    n=n//10
print(reverse)'''
                  #or
'''n=678
reversed=str(n)[::-1]
print(reversed)'''

#(12)Use a loop to display elements from a given list present at odd index positions.
'''list=input("enter some list:")
l=[]
for x in list.split(' '):
    l.append(x)
l1=l[1::2]
print(l1)
for x in l1:
    print("the objects present at odd positions is:",x)'''

#(13)Calculate the cube of all numbers from 1 to a given number.
'''n=int(input("enter the number:"))
for i in range(1,n):
    cube=i*i*i
    print(cube,end=',')'''

#(14)Find the sum of the series upto n terms.
'''n=int(input('enter the n value:'))
sum=0
for x in range(n+1):
    sum=sum+x
print("the sum of n numbers is :",sum)'''

#(15)append new string in the middle of the string
'''str=input("enter the string :")
str1=input("enter the new string :")
new_str=''
new_str=(str.split(' ')[0:2])+str1.split()+(str.split(' ')[2:])
print("the new string is :",' '.join(new_str))'''

#(16)Arrange string characters such that lowercase letters should come first.
'''str=input("enter the string :")
str_lowercase=[]
str_uppercase=[]
for i in str:
    if i.islower():
        str_lowercase.append(i)
    else:
        str_uppercase.append(i)
new_str=str_lowercase+str_uppercase
print("the new string with lowercase letters first:",''.join(new_str))'''

#(17)Count all letters, digits, and special symbols from a given string
'''str=input("enter the string:")
count=0
count1=0
count2=0
for x in str:
    if  x.isdigit():
        count=count+1
    elif x.isalpha():
        count1=count1+1
    else:
        count2=count2+1
print("number of digits in string is:",count)
print("number of alphabets in a string is:",count1)
print("number of special symbols in a string is :",count2)'''

#(18)Find all occurrences of a substring in a given string by ignoring the case.
'''str=input("enter the string :")
count=str.count("hi")
print(count)'''

#(19)Calculate the sum and average of the digits present in a string.
'''str=input("enter the string:")
sum=0
count=0
for x in str:
    if x.isdigit():
        sum+=int(x)
        count+=1
print("sum of all digits present in string:",sum)
print("avg of all digits present in a string is:",sum/count)'''

#(20)Write a program to count occurrences of all characters within a string.
'''str=input("enter the string:")
for x in str:
    count=str.count(x)
    print("{} : {} ".format(x,count),end='')'''
                  #or
'''str=input("enter the string:")
d={x:str.count(x) for x in str}
print(d)'''
                
#(21)Reverse a given string.
'''str=input("enter the string:")
reversed=(str.split())[::-1]
print("the reversed string is :"," ".join(reversed))'''

#(22)Split a string on hyphens
'''str=input("enter the string:")
str1=str.split('-')
print(str1)'''

#(23) Remove empty strings from a list of strings.
'''str=['hi',"",'hello',"",'g']
for x in str:
    if x=="":
        str.remove("")
print(str)'''
               #or
'''print("".join(str))'''

    
#(24)Removal all characters from a string except integers.
'''str=input("enter the string:")
str1=''
str2=''
for x in str:
    if x.isalpha():
        str1=str1+x
    else:
        str2=str2+x
str=str1+str2
print(str.replace(str1,' '))'''
                #or
'''str=input("enter the string:")
str1=''
for x in str:
    if x.isdigit():
        str1=str1+x
print("new string with only integers is:",str1)'''


#(25)Reverse a list in Python
'''str=input("enter the string:")
list=str.split()
print(list[::-1])'''

#(26)Concatenate two lists index-wise.
'''l1=['hi','hello',345,7.68]
l2=['my','name','is',345]
list=[]
for i in range(len(l1)):
    list.append(str(l1[i])+str(l2[i]))
print(list)'''

#(27)Turn every item of a list into its square.
'''list=(input("enter the list:"))
list1=[]
for x in list:
    list1.append(x)
new_list=[x*x for x in range(len(list1))]
print("list with square of a numbers s:",new_list)'''

#(28)Replace list’s item with new value if found
'''l=['hi','hello',345,89.12]
l[2]='apple'
print(l)'''

#(29).Add new item to list after a specified item.
'''l=['hi','hello',345,89.12]
l.insert(2,'apple')
print(l)'''

#(30): Remove all occurrences of a specific item from a list.
'''l=[1,2,3,4,2,3,1,1,2,3,1,2,1]
l1=[]
for x in l:
    if x!=1:
        l1.append(x)
print(l1)'''










