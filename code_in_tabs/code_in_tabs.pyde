#
# for(int i = 0; i < 10; i++){
#}
# int i = 0;
#while(i < x){
#              }
# float [] x = new float[30]

from something import *
size(100,100)
number_of_circles = 300
circles = []

for i in range(0, number_of_circles):
    x = random(width)
    y = random(height)
    c = color(random(0, 255))
    circles.append([x, y, c])

for j in range(0, len(circles)):
    one_circle = circles[j] 
    fill(one_circle[2])
    ellipse(one_circle[0], one_circle[1],10,10)


