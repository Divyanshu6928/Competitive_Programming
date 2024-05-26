nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
k=int(input())
c=0
for i in range(len(nums1)):
    for j in range(len(nums2)):
        if(nums1[i]%(nums2[j]*k)==0):
            c+=1
print(c) 