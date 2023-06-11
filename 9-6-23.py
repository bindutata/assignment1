#program to store information and print the information name as input
n=int(input("enter the no.of students:"))
d={}
for x in range(n):
    name=input("enter the name of student:")
    marks=int(input('enter the marks of student:') )
    per=int(input("enter the % of the student:"))
    d[name]=marks
print("name of the student""\t","marks""\t","% of marks")
for a in d:
    print("\t {} \t\t {} \t {}".format(a,d[a],per))