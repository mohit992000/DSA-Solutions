class Solution:
    def vowelStrings(self, words, queries):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Step 1: Compute prefix sum array
        n = len(words)
        vowel_prefix = [0] * (n + 1)

        for i in range(n):
            word = words[i]
            # Check if first and last character is a vowel
            if word[0] in vowels and word[-1] in vowels:
                vowel_prefix[i + 1] = vowel_prefix[i] + 1
            else:
                vowel_prefix[i + 1] = vowel_prefix[i]

        # Step 2: Answer queries efficiently
        result = []
        for li, ri in queries:
            result.append(vowel_prefix[ri + 1] - vowel_prefix[li])
        
        return result

# ✅ Example Usage:
solution = Solution()
words = ["aba", "bcb", "ece", "aa", "e"]
queries = [[0,2],[1,4],[1,1]]
print(solution.vowelStrings(words, queries))  # Expected Output: [2, 3, 0]

words2 = ["a", "e", "i"]
queries2 = [[0,2],[0,1],[2,2]]
print(solution.vowelStrings(words2, queries2))  # Expected Output: [3, 2, 1]