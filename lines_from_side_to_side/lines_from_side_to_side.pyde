'''
a simple sketch that draws
lines from top to bottom
and from left to right
'''
NUMBER_OF_LINES = 10

strokeWeight(random(0, 3))
# left to right
for i in range(0, NUMBER_OF_LINES):
    x1 = 0
    y1 = random(0, height)
    x2 = width
    y2 = random(0, height)
    line(x1, y1, x2, y2)
# top to bottom
for j in range(0, NUMBER_OF_LINES):
    x1 = random(0, width)
    y1 = 0
    x2 = random(0, width)
    y2 = height
    line(x1, y1, x2, y2)
