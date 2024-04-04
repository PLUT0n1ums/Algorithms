class MySet:
    def __init__(self):
        self.elements = []
    def add(self, x):
        if x not in self.elements:
            self.elements.append(x)
            self.elements.sort()
    def remove(self, x):
        if x in self.elements:
            self.elements.remove(x)
    def contains(self, x):
        return x in self.elements
