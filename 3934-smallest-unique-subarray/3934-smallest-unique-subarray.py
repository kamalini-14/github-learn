
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        mod1 = 10**9 + 7
        mod2 = 10**9 + 9
        base1 = 31
        base2 = 37

        def check(length):
            power1 = pow(base1, length - 1, mod1)
            power2 = pow(base2, length - 1, mod2)

            h1 = 0
            h2 = 0

            for i in range(length):
                h1 = (h1 * base1 + nums[i]) % mod1
                h2 = (h2 * base2 + nums[i]) % mod2

            freq = {}
            unique = 0

            key = (h1, h2)
            freq[key] = 1
            unique += 1

            for i in range(length, n):
                h1 = ((h1 - nums[i-length] * power1) * base1 + nums[i]) % mod1
                h2 = ((h2 - nums[i-length] * power2) * base2 + nums[i]) % mod2

                key = (h1, h2)
                count = freq.get(key, 0)

                if count == 0:
                    unique += 1
                elif count == 1:
                    unique -= 1

                freq[key] = count + 1

            return unique > 0

        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
