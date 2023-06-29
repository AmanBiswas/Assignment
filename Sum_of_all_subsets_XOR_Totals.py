def subsetXORSum(nums):
    xor_total = 0
    bitwise_or = 0

    for num in nums:
        bitwise_or |= num

    n = len(nums)
    xor_total = bitwise_or * pow(2, n - 1)

    return xor_total

nums = [5,1,6]
print(subsetXORSum(nums))
nums = [1,3]
print(subsetXORSum(nums))
