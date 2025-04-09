# ✅ Prefix Sum + Palindrome Substring Queries

class Solution:
    def canMakePaliQueries(self, s, queries):
        n = len(s)
        prefix = [[0]*26 for _ in range(n+1)]

        # Precompute prefix character counts
        for i in range(n):
            ch_index = ord(s[i]) - ord('a')
            for j in range(26):
                prefix[i+1][j] = prefix[i][j] + (1 if j == ch_index else 0)

        result = []

        for left, right, k in queries:
            freq = [prefix[right+1][j] - prefix[left][j] for j in range(26)]
            odd_count = sum(1 for f in freq if f % 2 == 1)
            result.append(odd_count // 2 <= k)

        return result


# ✅ Example Usage
solution = Solution()
s = "abcda"
queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
print(solution.canMakePaliQueries(s, queries))  # Output: [True, False, False, True, True]