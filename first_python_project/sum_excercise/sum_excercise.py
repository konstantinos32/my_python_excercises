nums =[11,7,2,15]
target=9

def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

print(two_sum(nums, target))


numbers=[3,2,4]
target=6

def new_two_sum(numbers,target):
    num_dict = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return None

print(new_two_sum(numbers, target))