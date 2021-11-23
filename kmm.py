a = int(input(' addad aval '))
b = int(input('addad dovom '))
c = max(a, b)
d = min(a,b)
for i in range(1, (c * d)):
    if ((c * i) % d == 0):
        answer = (c * i)
        break        
print(answer)