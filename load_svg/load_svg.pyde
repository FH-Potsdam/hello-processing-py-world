'''
simple sketch that loads svg files
'''
# global scope
tropfen = ["circle1.svg","circle2.svg","circle3.svg"]

# setup executed one
def setup():
    print "these aren't the droids you are looking for"
# draw executed in a loop
def draw():
    noStroke() # dont want a stroke
    frameRate(3) # reduce the framerate
    fill(255) # make a white backgounrd
    rect(0, 0, width, height) # draw a rect as bg
    # select a random svg from the array
    tropf = tropfen[int(random(0, len(tropfen))) ]
    s = loadShape(tropf) # load the svg
    shape(s,0,0) # draw the svg

