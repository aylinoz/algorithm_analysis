def fibo_loop_1(a,b,n):
    if(n>0):
        print (a,b,n)
        n=n-1
        t=a
        a=b
        b=t+b
        fibo_loop_1(b,a+b,n)
    else:
        return a

s=fibo_loop_1(0,1,10)
print(s)

import time
def fibo_loop(n):
    if (n<2):
        return n
    else:
        a=0
        b=1
        while(n>1):
            c=a+b
            a=b
            b=c
            n=n-1
    return c

def fibo_rec(n):
    if (n<2):
        return n
    else:
        return fibo_rec(n-1)+fibo_rec(n-2)

for n in range(40):
    time_1=int (round(time.time()))
    fibo_rec(n)
    time_2=int (round(time.time()))
    print("recursive np olan: ",n," icin gecen sure: ", time_2-time_1, "saniye")
    time_1=int (round(time.time()))
    fibo_loop(n)
    time_2=int (round(time.time()))
    print(" -------------------------- ")
    print("loop p(lineer) olan: ",n," icin gecen sure: ", time_2-time_1, "saniye")
