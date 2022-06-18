"""
File: priority_queue_linked_list.py
Name: 
--------------------------
This file shows how to construct a linked list 
from scratch and use it to implement a priority queue.
"""


# It breaks the user inputs
EXIT = ''


class ListNode:
	def __init__(self, data, pointer):
		self.val = data
		self.next = pointer


def main():
	priority_queue = None

	print('--------------------------------')
	# TODO:
	while True:
		name = input("name :")
		if name == 'EXIT':
			break
		priorty = input("priorty :")
		new_node = ListNode((name, priorty), None)
	##### Construct linked_list #####
		if priority_queue == None:
			print("Original linked_list: ")
			priority_queue = new_node
		else:
		######## Prepend ########
			if priority_queue.val[1] > priorty:
				print("Prepend")
				new_node.next = priority_queue
				priority_queue = new_node
		#########################
			else:
		######## Append #########
		# print("Appending")
		# cur = priority_queue
		# while cur.next is not None:
		# 	cur = cur.next
		# cur.next = new_node
		#########################

		######### In between ############
				cur = priority_queue
				while True:
					# if cur.val[0] <= new_node.val[0] < cur.next.val[0] and cur.val[1] <= new_node.val[1] < cur.next.val[1]:
					if cur.next is None:
						print("append")
						cur.next = new_node
						break
					elif cur.val[1] <= priorty < cur.next.val[1]:
						print("In between")
						new_node.next = cur.next
						cur.next = new_node
						break
					else:
						print("cur go")
						cur = cur.next
					# elif cur.next is not None:
					# 	print("cur go")
					# 	cur = cur.next
					# else:
					# 	break
	print('--------------------------------')
	traversal(priority_queue)


def traversal(priority_queue):
	"""
	:param priority_queue: ListNode, holding the first ListNode object 
						   as the start of priority queue
	--------------------------
	This function prints out each val of a linked list
	"""
	cur = priority_queue
	while cur is not None:
		print(cur.val)
		cur = cur.next


if __name__ == '__main__':
	main()
