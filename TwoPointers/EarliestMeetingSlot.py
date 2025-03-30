# ✅ Earliest Meeting Slot - Two Pointers Approach

class Solution:
    def minAvailableDuration(self, slt1, slt2, d):
        i, j = 0, 0

        while i < len(slt1) and j < len(slt2):
            start = max(slt1[i][0], slt2[j][0])
            end = min(slt1[i][1], slt2[j][1])

            if end - start >= d:
                return [start, start + d]

            if slt1[i][1] < slt2[j][1]:
                i += 1
            else:
                j += 1

        return []

# ✅ Example Usage
solution = Solution()
print(solution.minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8))   # [60, 68]
print(solution.minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 12))  # []