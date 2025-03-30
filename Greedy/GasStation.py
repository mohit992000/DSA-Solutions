class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_tank = 0
        current_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            balance = gas[i] - cost[i]
            total_tank += balance
            current_tank += balance

            # If tank runs dry, try starting from next station
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0

        return start_index if total_tank >= 0 else -1


# ✅ Example usage:
solution = Solution()
print(solution.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))  # Output: 3
print(solution.canCompleteCircuit([2,3,4], [3,4,3]))          # Output: -1