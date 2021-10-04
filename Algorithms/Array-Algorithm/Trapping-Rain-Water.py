#Time Complexity :O( n )
#Space Complexity : O( n )


print("Enter list of elements")
a=list(map(int,input().split()))
n=len(a)
res=0
left=[0]*len(a)
right=[0]*len(a)
left[0]=a[0]
for i in range(1,n-1):
    left[i]=max(left[i-1],a[i])
right[n-1]=a[n-1]
for i in range(n-2,-1,-1):
    right[i]=max(right[i+1],a[i])
for i in range(0,n):
    res=res+min(left[i],right[i])-a[i]
print("Rain Water Trapped is",res)
