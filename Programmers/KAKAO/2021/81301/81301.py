def solution(s):
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in range(len(nums)):
        if nums[i] in s:
            print(nums[i])
            s = s.replace(nums[i], str(i))

    print(s)
    answer = 0
    return int(s)

print(solution("one4seveneight"))