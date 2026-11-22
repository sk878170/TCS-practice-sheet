def binary_search(nums,x):
    i=0
    j=len(nums)-1
    while i<=j:
        mid=(i+j)//2
        if nums[mid]==x:
            return "found"
        elif x>nums[mid]:
            i=mid+1
        else:
            j=mid-1
    return "not found"

nums=list(map(int,input().split()))
target=int(input())