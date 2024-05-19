# q=[[2,4],[5,6]]
# for query in q:
#     f,t=query

#     print(f,t)

nums=[1,2,3,4,5]
n = len(nums)
    
    # Step 1: Create parity array
parity = [num % 2 for num in nums]

print(parity)