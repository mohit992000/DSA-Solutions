from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []  # This will hold all the valid combinations
        
        def backtrack(remain: int, combo: List[int], start: int):
            # If remain is zero, we've found a valid combination.
            if remain == 0:
                result.append(list(combo))
                return
            # If remain becomes negative, no valid combination can be found further.
            if remain < 0:
                return
            
            # Explore further candidates starting from the index 'start'
            for i in range(start, len(candidates)):
                # Add the candidate to the current combination.
                combo.append(candidates[i])
                # Recursively explore further with updated remaining target.
                backtrack(remain - candidates[i], combo, i)  # Not i+1 because the same candidate can be used again.
                # Remove the last candidate (backtracking) and try the next one.
                combo.pop()
        
        backtrack(target, [], 0)
        return result

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2, 3, 6, 7], 7))
    # Expected output: [[2, 2, 3], [7]]
