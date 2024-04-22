def triangle(nums):
    if(nums[0]+nums[1]>nums[2] and nums[1]+nums[2]>nums[0] and nums[2]+nums[0]>nums[1]):
        if(nums[0]==nums[1]==nums[2]):
            return "equilateral"
        elif(nums[0]==nums[1] or nums[1]==nums[2] or nums[2]==nums[0]):
            return "isosceles"
        elif(nums[0]!=nums[1] and nums[1]!=nums[2] and nums[2]!=nums[0]):
            return "scalene"
    else:
        return "none"
    
nums=list(map(int,input().split()))
print(triangle(nums))
