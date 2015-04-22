zufall = random(3)
x = width / 2
y = height / 2
multiplier = random(5,15)
p = PVector(x, y)
p1 = PVector(random(width), random(height))

if zufall > 1.5:
    rectMode(CENTER)
    rect(p.x, p.y, zufall * multiplier, zufall * multiplier)
else:
    ellipse(p.x, p.y, zufall * multiplier, zufall * multiplier)

line(p.x,p.y,p1.x,p1.y)

line(p1.x,p1.y, 0, 0)
