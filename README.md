class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the complement and its index
        num_to_index = {}
        
        # Iterate through the list
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            # Otherwise, store the current number with its index
            num_to_index[num] = i
