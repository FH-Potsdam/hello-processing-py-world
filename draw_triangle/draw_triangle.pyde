# create some empty lists
# this will hold the actual points
p1 = []
p2 = []
p3 = []
p4 = []
#this is a container for all the points
point_list = []

# a function that draws shapes from lists of points
def draw_triangle(p_list):
    beginShape()
    for i in range(0,len(p_list)):
        vertex(p_list[i][0], p_list[i][1])
    endShape()
    

def setup():
    # add some values to the points
    p1.append(10)
    p1.append(10)
    
    p2.append(30)
    p2.append(30)
    
    p3.append(10)
    p3.append(40)
    # last one is not necessary if you close the shape again
    p4.append(10)
    p4.append(10)
    
    # add the points to one list
    
    point_list.append(p1)
    point_list.append(p2)
    point_list.append(p3)
    point_list.append(p4)
    
    # call the function
    draw_triangle(point_list)
    
    # if you dont want to put them into a list
    # you can draw them by yourself
    #beginShape()
    #vertex(p1[0], p1[1])
    #vertex(p2[0], p2[1])
    #vertex(p3[0], p3[1])
    #vertex(p4[0], p4[1])
    #endShape()
