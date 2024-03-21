class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    dummy = ListNode()  # Dummy node to start the merged list
    current = dummy  # Pointer to traverse the merged list

    # Traverse both lists simultaneously
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Append remaining nodes from list1 or list2 if any
    current.next = list1 if list1 else list2

    return dummy.next  # Return the head of the merged list

# Example usage:
# Define linked lists
list1 = ListNode(1, ListNode(3, ListNode(5)))
list2 = ListNode(2, ListNode(4, ListNode(6)))

# Merge lists
merged_list = merge_two_lists(list1, list2)

# Print the merged list
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
