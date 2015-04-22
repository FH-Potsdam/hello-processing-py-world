from tri import Tri

liste_of_tris = []
def setup():
    global liste_of_tris
    p1 = PVector(10, 10)
    p2 = PVector(30, 30)
    p3 = PVector(10, 30)
    # p4 will be the new point of the
    # second triangle
    p4 = PVector(50, 50)
    tri1 = Tri(p1, p2, p3)  # new object of class Tri
    #tri2 = Tri(tri1.p3, tri1.p2, p4)
    liste_of_tris.append(tri1)
    #liste_of_tris.append(tri2)
    #tri1.display_lines(255)
    #tri2.display_lines(0)
    #tri1.display_ellipse(255)
    # executed once
def draw():
    global liste_of_tris
    background(255)
    for i in range(0, len(liste_of_tris)):
        liste_of_tris[i].display_lines(0)
    # executed all the time
    
def mousePressed():
    global liste_of_tris
    p = PVector(random(width),random(height))
    my_tri = Tri(liste_of_tris[-1].p2,liste_of_tris[-1].p3, p)
    liste_of_tris.append(my_tri)
