#(1)Write a Python function to find the maximum of three numbers.
'''def max(a,b,c):
    return a if a>b else b if b>c else c if a<c else a
print(max(10,20,30))
print(max(100,459,230))
print(max(200,180,60))'''

#(2)Write a Python function to sum all the numbers in a list.
'''def sum(list):
    sum=0
    for x in list:
        sum=sum+x
    print("the sum of the numbers in list is:",sum)
sum([1,2,4,0,3])
sum([7,4,9,2])'''

#(3) Write a Python function to multiply all the numbers in a list.
'''def pro(list):
    pro=1
    for x in list:
        pro*=x
    print("the product of the numbers in list:",pro)
pro([5,5,1])'''

#(4)Write a Python program to reverse a string.Sample String : "1234abcd"
#string=input("enter the string:")
'''new_string=string[::-1]
print(new_string)'''
                   #or
'''print(''.join(reversed(string)))'''
                #or
'''new_str=''
i=len(string)-1
while i>=0:
    new_str+=string[i]
    i-=1
print(new_str)'''

#(5)Write a Python function to calculate the factorial of a number. The function accepts the number as an argument.
'''def fact(n):
    if n==0:
        factorial=1
    else:
        factorial=n*fact(n-1)
    return factorial
print(fact(5))'''

#(6)Write a Python function that accepts a string and counts the number of upper and lower case letters.
'''def letters(str):
    count=0
    count1=0
    for  x in str:
        if x.isupper():
            count=count+1
        elif x.islower():
            count1=count1+1
    print("no. of uppercase leters is:",count)
    print("no. of uppercase leters is:",count1)
letters('Hai Hello Good Morning')'''

#(7)Write a Python function that takes a list and returns a new list with distinct elements from the first list.
'''def new_list(list):
    new_list=[]
    for x in list:
        if x not in new_list:
            new_list.append(x)
    print(new_list)
new_list([1,1,4,6,3,8,4])'''

#(8)Write a Python program to print the even numbers from a given list.
'''list=eval(input("enter the list:"))
even_list=[]
for x in list:
    if x%2==0:
        even_list.append(x)
print("the list of even no.s are:",even_list)'''

##(9) Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
str=input("enter the words:")   
words=str.split('-')
sorted_words=sorted(words)
print('-'.join(sorted_words))

#(10)Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30
'''def squares(list):
    print("the numbers in the list are:",list)
    print("the square of the numbers are:")
    print([x*x for x in list])
squares(list(range(1,31)))'''

#(11)Write a Python program to create any chain of function decorators.
'''def decor1(fun):
    def inner(marks):
        if marks>=90:
            print("excellent")
        else:
            fun(marks)
    return inner
def decor2(fun):
    def inner1(marks):
        if marks<=50:
            print("please improve")
        else:
            fun(marks)
    return inner1
@decor2
@decor1
def fun(marks):
    print("the marks obtained are:",marks)
#a=decor2(fun)
#a(45)
fun(45)
#fun(90)    
#fun(89)'''

#(12)Write a Python program to access a function inside a function.
'''def div(a,b):
    print(a//b)
    def inner(a,b):
        if b==0:
            print("can't be divided by zero")  
    return inner
a=div(4,2)
a(4,0)'''




