from collections import defaultdict

class Solution:
    def findNumOfValidWords(self, words, puzzles):
        # Step 1: Create word bitmasks and store their frequencies
        word_mask_count = defaultdict(int)

        def get_bitmask(word):
            """Returns a bitmask representation of the word"""
            bitmask = 0
            for char in word:
                bitmask |= (1 << (ord(char) - ord('a')))
            return bitmask
        
        for word in words:
            mask = get_bitmask(word)
            word_mask_count[mask] += 1

        # Step 2: Process each puzzle
        results = []
        for puzzle in puzzles:
            first_letter_mask = 1 << (ord(puzzle[0]) - ord('a'))  # First letter must be included
            puzzle_mask = get_bitmask(puzzle)  # Create puzzle bitmask

            # Step 3: Generate all subsets of the puzzle bitmask
            subset = puzzle_mask
            total_valid_words = 0
            
            while subset:
                # Ensure the subset contains the first letter
                if subset & first_letter_mask:
                    total_valid_words += word_mask_count.get(subset, 0)

                # Generate the next subset
                subset = (subset - 1) & puzzle_mask  

            results.append(total_valid_words)

        return results

# ✅ Example Usage
solution = Solution()
words = ["apple","pleas","please"]
puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]
print(solution.findNumOfValidWords(words, puzzles))
# Expected Output: [0, 1, 3, 2, 0]