def setup():
    size(300,200)

def draw():
    print "Hello Draw"

def mousePressed():
    x = random(width)
    y = random(height)
    ellipse(x,y, 10, 10)
    h = hour()
    mi = minute()
    s = second()
    y = year()
    mo = month()
    d = day()
    timestamp = str(y) + str(mo) + str(d) +"-" + str(h) + str(mi) + str(s) 
    saveFrame("my-image-" + timestamp +".png")
