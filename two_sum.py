# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

nums=[int(x) for x in input().split()]
target=int(input())
def two_sum(nums,target):
    hashmap={}
    compliment=target-nums[i]
    for i in range(1,len(nums),1):
        if compliment in hashmap:
            return [i,hashmap[compliment]]
        else:
            hashmap[nums[i]]=i