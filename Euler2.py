fib=[]
def fibo(a=0,b=1,upto=4000000):
    if a+b>=upto:
        return
    else:
        a,b=b,a+b
        fib.append(b)
        fibo(a,b)

fibo()
even=[i for i in fib if(i%2!=1)]
print sum(even)