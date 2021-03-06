# ENPM661-Project 2
## Implementation of Dijkstra algorithm for a Point and Rigid Robot
Fig. Final Obstacle Map
    ![alt text](https://github.com/AkshayKurhade/ENPM661-Project2-Dijkstra/blob/master/OldAlgo/map.png "Map Title Text 1")
## Libraries used
    1) Matplotlib
    2) Numpy
    3) Time
    4) Math
    5) heapq
 Warning - Use of 'heapq' may generate low memory or running out of memory error
## Files required in the source directory
    1) dijkstra_point and/or dijkstra_rigid.py
    2) finalmap.py
    3) dijkstra_functions.py
## How to run the code-
 ### System Requirements-
        Python v3.0.x or later
 ### Set the User Defined Co-ordinates Flag in 'main.py'
        True= User inputs the initial and goal configuration.
        False- Pre-defined initial and goal configuration.
 ### Input arguements-
 #### For Point Robot(dijkstra_point.py)
        1) Input Start point x co-ordinate - Enter X co-ordinate of start position.
        2) Input Start point y co-ordinate - Enter Y co-ordinate of start position.
        3) Input Goal point x co-ordinate - Enter X co-ordinate of goal position.
        4) Input Goal point y co-ordinate - Enter Y co-ordinate of goal position.
 #### For Rigid Robot(dijkstra_rigid.py)
        1) Input Start point x co-ordinate - Enter X co-ordinate of start position.
        2) Input Start point y co-ordinate - Enter Y co-ordinate of start position.
        3) Input Goal point x co-ordinate - Enter X co-ordinate of goal position.
        4) Input Goal point y co-ordinate - Enter Y co-ordinate of goal position.
        5) Input Radius of the robot      - Enter Radius of the robot
        
Note: If the radius of the robot is bigger than 15 this will cause the map to look distored. But will still calculate optimal path following the conditions.
 ## Runtime
    Runtime for:
        Start Position=(5,5)
        Goal Position =(295,195)
        Average ~ 9.2-10.3 seconds
    Figure:- Final Path for (5,5) to (295,195)
    
   ![alt text](https://github.com/AkshayKurhade/ENPM661-Project2-Dijkstra/blob/master/OldAlgo/path_point.png "Map Title Text 1")
   
