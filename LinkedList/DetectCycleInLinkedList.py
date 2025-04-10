# ✅ Detect Cycle in a Linked List using Floyd’s Cycle Detection Algorithm

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True  # Cycle found

        return False  # No cycle


# ⚠️ Test cases require linked list creation with cycle (not shown here)
# Use helper functions to build cycle-linked lists in test environments.