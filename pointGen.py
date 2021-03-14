import math
import sys

pi = math.pi

r = 12
n = 100

pts = [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r) for x in range(0,n+1)]

for pt in pts:
    print(pt)