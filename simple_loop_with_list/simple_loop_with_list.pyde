'''
this sketch shows how to fill an array
with values and acces them later
'''

number_of_circles = 6 # the number of circles we want
my_list = [] # the list we will use to store coordiantes
# just do it once
def setup():
    # loop from 0 to 6
    for i in range(0, number_of_circles):
        # create a random value for x and y
        x1 = int(random(0, width))
        y1 = int(random(0, height))
        # store the values in an array in the array
        my_list.append([x1, y1])
        # print(i)
    # print(my_list)

    # now let's loop that list
    # we use len() to determine the number
    # of items in our list
    for j in range(0, len(my_list)):
        # draw at each coordiante an ellipse
        # j is between 0 and 6
        # 0 is x
        # 1 is y
        ellipse(my_list[j][0], my_list[j][1], 10, 10)

