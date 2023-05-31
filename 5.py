#program to sort even no.'s
#l=[10,11,13,14,9,8]
#l1=[x for x in l if x%2==0]
#print("output using list comprehension:",l1)

#program to fetch all sting values in a list
#l=[10,'a',20,True,30,'b',40]
#l1=[x for x in l if isinstance(x,str)]
#print(l1)


#program to find divisibles by 5
#l=[12,15,27,20,5]
#l=[x for x in l if x%5==0]
#print(l)

#program  to count all int values in a list
#l=[10,'a',True,30,'b',40]
#l1=sum([x for x in l if isinstance(x,int)])
#print(l1)

#program to count total no.of characters in a string including spaces
s="python programming"
l=sum(1 for str in s)
print(l)


# program to count total no.of words in given string?
#s="python is good language for beginners"
#l=len([x for x in s.split()])
#print(l)

#program tofetch all vowels from the string?
#s='python is good language for beginners'
#l=[x for x in s if x in 'a,e,i,o,u']
#print(l)

#program to count no.of vowels in str?
#s='python is good language for beginners'
#l=len([x for x in s if x in "a,e,i,o,u"])
#print(l)

#program to count total no.of charectors in given strng (include space)?
#s='python is a simple language'
#l=len([x for x in s ])
#print(l)

#write a program to fetch all no.of consonants in the str?
#s='python language'
#l=len([x for x in s if x not in'a,e,i,o,u'])
#print(l)

#program to fetch all words which starts with vowel from given str?
#s='python is a simple and easy language'
#i=0
#l=[word for word in s.split() if word[i] in ('a,e,i,o,u')]
#print(l)

# program to fetch all words which endswith consonent in the given str?
#s='python is simple and easy language'
#l=[word for word in s.split() if word[len(word)-1] not in 'a,e,i,o,u']
#print(l)

# program to fetch all words which 'a' two or more then two times
#s='python is simple and easy language'
#l=[x for x in s.split() if x.count('a')>1]
#print(l)

#program to count number of charector  of each word in the str?
#s='python is simple and easy language'
#l=[len(word) for word in s.split()]
#print(l)

#program to fetch the first  and last charector for each word in str?
#s='python is simple and easy language'
#l=[x[0]  for x in s.split()]
#l1= [x[len(x)-1] for x in s.split()]
#l=l+l1
#print(l)

#program to fetch all words each contains 'a' charector in the str?
#s='python is simple and easy language'
#l=[word for word in s.split() if 'a' in word]
#print(l)  

#program to fetch all words does not contain 'e' charector in str?
#s=input("enter the string:")
#l=[x for x in s.split() if 'e' not in x]
#print(l)

#a program to fetch all words which contain only 4 or lessthen 4 charectors?
#s=input("enter the string:")
#l=[word for word in s.split() if len(word)<=4]
#print(l)

#program to fetch all words which contain odd number of charectors in str?
#s=input("enter the input:")
#l=[x for x in s.split() if len(x)%2==1]
#print(l)

#program to fetch all words which starts and ends with vowel in str?
#s="hari is hard working"
#l=[word for word in s.split() if word[0] in 'a,e,i,o,u' and word[-1] in 'a,e,i,o,u']
#print(l)

#program to fetch all palendram words from  lst?
#names=['madam','python','dad','language','eye','malayalam']
#l=[x for x in names if x[:]==x[::-1]]
#print(l)

#program to fetch all  non-palendram words from  lst?
#names=['madam','python','dad','language','eye','malayalam']
#l=[x for x in names if x[:]!=x[::-1]]
#print(l)

# program to fetch all  palendram words which starts with 'm' charector?
#names=['madam','python','dad','language','eye','malayalam']
#l=[x for x in names if 'm' in x[0]]
#print(l)

#program to fetch all  palendram words which more then 3 charectors?
#names=['madam','python','dad','language','eye','malayalam']
#l=[x for x in names if len(x)>3]
#print(l)

# program to fetch longest  palendram word
#names=['madam','python','dad','language','eye','malayalam','narayaayaran']
#l=max([x for x in names if x[:]==x[::-1]])
#print(l)











         
        

    
        
        