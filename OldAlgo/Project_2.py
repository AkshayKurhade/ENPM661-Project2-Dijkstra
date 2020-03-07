import numpy as np
import copy
from collections import deque
import time


# # # # # # # # # # A C T I O N S # # # # # # # # #
def ActionMoveLeft(CurrentNode, Parent, Cost): # Calculates if 0 can move to his left
    new_point =  [CurrentNode[0]-1, CurrentNode[1] +0]
    if new_point[0] >= 0 and new_point != Parent:
        Node = {'state': new_point, 'parent': Parent, 'Cost2come': 1}
        return Node
    else:
        # Can't move it, return None
        return -1


def ActionMoveRight(CurrentNode, Parent, Cost): # Same idea as ActionMoveLeft but applied to Right
    new_point =  [CurrentNode[0]+1, CurrentNode[1] +0]
    if new_point[0] <= 300 and new_point != Parent:
        Node = {'state': new_point, 'parent': Parent, 'Cost2come': 1}
        return Node
    else:
        # Can't move it, return None
        return -1


def ActionMoveUp(CurrentNode, Parent, Cost): # Same idea as previous nodes
    new_point =  [CurrentNode[0]+0, CurrentNode[1] +1]
    if new_point[1] <= 200 and new_point != Parent:
        Node = {'state': new_point, 'parent': Parent, 'Cost2come': 1}
        return Node
    else:
        # Can't move it, return None
        return -1


def ActionMoveDown(CurrentNode, Parent, Cost):# Same idea as ActionMoveLeft but applied to Right
    new_point = [CurrentNode[0] + 0, CurrentNode[1] - 1]
    if new_point[1] >= 0 and new_point != Parent:
        Node = {'state': new_point, 'parent': Parent, 'Cost2come': 1}
        return Node
    else:
        # Can't move it, return None
        return -1


def ActionMoveUpperLeft(CurrentNode, Parent, Cost): # Same idea as ActionMoveLeft but applied to Right
    new_point = [CurrentNode[0] - 1, CurrentNode[1] + 1]
    if new_point[0] >= 0 and new_point[1] <= 200 and new_point != Parent:

        Node = {'state': new_point, 'parent': Parent, 'Cost2come': 1.414}

        return Node
    else:
        # Can't move it, return None
        return -1


def ActionMoveUpperRight(CurrentNode, Parent, Cost): # Same idea as ActionMoveLeft but applied to Right
    new_point = [CurrentNode[0] + 1, CurrentNode[1] + 1]
    if new_point[0] <= 300 and new_point[1] <= 200 and new_point != Parent:

        Node = {'state': new_point, 'parent': Parent, 'Cost2come': 1.414}

        return Node
    else:
        # Can't move it, return None
        return -1


def ActionMoveLowerLeft(CurrentNode, Parent, Cost): # Same idea as ActionMoveLeft but applied to Right
    new_point =  [CurrentNode[0]-1, CurrentNode[1] -1]
    if new_point[0] >= 0 and new_point[1] >= 0 and new_point != Parent:

        Node = {'state': new_point, 'parent': Parent,  'Cost2come': 1.414}

        return Node
    else:
        # Can't move it, return None
        return -1


def ActionMoveLowerRight(CurrentNode, Parent, Cost): # Same idea as ActionMoveLeft but applied to Right
    new_point =  [CurrentNode[0]+1, CurrentNode[1] -1]

    if new_point[0] <= 300 and new_point[1] >= 0 and new_point != Parent:

        Node = {'state': new_point, 'parent': Parent, 'Cost2come': 1.414}

        return Node
    else:
        # Can't move it, return None
        return -1

def branch_nodes(Node, Parent, Cost): # funtion that determines the all the posible moves of cero. It returns my new nodes from its Parent
    Nodes=[]
    Nodes.append(ActionMoveUpperRight(Node, Parent, Cost)) # intend to calculate move in diagonal
    Nodes.append(ActionMoveRight(Node, Parent, Cost))
    Nodes.append(ActionMoveLowerRight(Node, Parent, Cost))
    Nodes.append(ActionMoveDown(Node, Parent, Cost))
    Nodes.append(ActionMoveLowerLeft(Node, Parent, Cost))
    Nodes.append(ActionMoveLeft(Node, Parent, Cost))
    Nodes.append(ActionMoveUpperLeft(Node, Parent, Cost))
    Nodes.append(ActionMoveUp(Node, Parent, Cost))
    Nodes = [x for x in Nodes if x != -1]
    #print("exit branchs", Nodes)

    return Nodes


if __name__ == '__main__':
    t0=time.time()
    #____Inicial Data
    Goal = []
    Initial = []
    #x, y = input("Enter a two value: ").split()
    #Goal_x, Goal_y = input(" Goal coordinates: x y ").split()
    #In_x, In_y = input("Initial coordinates: x, y ").split()
    #Goal=[Goal_x, Goal_y]
    #Initial=[In_x, In_y]
    Goal = [300, 200]
    Initial = [0, 0]
    # # # # # # # # # P R O G R A M # # # # # # # # #  #  #
    Cost2come = deque()
    Parents = deque()
    New_Nodes = deque()
    father = {'state': Initial, 'parent': None, 'Cost2come': 0}
    # Create the queue with the root node in it.
    node = copy.deepcopy(father)

    #New_Layer=[]
    Parents.append(node)
    x = 0

    while True:
        father = node['state']
        Cost = node['Cost2come']
        if node['state'] == Goal:
            break
        else:
            New_Nodes = branch_nodes(node['state'], father, Cost)  # calculate the possible nodes excluding the ones that have been already calculated.
            parentsStates = [parent['state'] for parent in Parents]
            #print("Parents new cycle ", Parents[x])
            #print("New Node ", [(New_Node['state'], New_Node['parent'], New_Node['Cost2come']) for New_Node in New_Nodes])

            for New_Node in New_Nodes:
                #print(parentsStates)
                #print(New_Node['state'], parentsStates)
                if New_Node['state'] in parentsStates:
                    #print(New_Node)
                    ind = parentsStates.index(New_Node['state'])
                    #print(ind)
                    #print(Parents[ind])
                    if Parents[ind]['Cost2come'] > New_Node['Cost2come']:
                        Parents[ind]=New_Node
                    #print(Parents[ind])
                if New_Node['state'] not in parentsStates:
                    Parents.append(New_Node)

        node = Parents[x+1]  # this instruction refress the node to continue with the next iteration
        #print(node)

        x = x+1
        #print([parent['parent'] for parent in Parents])
    backParents = [parent for parent in Parents if parent['state'] == Goal]
    print('Goal:\t\t', Goal)
    print('Init:\t\t', Initial)

    while True:
        parentGoal = backParents[-1]
        if parentGoal['state'] == Initial:
            break
        parentForGoal = [parent for parent in Parents if parent['state'] == parentGoal['parent']]
        backParents.append(parentForGoal[0])
        #print(parentForGoal)
    # CHEcKING RESULTS
    #print([parent['Cost2come'] for parent in backParents])
    #print(len(backParents))


    for i in range(len(backParents)):

        print(backParents[-i-1]['state'], backParents[-i-1]['Cost2come'])
    t1=time.time()
    print(t1-t0)
