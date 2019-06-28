class Node:
	def __init__(self,value, next_node)
		self.value = value
		self.next_node = next_node
	
	def get_value(self):
		return self.value
	
	def get_next(self):
		return self.next_node
	
	def set_next(self, new)
		self.next_node = new


class LinkedList:
	def __init__(self,head=None,tail=None):
		self.head = head
		self.tail = tail
	
	def enqueue(self, node):
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			self.tail.set_next(node)
			self.tail = node
			node.set_next(None)
	
	def dequeue(self):
		val = None

		if self.head == self.tail:

			val = self.head.get_value()

			self.head == None
			self.tail == None

		else:
			val = self.head.get_value()

			self.head = self.get_next()

		return print(f'{val} was deleted.')

	def len(self):
		count=0
		if self.head == 0:
			return count

		elif self.head == self.tail:
			return count + 1
		
		else:
			one_node = self.head
			while one_node.get_next() != None:
				count +=1
				one_node = one_node.get_next()



Q = LinkedList()

class Queue:
	def __init__(self):
		self.size = 0
	# what data structure should we
	# use to store queue elements?


	self.storage = Q

  


	  
