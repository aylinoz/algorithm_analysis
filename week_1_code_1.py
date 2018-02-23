import time
def fibo_rec(n):
    if(n<2):
        return n
    else:
        return fibo_rec(n-1)+fibo_rec(n-2)
fibo_rec(0),fibo_rec(1),fibo_rec(2),fibo_rec(3)fibo_rec(4),fibo_rec(5)
n=40
time_1=int (round(time.time()))
fibo_rec(n)
time_2=int (round(time.time()))
print(n, "icin gecen sure:", time_2-time_1, "saniye")
for n in range(45):
    time_1=int (round(time.time()))
    fibo_rec(n)
    time_2=int (round(time.time()))
    print(n, "icin gecen sure:", time_2-time_1, "saniye")
