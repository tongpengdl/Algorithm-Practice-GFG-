from ListNode import ListNode


def printList(head):
    temp = head
    while temp is not None:
        print temp.val,
        temp = temp.next


def construct_linkedList(lists=[]):
    if len(lists) == 0:
        return None
    elif len(lists) == 1:
        return lists[0]
    else:
        for i in range(len(lists) - 1):
            lists[i].next = lists[i + 1]


# 16. reverse a linkedList, iterative
def reverse_iter(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


# 16. reverse a linkedList, recursive
def reverse_rec(head):
    if head is None or head.next is None:
        return head
    next = head.next
    new_head = reverse_rec(next)
    next.next = head
    head.next = None
    return new_head


# 17. detect cycle in linkedlist
# proof: https://www.quora.com/How-does-Floyds-cycle-finding-algorithm-work
def detectloop_flag(head):
    if head is None or head.next is None:
        return "No loop"
    while head is not None and not head.is_visited:
        head.is_visited = True
        head = head.next

    if not head:
        return "No loop"
    else:
        return "find loop"


def detectloop_2pointer(head):
    if head is None or head.next is None:
        return "No loop"

    slow = head
    fast = head
    while fast and fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

        if fast is slow:
            return "find loop"
    return "No loop"


# 18.merge two linkedlists
def sorted_merge(l1, l2):
    dummy = ListNode(0)
    tail = dummy

    while l1 and l2:
        if l1.val > l2.val:
            tail.next = l2
            l2 = l2.next
        else:
            tail.next = l1
            l1 = l1.next
        tail = tail.next

    if l1:
        tail.next = l1
    else:
        tail.next = l2
    return dummy.next


def sorted_merge_rec(l1, l2):
    if not l1:
        return l2

    if not l2:
        return l1

    if l1.val > l2.val:
        res = l2
        res.next = sorted_merge(l1, l2.next)
    else:
        res = l1
        res.next = sorted_merge(l1.next, l2)
    return res


# 20.Given a linked list which is sorted, how will you insert in sorted way
def sortedInsert(head, n):
    """

    :param head: ListNode
    :param n: int
    :return: ListNode
    """
    new_node = ListNode(n)
    if head is None:
        return new_node
    elif head.val > n:
        new_node.next = head
        return new_node
    else:
        prev = None
        curr = head
        while curr and curr.val < n:
            prev = curr
            curr = curr.next
        prev.next = new_node
        new_node.next = curr
        return head


# 22.Function to check if a singly linked list is palindrome
def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head is None or head.next is None:
        return True

    middle = find_middle(head)
    second_half = middle.next
    middle.next = None

    second_half_rev = reverse(second_half)
    return compare(head, second_half_rev)


def reverse(head):
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def find_middle(head):
    if head is None or head.next is None:
        return head
    slow = head
    fast = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def compare(self, l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return True


# 34.Merge Sort for Linked Lists
def merge_sort(head):
    if head is None or head.next is None:
        return head
    first, second = divide_lists(head)
    if first is not second:
        sorted_first = merge_sort(first)
        sorted_second = merge_sort(second)
        return sorted_merge(sorted_first, sorted_second)
    else:
        return first

def divide_lists(head):
    if head is None or head.next is None:
        return (head, head)
    slow = head
    fast = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    next_half = slow.next
    slow.next = None
    return (head, next_half)

if __name__ == "__main__":
    l1 = ListNode(20)
    l2 = ListNode(10)
    l3 = ListNode(30)
    l4 = ListNode(80)

    l5 = ListNode(35)
    l6 = ListNode(102)
    l7 = ListNode(9)
    l8 = ListNode(98)
    l9 = ListNode(1)
    construct_linkedList([l1, l2, l3, l4, l5, l6, l7, l8, l9])

    printList(l1)
    print
    a = merge_sort(l1)
    printList(a)
