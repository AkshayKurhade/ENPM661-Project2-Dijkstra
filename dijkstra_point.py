import time
from dijkstra_functions import *
from finalmap import *

userdefined = False
if userdefined:
    start_nodex = int(input("please enter start point x coordinate: "))
    start_nodey = int(input("please enter start point y coordinate: "))

    goal_nodex = int(input("please enter goal point x coordinate: "))
    goal_nodey = int(input("please enter goal point y coordinate: "))
else:
    start_nodex = 5
    start_nodey = 5
    goal_nodex = 295
    goal_nodey = 5

start_pos = (start_nodex, start_nodey)
goal_pos = (goal_nodex, goal_nodey)
plt.plot(start_nodex, start_nodey, "Dr")
plt.plot(goal_nodex, goal_nodey, "Dr")

start_time = time.time()

if __name__ == '__main__':
    final_obs, wall_x, wall_y = finalmap()
    if start_pos in (zip(wall_x, wall_y) or final_obs):
        print("Start Position in obstacle space")

    elif goal_pos in (zip(wall_x, wall_y) or final_obs):
        print("goal Position in obstacle space")

    else:
        path = dijkstra(start_pos, goal_pos, final_obs)
        if path is not None:
            scatterx = [x[0] for x in path]
            scattery = [x[1] for x in path]
            plt.plot(scatterx, scattery, color='r', linewidth=4)
            elapsed_time = time.time() - start_time
            print("Time Required to Solve ", round(elapsed_time, 2), "seconds")
        else:
            print("No path found")
