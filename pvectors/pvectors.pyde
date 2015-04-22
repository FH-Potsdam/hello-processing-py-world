vectors = []

def setup():
    for i in range(0,10):
        vectors.append(PVector(random(width),random(height)))
    
    for j in range(0,len(vectors)):
        v = vectors[j]
        ellipse(v.x, v.y,10,10)
