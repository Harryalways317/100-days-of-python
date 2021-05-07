alex_s = int(input())
bob_s = int(input())
A = [int(input()) for i in range(alex_s) ]
B = [int(input()) for i in range(bob_s) ]
k = []
l = []
for i in A:
    for j in B:
        k.append(i^j)
for i,j in zip(A,k):
    l.append(j | i)
print(min(l))