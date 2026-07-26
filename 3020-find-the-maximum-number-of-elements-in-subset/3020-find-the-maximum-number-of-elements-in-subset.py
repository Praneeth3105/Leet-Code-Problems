from collections import Counter

class Solution:
    def maximumLength(self, nums):
        count = Counter(nums)
        ans = 1

        # Handle 1 separately
        ones = count[1]
        if ones:
            ans = ones if ones % 2 == 1 else ones - 1

        for x in list(count.keys()):
            if x == 1:
                continue

            length = 0
            cur = x

            while count[cur] >= 2:
                length += 2
                cur = cur * cur

            if count[cur] >= 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans