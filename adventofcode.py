f = open('./day1.txt', 'r')

nums = []
for line in f.readlines():
    nums.append(int(line))


print('first answer', sum(x < y for x, y in zip(nums, nums[1:])))

print('second answer', sum(x < y for x, y in zip(nums, nums[3:])))
