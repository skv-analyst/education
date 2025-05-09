import json


def show_result(examples, solution, is_dict=None):
    for i, v in enumerate(examples):
        if is_dict:
            print(f"Example: {i + 1}. Values: {v}. Result: {solution(**v)}")
        else:
            print(f"Example: {i + 1}. Values: {v}. Result: {solution(v)}")


# LeetCode functions
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        arr = []
        head = self
        while head:
            arr.append(head.val)
            head = head.next
        return str(arr)


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def prettyPrintLinkedList(node):
    while node and node.next:
        print(str(node.val) + "->", end='')
        node = node.next

    if node:
        print(node.val)
    else:
        print("Empty LinkedList")


# 876. Middle of the Linked List
examples_876 = [stringToListNode("[1,2,3,4,5,6]")]


def solution_876(head):
    node_cnt = 0
    node = head

    while node:
        node_cnt += 1
        node = node.next

    steps_to_mid = node_cnt // 2

    while steps_to_mid:
        head = head.next
        steps_to_mid -= 1

    return head


def solution_876_2(head):
    turtle, leopard = head, head

    while leopard and leopard.next:
        turtle = turtle.next
        leopard = leopard.next.next

    return turtle


# 141. Linked List Cycle
examples_141 = [
    stringToListNode("[3,2,0,-4]"),
    stringToListNode("[1,2]"),
    stringToListNode("[1]")
]


def solution_141(head):
    # Time: O(n)
    # Space: O(n)
    seen = set()

    while head:
        if head in seen:
            return True

        seen.add(head)
        head = head.next

    return False


def solution_141_2(head):
    # Time: O(n)
    # Space: O(1)
    turtle = head
    leopard = head.next

    while leopard and leopard.next:
        if leopard == turtle:
            return True

        turtle = turtle.next
        leopard = leopard.next.next

    return False


# 203. Remove Linked List Elements
examples_203 = [
    {"head": stringToListNode("[1,2,6,3,4,5,6]"), "val": 6},
    {"head": stringToListNode("[]"), "val": 1},
    {"head": stringToListNode("[7,7,7,7]"), "val": 7}
]


def solution_203(head, val):
    # Time: O(n)
    # Space: O(n)

    arr = []

    while head:
        if head.val != val:
            arr.append(head.val)
        head = head.next

    head = ListNode(arr[0]) if len(arr) > 0 else None
    prev = head

    for i in range(1, len(arr)):
        cur = ListNode(arr[i])
        prev.next = cur
        prev = cur

    return head


def solution_203_2(head, val):
    dummy = ListNode(val=0, next=head)

    prev, cur = dummy, head

    while cur:
        if cur.val == val:
            prev.next = cur.next
        else:
            prev = cur

        cur = cur.next

    return dummy.next


# 83. Remove Duplicates from Sorted List
examples_83 = [
    stringToListNode("[1,1,2]"),
    stringToListNode("[1,1,2,3,3]"),
]


def solution_83(head):
    dummy = ListNode(val=None, next=head)
    prev, cur = dummy, head

    while cur:
        if prev.val == cur.val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next

    return dummy.next


# 206. Reverse Linked List
examples_206 = [
    stringToListNode("[1,2,3,4,5]"),
    stringToListNode("[1,2]"),
]


def solution_206(head):
    prev, cur = None, head

    while cur:
        temp_next = cur.next
        cur.next = prev
        prev = cur
        cur = temp_next

    return prev


# 21. Merge Two Sorted Lists
examples_21 = [
    {"list1": stringToListNode("[1,2,4]"), "list2": stringToListNode("[1,3,4]")},
    {"list1": stringToListNode("[]"), "list2": stringToListNode("[]")},
    {"list1": stringToListNode("[]"), "list2": stringToListNode("[0]")}
]


def solution_21(list1, list2):
    dummy = ListNode()
    prev = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            prev.next = list1

            prev = list1
            list1 = list1.next

        else:
            prev.next = list2

            prev = list2
            list2 = list2.next

    prev.next = list1 if list1 else list2

    return dummy.next


# 234. Palindrome Linked List
examples_234 = [
    stringToListNode("[1,2,2,1]"),
    stringToListNode("[1,2,]")
]


def solution_234(head):
    pass


# 160. Intersection of Two Linked Lists
examples_160 = [
    {"headA": stringToListNode("[4,1,8,4,5]"), "headB": stringToListNode("[5,6,1,8,4,5]")},
    {"headA": stringToListNode("[1,9,1,2,4]"), "headB": stringToListNode("[3,2,4]")}
]


def solution_160(headA, headB):
    seen = set()

    while headA:
        seen.add(headA)
        headA = headA.next

    while headB:
        if headB in seen:
            return headB
        headB = headB.next

    return None

if __name__ == '__main__':
    # show_result(examples_876, solution_876, is_dict=False)
    # show_result(examples_876, solution_876_2, is_dict=False)
    # show_result(examples_141, solution_141, is_dict=False)
    # show_result(examples_203, solution_203, is_dict=True)
    # show_result(examples_203, solution_203_2, is_dict=True)
    # show_result(examples_83, solution_83, is_dict=False)
    # show_result(examples_206, solution_206, is_dict=False)
    # show_result(examples_21, solution_21, is_dict=True)
    # show_result(examples_234, solution_234, is_dict=False)
    show_result(examples_160, solution_160, is_dict=True)
