class GUIStack:

	def __init__(self):
		self.items = []
		self.length = 0

	def isEmpty(self):
		if self.length == 0:
			return True
		else:
			return False

	def push(self, window):
		self.items.append(window)
		self.length += 1

	def pop(self):
		self.length -+ 1

	def peek(self):
		return self.items[0]