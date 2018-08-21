#Question 1
yr=int(input("Enter a year to check if its leap year:"))
if(yr%4==0):
    if(yr%100==0):
        if(yr%400==0):
            print("Leap Year")
        else:
            print("not a Leap Year")
    else:
        print("Leap Year")
else:
    print("not a Leap Year")


#Question 2
a=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
if(a==b):
    print("It is a square")
else:
    print("It is a rectangle")



#Question 3
x=int(input("Enter age of person 1:"))
y=int(input("Enter age of person 2:"))
z=int(input("Enter age of person 3:"))
if(x>=y and x>=z):
    print("Person 1 is the oldest")
elif(y>=x and y>=z):
    print("Person 2 is the oldest")
else:
    print("Person 3 is the oldest")

if(x<=y and x<=z):
    print("Person 1 is the youngest")
elif(y<=x and y<=z):
    print("Person 2 is the youngest")
else:
    print("Person 3 is the youngest")


#Question 4
Age=int(input("Enter the age:"))
Sex=input("Enter the sex:")
m=input("Enter marital status:")
if(Sex=='M'):
    print("She will only work in Urban Areas")
else:
    if(Age>=20 and Age<=40):
        print("He can work anywhere")
    elif(Age>=40 and Age<=60):
        print("He will work in urban areas only")
    else:
        print("ERROR")


#Question 5
a=int(input("Enter quantity:"))
b=100*a
if(b>1000):
    b=b-(b*0.1)
    print("Total cost for user is =",b)
else:
    print("Total cost for user is =",b)



#LOOPS

#Question 1
a=[]
for i in range(10):
    b=int(input("Enter a number:"))
    a.append(b)
print(a)

#Question 2
while True:
    print("*")

    
#Question 3
a=[]
b=[]
num=int(input("Enter number of elements:"))
for i in range(num):
    c=int(input("Enter number:"))
    a.append(c)
for y in a:
    x=y*y
    b.append(x)
print(b)

#Question 4
lst_1=[]
lst_2=[]
lst_3=[]
lst_4=[]
a=int(input("Enter number of inputs:"))
for i in range(a):
    b=input("Enter elements of list:")
    lst_1.append(b)
for i in lst_1:
    if(i.isdigit()):
        lst_2.append(i)
    elif(i.isalpha()):
        lst_3.append(i)
    else:
        lst_4.append(i)
print(lst_2)
print(lst_3)
print(lst_4)

#Question 5
p=[]
for i in range(1,101):
    if(i>1):
        flag=False
        for j in range(2,i):
            if(i%j==0):
                flag=True
        if not flag:
            p.append(i)
print(p)

#Question 6
for i in range(5):
    for j in range(i):
        print("*",end='')
    print()


#Question 7
lst=[]
n=int(input("Enter number of elements of list:"))
for i in range(n):
    a=int(input("Enter element:"))
    lst.append(a)
num=int(input("Enter the number you want to delete from list:"))
x=lst.count(num)
for i in range(x):
    y=lst.index(num)
    del(lst[y])
print(lst)







