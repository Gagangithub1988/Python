def list_4(nums):
    count=0
    for num in nums:
        if num == 4:
            count+=1
    return count
print(list_4([1,2,3,4,5,6,4,4,4,5]))
