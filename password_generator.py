import random


lower="abcdetghijkemnopqrstuvwxyz"
upper ="ABCDEFGHITKIMNOPeRSTUVWXYZ"
numbers="0123456789"
symbols="[]{()*;}/,_-"

lowers=[]
uppers=[]
number=[]
symbol=[]

for i in lower:
    lowers.append(i)
print(lowers)

for i in uppers:
    uppers.append(i)
print(uppers)

for i in numbers:
    number.append(i)
print(number)

for i in symbols:
    symbol.append(i)
print(symbol)


all= lowers + uppers+ number + symbol
length=16
password="".join(random.sample(all,length))
print(password)