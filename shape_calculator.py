class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h
    
    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.width > 50 or self.width > 50:
            return "Too big for picture."
        else:
            picture = ""
            for n in range(self.height):
                picture += "*"*self.width + '\n'
            return picture

    def get_amount_inside(self, shape):
        cols = int(self.width / shape.width )
        rows = int(self.height / shape.height )
        return cols*rows

    def __str__ (self):
        return "Rectangle(width={0}, height={1})".format(self.width, self.height)
        
    
class Square(Rectangle):
    def __init__(self, s):
        self.width = s
        self.height = s

    def set_side(self, s):
        self.set_width(s)
        self.set_height(s)
    
    def set_width(self, s):
        self.width = s
        self.height = s

    def set_height(self,s):
        self.height = s
        self.width = s



    def __str__(self):
        return "Square(side={})".format(self.width)
