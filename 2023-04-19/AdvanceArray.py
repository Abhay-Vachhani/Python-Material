class AdvanceArray(list):
    def __init__(self, array=[]):
        self.type = None
        if len(array) != 0:
            self.type = type(array[0])
        
        self.array = []
        for elem in array:
            if type(elem) == self.type:
                self.array.append(elem)
    
    def __str__(self):
        return str(self.array)
    
    def append(self, elem):
        if type(elem) == self.type:
            self.array.append(elem)
    
    def remove(self, elem):
        self.array.remove(elem)

    def pop(self, index = -1):
        return self.array.pop(index)
    
    def insert(self, index, elem):
        self.array.insert(index, elem)

x = AdvanceArray(['1', 3, '4'])
x.append(10)
x.append('3')
x.append('4')
x.append('8')
x.append('9')
x.append('10')
