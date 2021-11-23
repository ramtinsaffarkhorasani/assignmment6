def fibo(a):
    b=[0,1]
    for i in range(a-2):
        if a==1:
            print("[0]")
            break
        elif a==2:
            print('[0,1]')
            break
        elif a==0:
            print("error")
            break
        c=b[i]+b[i+1]
        b.append(c)
    print(b)
a=int(input())
fibo(a)
