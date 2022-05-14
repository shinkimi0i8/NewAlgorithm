def solution(phone_book):
    answer = True
    nums = {}
    for i in range(len(phone_book)):
        if phone_book[i] not in nums:
            nums[phone_book[i]] = 1
        else:
            nums[phone_book[i]] += 1
    print(nums)

    
    return answer

print(solution(["123", "456", "789"]))