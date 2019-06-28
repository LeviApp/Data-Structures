"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
	def __init__(self, node=None):
		self.head = node
		self.tail = node
		self.length = 1 if node is not None else 0

	def __len__(self):
		return self.length

	def add_to_head(self, value):
		if self.head == None:
			node = ListNode(value)
			self.head = node
			self.tail = node
		else:
			node = ListNode(value)
			node.next = self.head
			self.head.prev = node
			self.head = self.head.prev
		
		self.length+=1

	def remove_from_head(self):
		removed_value = self.head.value
		if self.head == self.tail:
			self.head = None
			self.tail = None
		else:
			self.head.next = None
			self.head = self.next
			self.head.prev = None
		self.length-=1

		return removed_value
	



	def add_to_tail(self, value):
		if self.head == None:
			node = ListNode(value)
			self.head = node
			self.tail = node
		else:
			node = ListNode(value)
			node.prev = self.tail
			self.tail.next = node
			self.tail = self.tail.next
		self.length +=1

	def remove_from_tail(self):
		removed_value = self.tail.value

		if self.head == self.tail:
			self.head == None
			self.tail == None
		else:
			self.tail = self.tail.prev
			self.tail.next = None

		self.length -=1

		return removed_value


	def move_to_front(self, node):
			pass
		# if self.head == None:
		# 	return print('Nothing to move')

		# elif self.head == self.tail:
		# 	return print(f'{self.head}')

		# else:
		# 	node.delete()
		# 	self.add_to_head(node.value)

	def move_to_end(self, node):
			pass
		# if self.head == None:
		# 	return print('Nothing to move')

		# elif self.head == self.tail:
		# 	return print(f'{self.tail}')

		# else:
		# 	node.delete()
		# 	self.add_to_tail(node.value)

	def delete(self, node):
		deleted_node = node.value
		if self.head == None and self.tail == None:
			return
		
		elif self.head == self.tail:
			self.head = None
			self.tail = None

		elif self.head.value == node.value:
			self.head = self.head.next
			node.delete()

		elif self.tail.value == node.value:
			self.tail = self.tail.prev
			node.delete()
		
		else:
			node.delete()

		self.length -=1
		
		return deleted_node

	def get_max(self):
		maximum = self.head.value
		current = self.head

		while current.next:
			current = current.next
			if current.value > maximum:
				maximum = current.value
			
		
		return maximum


		
