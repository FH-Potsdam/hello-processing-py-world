'''
This sketch calls a function several times
once in the setup
and all the time in the draw
'''
x1 = 10
y1 = 10
x2 = 50
y2 = 10
x3 = 25
y3 = 50

def setup():
    my_triangle()


def draw():
    my_triangle()

# draw a triangle
def my_triangle():
    beginShape()
    vertex(x1,y1)
    vertex(x2,y2)
    vertex(x3,y3)
    vertex(x1,y1)
    endShape()
    ellipse(x1,y1,5,5)
