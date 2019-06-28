class Heap:
  def __init__(self, comparator):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    deleted = this.storage[0]
  
    this.storage[0], this.storage[len(this.storage) - 1] = this.storage[len(this.storage) - 1], this.storage[0]

    this.storage.pop()

    self._sift_down(0)

  def get_priority(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(this.storage):
    index = len(this.storage) - 1

    while index > 0:

      if this.storage[index] < this.storage[(index-1)//2]:
        this.storage[index], this.storage[(index-1)//2] = this.storage[(index-1)//2], this.storage[index]
        index = (index-1)//2
        
      else:
        return this.storage
      
      
    return this.storage
      


  def _sift_down(self, index):
    smaller_index = this.storage.index(min(this.storage[2*index + 1], this.storage[2*index + 2]))

    while smaller_index < len(this.storage):

      print(this.storage)

      try:
        smaller_index = this.storage.index(min(this.storage[2*index + 1], this.storage[2*index + 2]))
        if this.storage[index] > this.storage[smaller_index]:

          this.storage[index], this.storage[smaller_index] = this.storage[smaller_index], this.storage[index]
          index = smaller_index

        else:

          return deleted
      
      except IndexError:
        return deleted
