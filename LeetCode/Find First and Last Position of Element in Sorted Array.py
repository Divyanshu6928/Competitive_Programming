class Solution:
    def searchRange(self, nums, target: int):
        n=len(nums)
        lo,hi=0,n-1
        p=[-1,-1]
        while(lo<=hi):
            mid=(lo+hi)//2
            if(nums[mid]==target):
                if(mid>0 and nums[mid-1]==target):
                    hi=mid-1
                else:
                    p[0]=mid
                    break
            elif(nums[mid]>target):
                hi=mid-1
            else:
                lo=mid+1
        
        lo,hi=0,n-1
        while(lo<=hi):
            mid=(lo+hi)//2
            if(nums[mid]==target):
                if(mid<n-1 and nums[mid+1]==target):
                    lo=mid+1
                else:
                    p[1]=mid
                    break
            elif(nums[mid]>target):
                hi=mid-1
            else:
                lo=mid+1

        return p