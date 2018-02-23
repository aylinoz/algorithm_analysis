import time
def fibo_loop(n):
    if (n<2):
        return n
    else:
        a=0
        b=1
        c=0
        while(n>0):
            a=b
            b=c
            c=a+b
            n=n-1
    return a

def fibo_rec(n):
    if(n<2):
        return n
    else:
        return fibo_rec(n-1)+fibo_rec(n-2)

for n in range(40):
    time_1=int (round(time.time()))
    fibo_rec(n)
    time_2=int (round(time.time()))
    print ("recursive np olan", n, "icin gecen sure: ", time_2-time_1, "saniye")
    fibo_loop(n)
    time_2=int (round(time.time()))
    print ("loop p(lineer olan)", n, "icin gecen sure: ", time_2-time_1, "saniye")
