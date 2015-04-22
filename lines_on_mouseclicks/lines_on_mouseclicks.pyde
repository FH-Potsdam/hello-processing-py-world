mouse_clicks = []
dist_x = 5
dist_y = 5

def draw_lines(x, y, x_dist, y_dist):
    number_of_lines = int(random(1, 24))
    distx = x_dist
    disty = y_dist
    x1 = x
    y1 = y
    x2 = x1 + distx
    y2 = y1

    for i in range(0, number_of_lines):
        # print i
        line(x1, y1, x2, y2)
        x1 = x1 + distx
        x2 = x1 + distx
        y1 = y1 + disty
        y2 = y1

def setup():
    size(640, 360)

def draw():
    global dist_x
    global dist_y

    for i in range(0, len(mouse_clicks)):
        # mouse_clicks[i][0] is the same as the two
        # lines below
        clicks = mouse_clicks[i]
        x = clicks[0]
        y = clicks[1]
        draw_lines(x,y ,dist_x, dist_y)

def mousePressed():
    global mouse_clicks
    x = mouseX
    y = mouseY
    mouse_clicks.append([x, y])

