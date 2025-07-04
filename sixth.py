def find_kth_largest(nums: list, k: int) -> int:
    x = sorted(nums, reverse=True)
    
    return x[k - 1]

nums = [3, 2, 1, 5, 6, 4,]
k = 2
print(find_kth_largest(nums, k))