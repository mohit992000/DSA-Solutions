import collections
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list) -> int:
        # Convert wordList to a set for fast lookups
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        # Initialize BFS queue: (current_word, number_of_steps)
        queue = collections.deque([(beginWord, 1)])
        
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            # For every possible transformation, try all letters at each position
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordSet:
                        wordSet.remove(newWord)  # Remove to prevent revisiting
                        queue.append((newWord, steps + 1))
        
        return 0

# Example usage:
solution = Solution()
print(solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # Expected output: 5
print(solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))          # Expected output: 0