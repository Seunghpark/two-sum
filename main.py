from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    map = {}
    for i, num in enumerate(nums):
        diff =target- num
        if diff in map:
            return [map[diff], i]
        num_map[num] = i
