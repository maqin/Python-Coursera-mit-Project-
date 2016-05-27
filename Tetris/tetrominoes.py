__author__ = 'qingfei'
from graphics import *
class Block(Rectangle):
    BLOCK_SIZE = 30
    OUTLINE_WIDTH = 3
    def __init__(self,pos,color):
        self.x = pos.x
        self.y = pos.y
        p1 = Point(pos.x*Block.BLOCK_SIZE+Block.OUTLINE_WIDTH,
                   pos.y*Block.BLOCK_SIZE+Block.OUTLINE_WIDTH)
        p2 = Point(p1.x+Block.BLOCK_SIZE,
                   p1.y+Block.BLOCK_SIZE)
        Rectangle.__init__(self,p1,p2)
        self.setWidth(Block.OUTLINE_WIDTH)
        self.setFill(color)
    def draw(self, win):
        Rectangle.draw(self,win)

class Shape:
    def __init__(self,coords,color):
        self.blocks = []
        for pos in coords:
            self.blocks.append(Block(pos,color))

    def draw(self,win):
        for b in self.blocks:
            b.draw(win)

class I_shape(Shape):
    def __init__(self,center):
        coords = [Point(center.x - 2, center.y),
                  Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y)
                  ]
        Shape.__init__(self,coords,'blue')

class J_shape(Shape):
    def __init__(self,center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y),
                  Point(center.x + 1, center.y + 1)
                  ]
        Shape.__init__(self,coords,'orange')

class L_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x - 1, center.y + 1),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y)
                  ]
        Shape.__init__(self,coords,'BlueViolet')

class O_shape(Shape):
    def __init__(self,center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x - 1, center.y + 1),
                  Point(center.x    , center.y),
                  Point(center.x    , center.y + 1)
                  ]
        Shape.__init__(self,coords,'red')

class S_shape(Shape):
    def __init__(self,center):
        coords = [Point(center.x - 1, center.y + 1),
                  Point(center.x    , center.y),
                  Point(center.x    , center.y + 1),
                  Point(center.x + 1, center.y)
                  ]
        Shape.__init__(self,coords,'green')

class T_shape(Shape):
    def __init__(self,center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y),
                  Point(center.x    , center.y + 1)
                  ]
        Shape.__init__(self,coords,'yellow')

class Z_shape(Shape):
    def __init__(self,center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x    , center.y + 1),
                  Point(center.x + 1, center.y + 1)
                  ]
        Shape.__init__(self,coords,'red2')
win = GraphWin("Tetrominoes",900,150)
#block = Block(Point(4,4),'blue')
#block.draw(win)
#shape = I_shape(Point(3,1))
tetrominoes = [I_shape,J_shape,L_shape,O_shape,S_shape,T_shape,Z_shape]
x = 3
for tetromino in tetrominoes:
    shape = tetromino(Point(x, 1))
    shape.draw(win)
    x += 4
win.mainloop()