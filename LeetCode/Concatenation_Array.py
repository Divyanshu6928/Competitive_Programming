def concatenate(nums):
    n=len(nums)
    ans=[]
    for i in range(n*2):
        ans.append(0)
    for i in range(n):
        ans[i]=nums[i]
        ans[i+len(nums)]=nums[i]

    return ans

nums=list(map(int,input().split()))
print(concatenate(nums))