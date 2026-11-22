def linear_search(nums,x):
    for i in nums:
        if i==x:
            return "found"
    return "not found"

nums=list(map(int,input().split()))
target=int(input())
print(linear_search(nums,target))

        