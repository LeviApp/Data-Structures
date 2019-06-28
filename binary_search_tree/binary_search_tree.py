class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    current = self

    if value >= child.value:
      pass
      

  def contains(self, target):
    current = self

    if self.left == None and self.right == None and self.value != target:
      return False

    if self.left == None and self.right == None and self.value == target:
      return True

    if target == current.value:
      return True

    if target > current.value:
      current = self.right
      current.contains(target)

    if target < current.value:
      current = self.left
      current.contains(target)
  

  def get_max(self):
    if self.right == None:
      return self.value

    else:
      return self.right.get_max()

      

  def for_each(self, cb):
    pass