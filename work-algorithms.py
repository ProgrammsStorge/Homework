import time

data=[1,51,6,8,46,4626,484,5618261231,3213,5,53,218,6,156,4,1,6,485,65,4528,6,5,4518,4,54,61,89,23,46,1,486,15,8,65,48,56,0]
def algoritm_good(data):
    n58,n29,n2=0,0,0
    for i in data:n58 += int(i%58==0);n29+=int(i%29==0 and i%58!=0);n2+=int(i%2==0 and i%58!=0)
    return (n58*(n58-1)/2)+(n58*(len(data)-n58))+(n2*n29)

def algoritm_bad(data):
    valve=0
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[j]*data[i]%58==0:valve+=1
    return valve


bad_time=time.time()
bad_result=algoritm_bad(data)
bad_time = time.time()-bad_time

good_time=time.time()
good_result=algoritm_good(data)
good_time = time.time()-good_time

step=max([bad_time,good_time])/(max([bad_time,good_time])*1000000)
for frame in range(round(max([bad_time,good_time])*1000000)+10):
    print(f"\r Плохой алгоритм: {step*frame if step*frame<bad_time else f"{bad_time}👍"}  Хороший алгоритм: {step*frame if step*frame<good_time else f"{good_time}👍"}",end="",flush=True)
    time.sleep(0.05)
print()
print(f"Результаты совпадают! Хороший дал {good_result}, а плохой тоже {bad_result}" if bad_result==good_result else f"Стоп. А как это получилось так? Это же бред. Типа хороший дал {good_result}, а плохой {bad_result}")
