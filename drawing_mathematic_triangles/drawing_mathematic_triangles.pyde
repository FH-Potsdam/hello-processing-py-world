def draw_triangle(p1, p2, p3, diameter):
    #  draw three ellipses at these points
    ellipse(p1.x, p1.y, diameter, diameter)
    ellipse(p2.x, p2.y, diameter, diameter)
    ellipse(p3.x, p3.y, diameter, diameter)
    # dont fill the triangle
    noFill()
    # draw the triangle
    beginShape()
    vertex(p1.x, p1.y)
    vertex(p2.x, p2.y)
    vertex(p3.x, p3.y)
    endShape(CLOSE)

def calc_lerp(p1, p4, amt):
    # http://py.processing.org/reference/lerp.html
    # lerp calculates a number between two numbers at a specific increment
    x = lerp(p1.x, p4.x, amt)
    y = lerp(p1.y, p4.y, amt)
    # just to see what is going on
#     print x, y
    # create a fifth point
    return PVector(x, y)

# calc the midpoint between p2 and p3
def calc_mid(p2, p3):
    xmid = (p2.x + p3.x) / 2
    ymid = (p2.y + p3.y) / 2
    # so we have a forth point
    return PVector(xmid, ymid)

# calculate the third point for a
# equalsided triangle
def calc_triangle(p1, p2):
    x3 = p1.x + (cos(atan2(p2.y - p1.y, p2.x - p1.x) - PI / 3)
                 * dist(p1.x, p1.y, p2.x, p2.y))
    y3 = p1.y + (sin(atan2(p2.y - p1.y, p2.x - p1.x) - PI / 3)
                 * dist(p1.x, p1.y, p2.x, p2.y))
    return PVector(x3, y3)


######################################

def setup():
    size(400, 400)
    diameter = 30
    # define first point
    p1 = PVector(diameter / 2, height - diameter / 2)
    # define second point
    p2 = PVector(width - diameter / 2, height - diameter / 2)
    # this is the result of the point calc
    p3 = calc_triangle(p1, p2)
    draw_triangle(p1, p2, p3, diameter)
    p4 = calc_mid(p2, p3)
    # ellipse(p3.x,p3.y,diameter,diameter)
    # draw a line from p1 to p4
    line(p4.x, p4.y, p1.x, p1.y)
    # create a fifth point
    p5 = calc_lerp(p1, p4, 0.09)
    # and draw the fifth point
    noStroke()
    fill(255, 0, 0)
    ellipse(p5.x, p5.y, diameter, diameter)
    p6 = calc_mid(p1, p3)
    ellipse(p6.x, p6.y, diameter, diameter)

