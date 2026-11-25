'''a="hello"
print(a[3:1-1:-1])
print(a[-2:-5:-1])
print(a[::-1])






a='good morning' 
print(a[1:])
print(a[1:5+1:2])
print(a[5::3])
print(a[-7:-1+1:3])
print(a[-7::3])
print(len(a))'''

'''a=input("enter:")
print(type(a))'''

'''a=int(input("enter:"))
if a%2==0:
    print("even")
else:
    print("odd")'''

'''l=eval(input("enter:"))
if len==5:
    print("yes")
else:
    print("no")'''

'''print(chr(65))
print(chr(97))
print(ord('A'))
print(ord('a')-32)
print(ord('A')+32)


ch=input("enter:")
if "A"<=ch<="Z":
    print("upper")
elif "a"<=ch<='z':
    print("lower")
else:
    print("not a alpha")

un=input("enter:")
if un=='janet':
    print("valid user")
    pw=input("enter:")
if pw=='1234':
    print("success")
else:
    print("fail")

i=1
while i<=2:
    print(i)

for i in range(1,50):
    if i%2==0:
        print(i)
    else:
        continue

n=int(input("enter num:"))
rev=0
while n>0:
    ld=n%10
    n=n//10
    rev=rev*10+ld
    print(rev)

l=[10,20,30]
for i in l:
    print(i)
n="janet"
for i in n:
    print(i)

s=input("enter:")
rev=''
for i in s:
    if"A"<=i<="Z":
        out+=chr(ord(i)+32)
    if"a"<=i<="z":
        out+=chr(ord(i)+32)
else:
    out+=1
print(out)

s=input("enter:")
rev=''
for i in s:
    rev=i+rev
print(rev)

for i in range(1,6):
    for j in range(1,5):
        print('*',end=' ')
    print()

for i in range(1,6):
    for j in range (1,6):
        if i==j:
            print('1',end=' ')
        else:
            print('@',end=' ')
        print()'''

'''a="Happy Birthday"
print(a[0:-7:-1])'''

'''def convert(s,out):
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    return out
print(convert(input('enter a string:'),''))'''

'''def convert(s,out):
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)+32)
        else:
            out+=i
    return out
print(convert(input('enter a string:'),''))'''

'''def convert():
    s=input("enter:")
    out=''
    for i in s:
        if 'a'<=i<='z':
           out+=chr(ord(i)-32)
        else:
            out+=i 
    return out
print(convert())'''

'''def student(name,usn):
    name=name
    usn=usn
print()'''

'''class college:
    name="gopalan"
    loc="hoodi"
s1=college()
print(s1.name,s1.loc)
college.loc="whitefield"
print(college.loc)
print(s1.loc)
print("changing the location")
s1.loc="london"
print(s1.loc)
s1.loc="hoodi"
print(s1.loc)
print(college.loc)'''

'''class college:
    name="gopalan"
    loc="hoodi"
    s1=college()
    s1.name='janet'
    s1.phno=1234567890
    s2=college()
    s2.name='judo'
    s2.phno=7795335259
    s1.loc="londo"
    print("aftre changing")
    print(s1.loc)'''

'''class college:
    def __init__(self,name,phno,usn):
            self.name=name
            self.phno=phno
            self.usn=usn
s1=college("janet",1976,18)
s2=college("jan",7625,16)
print(s1.name)
print(s2.phno)
s1.display()
s2.display()'''

'''def disaplay (self):
    print(self.name,self.phno,self.usn)
s1=college("janet",1976,18)
s2=college("jan",7625,16)
s1.display()
s2.display()'''

class college:
    name="gopalan"
    loc="hoodi"
    def __init__(self,name,phno,usn):
            self.name=name
            self.phno=phno
            self.usn=usn
s1=college("janet",1976,18)
s2=college("jan",7625,16)
s1.display()
   