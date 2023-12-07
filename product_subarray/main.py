def maxProduct(nums):
    if not nums:
        return 0
    
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product = max(nums[i], min_product * nums[i])
            min_product = min(nums[i], max_product * nums[i])
        else:
            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])

        
        
        result = max(result, max_product)
    
    return result

print(maxProduct([2,3,-2,4]))
print(maxProduct([-2,0,-1])) 