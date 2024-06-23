class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        n=len(arr)
        lo=1
        hi=n-2
        while(lo<=hi):
            mid=(lo+hi)//2
            if(arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]):
                return mid
            elif(arr[mid]>arr[mid-1] and arr[mid]<arr[mid+1]):
                lo=mid+1
            else:
                hi=mid-1