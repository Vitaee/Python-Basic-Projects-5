from random import random

print("Welcome to the Coin Toss App")
#madeni paranın kaç kez havaya atılacağını belirliyoruz
n=int(input("How many time ı will throw:"))
t=0
y=0

para = []
for i in range(1, n + 1):
    x=random()
    if (x < 0.5):
        t=t+1
        para.insert(i, 'Heads')
    elif (x >= 0.5):
        y=y+1
        para.insert(i, 'Tails')
print(para)
print('Heads numbers: ', t)
print('Tails numbers: ', y)

tura = round(100*t / n + 1, 2)
yazi = round(100*y / n + 1, 2)
print("%",tura)
print("%",yazi)
