class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        from math import gcd

        n = len(nums)
        arr = [0] * n

        curr = 0

        for i in range(n):
            curr = max(curr, nums[i])
            arr[i] = gcd(nums[i], curr)

        arr.sort()

        ans = 0
        l, r = 0, n - 1

        while l < r:
            ans += gcd(arr[l], arr[r])
            l += 1
            r -= 1

        return ans
