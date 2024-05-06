def build(nums):
    ans=[]
    for i in range(len(nums)):
        ans.append(0)

    for i in range(len(nums)):
        ans[i]=nums[nums[i]]

    return ans

nums=list(map(int,input().split()))
print(build(nums))