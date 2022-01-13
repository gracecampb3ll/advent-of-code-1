f = open('./day1.txt', 'r')

nums = []
for line in f.readlines():
    nums.append(int(line))


print(sum(x < y for x, y in zip(nums, nums[1:])))