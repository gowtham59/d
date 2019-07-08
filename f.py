N1=int(input())
lis2=list(map(int,input().split()))
s3=lis2[1:N:2]
s4=lis2[0:N:2]
if(sum(s3)>=sum(s4)):
    print(sum(s3))
else:
    print(sum(s4))
