"""
File: word_linked_list.py
Name:
----------------------------
This program demonstrates constructing
a character-based linked list from the word
input by user.
"""


class ListNode:
    def __init__(self, data, pointer):
        self.val = data
        self.next = pointer


def main():
    word_linked = None
    word = input('word :')
    for ch in word:
        if word_linked is None:
            word_linked = ListNode(ch, None)
            cur = word_linked
        else:
            new_node = ListNode(ch, None)
            cur.next = new_node
            cur = cur.next

    traversal(word_linked)

def traversal(linked_list):
    cur = linked_list
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


if __name__ == '__main__':
    main()
