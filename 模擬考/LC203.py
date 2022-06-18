class ListNode:
    def __init__(self, val= 0, next=None):
        self.val = val
        self.next = next
def main():
    l1 = ListNode(3, None)
    l1.next = ListNode(3, None)
    l1.next.next = ListNode(4, None)
    l1.next.next.next = ListNode(3, None)
    l1.next.next.next.next = ListNode(3, None)
    ans = removeElements(l1, 3)
    travel(ans)

def removeElements(head: ListNode, val: int) -> ListNode:
    cur = head
    dummy_head = ListNode(0, None)
    dummy = dummy_head
    while cur is not None:
        if cur.val == val:
            cur = cur.next
        else:
            dummy.next = cur
            cur = cur.next
            dummy = dummy.next


    return dummy_head.next

def travel(head):
    cur = head
    if cur is None:
        print("None")
    else:
        while cur.next is not None:
            print(cur.val, end='->')
            cur = cur.next
        print(cur.val)


if __name__ == "__main__":
    main()