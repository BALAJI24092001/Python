# Topic : Linked Lists
# Status: Not Solved
# Date: 23/12/2024

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        val1 = ""
        while node1.next:
            val1 += str(node1.val)
            node1 = node1.next
        val1 += str(node1.val)
        val2 = ""
        while node2.next:
            val2 += str(node2.val)
            node2 = node2.next
        val2 += str(node2.val)
        fin = int(str(int(val1[::-1]) + int(val2[::-1]))[::-1])
        dummy = ListNode(0)
        cur = dummy
        for i in str(fin):
            cur.next = ListNode(val = int(i))
            cur = cur.next
        return dummy.next

# Error:
# TypeError: <__main__.ListNode object at 0x7f45fd319a50> is not valid value for the expected return type ListNode
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# raise TypeError(str(ret) + " is not valid value for the expected return type ListNode");
# Line 62 in _driver (Solution.py)
#     _driver()
# Line 71 in <module> (Solution.py)
# During handling of the above exception, another exception occurred:
# Exception: Type <class '__main__.ListNode'> cannot be serialized
# Line 138 in serializer_node (./python3/__serializer__.py)
# Line 181 in _serialize_default (./python3/__serializer__.py)
# Line 200 in _serialize (./python3/__serializer__.py)
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     out = ser._serialize(ret, 'ListNode')
# Line 60 in _driver (Solution.py)


```
Note: Optional is a type hint from the package typing. According to the use case in the above code, it can mean that, the output or input can either be a ListNode or a None value.
```
