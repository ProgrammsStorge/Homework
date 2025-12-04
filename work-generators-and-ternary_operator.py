n=int(input())
a1=["четное" if i%2==0 else "нечетные"for i in [j for j in range(0,n)]]
print(a1)

a2=[i if i>=10 else 0 for i in [j for j in range(0,n)]]
print(a2)

a3=[(lambda x:f"{'Fizz' if x%3==0 else ''}{'Buzz' if x%5==0 else ''}" if x%3==0 or x%5==0 else x)(i) for i in [j for j in range(0,n)]]
print(a3)

a4={i:"odd" if i%2==0 else "even"for i in [j for j in range(0,n)]}
print(a4)

a5=[len(i) if len(i)<=5 else 5 for i in ["car","cat","banana","BIGGEST IPHONE EVER!!!"]]
print(a5)

a6=[i if i>0 else 0 for i in [-1,5,9,99,-152]]
print(a6)

a7=[i**2 if i%2==0 else i**3 for i in [1,2,3,5,4,9,5,4,99]]
print(a7)

a8=["High" if i>50 else "Medium" if i>=20 else "Low" for i in [50,20,20,5,25,30,5,40,99]]
print(a8)
