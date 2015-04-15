'''
lets use HSB
'''
colorMode(HSB,360,100,100)
size(100,360)
noStroke()
sat = 60
bright = 100
for myhue in range(0, height, 120):
    fill(myhue, sat, bright)
    rect(0, myhue, width, 120)
