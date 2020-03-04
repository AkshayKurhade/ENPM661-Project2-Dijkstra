import matplotlib.pyplot as plt
import numpy as np
import math
import time
userdefined =False
if userdefined:
    start_nodex = int(input("please enter start point x coordinate: "))
    start_nodey = int(input("please enter start point y coordinate: "))

    goal_nodex = int(input("please enter goal point x coordinate: "))
    goal_nodey = int(input("please enter goal point y coordinate: "))
else:
    start_nodex=5
    start_nodey=5
    goal_nodex=195
    goal_nodey=195
obstaclespace = np.zeros(shape=(int(201), int(301)))

plt.plot(start_nodex, start_nodey, "Dr")
plt.plot(goal_nodex, goal_nodey, "Dr")

plotx = []
ploty = []

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
plt.scatter(centre_ellipse_x, centre_ellipse_y,color='b')
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
plt.scatter(rc_circlex, rc_circley,color='b')
for i in rc_circle:
    obstaclespace[i[1]][i[0]] = 1

# Object 3= bottom right quadrilateral
sideA = []
sideB = []
sideC = []
sideD = []
sideE = []

for x in range(301):
    for y in range(201):
        A = 3 * x + 5 * y - 875
        if A <= 0:
            sideA.append((x, y))

        B = 5 * y - 3 * x + 475
        if B <= 0:
            sideB.append((x, y))

        C = 5 * y + 3 * x - 725
        if B <= 0:
            sideC.append((x, y))

        D = 5 * y - 3 * x + 625
        if B <= 0:
            sideB.append((x, y))

        E = y - 25
        if E <= 0:
            sideE.append((x, y))

brquad = list(set(sideA) & set(sideB) & set(sideC) & set(sideD) & set(sideE))
x_brquad = [x[0] for x in brquad]
y_brquad = [x[1] for x in brquad]
plt.scatter(x_brquad, y_brquad,color='b')

for i in brquad:
    obstaclespace[i[1]][i[0]] = 1


# Object 4 = Bottom left rectangle
rect_side1 = []
rect_side2 = []
rect_side3 = []
rect_side4 = []
for x in range(301):
    for y in range(201):
        rect_line1 = 9 * y - 5 * x - 462
        if rect_line1 <= 0:
            rect_side1.append((x, y))
        rect_line2 = 65 * y + 38 * x - 6227
        if rect_line2 <= 0:
            rect_side2.append((x, y))
        rect_line3 = 9 * y - 5 * x + 205
        if rect_line3 <= 0:
            rect_side3.append((x, y))
        rect_line4 = 65 * y + 38 * x - 5560
        if rect_line4 <= 0:
            rect_side4.append((x, y))
blrectangle = list(set(rect_side1) & set(rect_side2) & set(rect_side3) & set(rect_side4))
x_blrectangle = [x[0] for x in blrectangle]
y_blrectangle = [x[1] for x in blrectangle]
plt.scatter(x_blrectangle, y_blrectangle,color='b')

for i in blrectangle:
    obstaclespace[i[1]][i[0]] = 1

# Object 5= Top Left quadrilateral
side1 = []
side2 = []
side3 = []
side4 = []
side5 = []
side6 = []
side7 = []
side8 = []
side9 = []

for x in range(301):
    for y in range(201):

        # Triangle A1

        line1 = y - 13 * x + 140
        if line1 <= 0:
            side1.append((x, y))
        line2 = y - x - 100
        if line2 <= 0:
            side2.append((x, y))
        line3 = 5 * y - 7 * x + 1100
        if line3 <= 0:
            side3.append((x, y))

        # Triangle A2
        line4 = y - 185
        if line4 <= 0:
            side4.append((x, y))
        line7 = x - 175
        if line7 <= 0:
            side7.append((x, y))
        line8 = 10 * y - 13 * x + 2175
        if line8 <= 0:
            side8.append((x, y))

        # Triangle A3

        line5 = 5 * y + 7 * x + 1450
        if line5 <= 0:
            side5.append((x, y))
        line6 = 5 * y - 6 * x + 150
        if line6 <= 0:
            side6.append((x, y))
        line7 = x - 75
        if line7 <= 0:
            side7.append((x, y))

triangle_A1 = list(set(side1) & set(side2) & set(side3))
triangle_A2 = list(set(side4) & set(side7) & set(side8))
triangle_A3 = list(set(side5) & set(side6) & set(side7))

tlquad = list(set(triangle_A1) | set(triangle_A2) | set(triangle_A3))
x_tlquad = [x[0] for x in tlquad]
y_tlquad = [x[1] for x in tlquad]
plt.scatter(x_tlquad, y_tlquad,color='b')

for i in brquad:
    obstaclespace[i[1]][i[0]] = 1
obstacle_t = obstaclespace.T
obs = []
for i in range(300):
    obs.append(obstacle_t[i])

plt.scatter(boundary_x, boundary_y, color='k')

plt.show()