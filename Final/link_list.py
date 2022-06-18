class ListNode:
    def __init__(self, val=0, next= None):
        self.val = val
        self.next = next
def main():
    l1= ListNode(1,None)
    l1.next = ListNode(4,None)
    l1.next.next = ListNode(3, None)
    l1.next.next.next = ListNode(2, None)
    l1.next.next.next.next = ListNode(5, None)
    l1.next.next.next.next.next = ListNode(1, None)
    ans = problemFive(l1,3)
    travel(ans)
def problemFive(head:ListNode, x:int) -> ListNode:
    smell_head = ListNode(0,None)
    smell_cur = smell_head
    big_head = ListNode(0,None)
    big_cur = big_head
    cur = head
    while cur is not None:
        print(cur.val)
        if cur.val < x:
            smell_cur.next = ListNode(cur.val,None)
            smell_cur = smell_cur.next
        else:
            big_cur.next = ListNode(cur.val,None)
            big_cur = big_cur.next
        cur = cur.next
    smell_cur.next = big_head.next
    return smell_head.next

def travel(head):
    cur = head
    if cur is None:
        print("None")
    else:
        while cur.next is not None:
            print(cur.val, end='->')
            cur = cur.next
        print(cur.val)




if __name__ == '__main__':
    main()