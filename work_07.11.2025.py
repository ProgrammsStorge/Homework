# Блох Роман ИИ-71

#Задача 2

def recursion_range_a_b(a, b, i=0,rev=True):
    if i==0:i=min([a,b])
    if rev==True:
        if b<a:rev=False
    if i > max([a,b]):
        return []
    else:
        return ([i] + recursion_range_a_b(a,b, i + 1,False))[::[1,-1][int(rev)]]
print(recursion_range_a_b(int(input("A: ")),int(input("B: "))))

#Задача 1

def recursion_range_n(n,i=1):
  if n <= i:
    return []
  else:
    return [i] + recursion_range_n(n,i+1)
print(recursion_range_n(float(input())))

#Задача 3

def recursion_two(n) :
    if n == 1:
        return True
    elif n > 1 and n < 2:
        return False
    else:
        return recursion_two(n / 2)
answer=recursion_two(float(input()))
print(int(answer)*"YES" + int(not answer)*"NO")

#Задача 4

def fibbonahi_recursion(i):
    if i <= 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibbonahi_recursion(i-1) + fibbonahi_recursion(i-2)
print(fibbonahi_recursion(float(input())))

