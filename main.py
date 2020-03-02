import matplotlib.pyplot as plt
import numpy as np
import math
import time

start_nodex = int(input("please enter start point x coordinate: "))
start_nodey = int(input("please enter start point y coordinate: "))

goal_nodex = int(input("please enter goal point x coordinate: "))
goal_nodey = int(input("please enter goal point y coordinate: "))

obstaclespace = np.zeros(shape=(int(201), int(301)))


# Geometrical definition of the obstacle space

## Defining the boundary walls
boundary_x = []
boundary_y = []

for i in range(301):
    boundary_x.append(i)
    boundary_y.append(0)
    obstaclespace[0][i] = 1

    boundary_x.append(i)
    boundary_y.append(200)
    obstaclespace[200][i] = 1

for i in range(201):
    boundary_x.append(0)
    boundary_y.append(i)
    obstaclespace[i][0] = 1

    boundary_x.append(300)
    boundary_y.append(i)
    obstaclespace[i][300] = 1

# Object 1 = Centre ellipse
centre_ellipse = []
major_axis = int(40)
minor_axis = int(20)

for x in range(251):
    for y in range(151):
        figure1 = (((x - 150) ** 2) / major_axis ** 2) + (((y - 100) ** 2) / minor_axis ** 2) - 1

        if figure1 <= 0:
            centre_ellipse.append((x, y))

centre_ellipse_x = [x[0] for x in centre_ellipse]
centre_ellipse_y = [x[1] for x in centre_ellipse]

for i in centre_ellipse:
    obstaclespace[i[1]][i[0]] = 1

# Object 2 = right corner Circle
rc_circle = []
for x in range(301):
    for y in range(201):
        figure2 = (x - 225) ** 2 + (y - 150) ** 2 - (25) ** 2
        if figure2 <= 0:
            rc_circle.append((x, y))

rc_circlex = [x[0] for x in rc_circle]
rc_circley = [x[1] for x in rc_circle]

for i in rc_circle:
    obstaclespace[i[1]][i[0]] = 1
