class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_circumference(self):
        return self.length + self.length + self.width + self.width

    def calculate_area(self):
        return self.length * self.width