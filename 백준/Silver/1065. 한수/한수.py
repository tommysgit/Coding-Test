N = int(input())
ans = 0
for num in range(1, N+1):
    if num < 100:
        ans += 1
        continue
    nums = list(map(int, str(num)))
    diff = nums[1] - nums[0]
    is_hansu = 1
    for i in range(1, len(nums)):
        prev_num = nums[i-1]
        cur_num = nums[i]
        cur_diff = cur_num - prev_num
        if cur_diff != diff:
            is_hansu = 0
            break
    if is_hansu == 1:
        ans += 1
print(ans)