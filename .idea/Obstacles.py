import numpy as np
import copy
from collections import deque


def ActionMoveLeft(CurrentNode, Parent): # Calculates if 0 can move to his left
    new_state = CurrentNode[:]
    index = new_state.index(0)

    if CurrentNode[0] > 0:    # Defines the boundary of a left move ( Needs to be checked)
        temp = new_state[index - -1]
        new_state[index - 1] = new_state[index]
        new_state[index] = temp

        Node = {'state': new_state, 'parent': Parent} # storage my new node in a dictionary with its respective parent, and index

        if Node['state'] == Parent: # compares if new node is equal to parent
            return -1 # returns a flag to avoid this calculation
        else:

            return Node
    else:   # return a flag if the move is not posible
        return -1


def ActionMoveRight(CurrentNode, Parent): # Same idea as ActionMoveLeft but applied to Right
    new_state = CurrentNode[:]
    index = new_state.index(0)

    if CurrentNode[0]<300:
        temp = new_state[index + 1]
        new_state[index + 1] = new_state[index]
        new_state[index] = temp

        Node = {'state': new_state, 'parent': Parent}

        if Node['state'] == Parent:
            return -1
        else:

            return Node
    else:
        return -1


def ActionMoveUp(CurrentNode, Parent): # Same idea as previous nodes
    new_state = CurrentNode[:]
    index = new_state.index(0)

    if CurrentNode[1] < 200:
        temp = new_state[index +1]
        new_state[index +1] = new_state[index]
        new_state[index] = temp

        Node = {'state': new_state, 'parent': Parent}

        if Node['state'] == Parent:
            return -1
        else:

            return Node
    else:
        return -1


def ActionMoveDown(CurrentNode, Parent):# Same idea as ActionMoveLeft but applied to Right
    new_state = CurrentNode[:]
    index = new_state.index(0)

    if CurrentNode[1]>0:
        temp = new_state[index -1]
        new_state[index -1] = new_state[index]
        new_state[index] = temp

        Node = {'state': new_state, 'parent': Parent}

        if Node['state'] == Parent:
            return -1
        else:

            return Node
    else:
        return -1


def ActionMoveUpperLeft(CurrentNode, Parent): # Same idea as ActionMoveLeft but applied to Right

        Node = {'state': new_state, 'parent': Parent}

        if Node['state'] == Parent:
            return -1
        else:

            return Node
    else:
        return -1


def ActionMoveUpperRight(CurrentNode, Parent): # Same idea as ActionMoveLeft but applied to Right
        Node = {'state': new_state, 'parent': Parent}

        if Node['state'] == Parent:
            return -1
        else:

            return Node
    else:
        return -1


def ActionMoveLowerLeft(CurrentNode, Parent): # Same idea as ActionMoveLeft but applied to Right
        Node = {'state': new_state, 'parent': Parent}

        if Node['state'] == Parent:
            return -1
        else:

            return Node
    else:
        # Can't move it, return None
        return -1


def ActionMoveLowerRight(CurrentNode, Parent): # Same idea as ActionMoveLeft but applied to Right
        Node = {'state':new_state, 'parent': Parent}
        if Node['state'] == Parent:
            return -1
        else:

            return Node
    else:
        return -1


def branch_nodes(Node, Parent): # funtion that determines the all the posible moves of cero. It returns my new nodes from its parent
    Nodes=[]
    #Nodes.append(ActionMoveUpperRight(Node, Parent)) # intend to calculate move in diagonal
    Nodes.append(ActionMoveLeft(Node, Parent))

    #Nodes.append(ActionMoveLowerLeft(Node, Parent))
    Nodes.append(ActionMoveRight(Node, Parent))

    Nodes.append(ActionMoveUp(Node, Parent))

    Nodes.append(ActionMoveDown(Node, Parent))
    #Nodes.append(ActionMoveUpperLeft(Node, Parent))
    #Nodes.append(ActionMoveLowerRight(Node, Parent))

    Nodes = [x for x in Nodes if x != -1]
    #print("exit branchs", Nodes)

    return Nodes


if __name__ == '__main__':
    #____Inicial Data
    Goal = []
    Initial = []
    x, y = input("Enter a two value: ").split()
    Goal_x, Goal_y = input(" Goal coordinates: x y ").split()
    In_x, In_y = input("Initial coordinates: x, y ").split()
    Goal=[Goal_x, Goal_y]
    Initial=[In_x, In_y]
    # # # # # # # # # P R O G R A M # # # # # # # # #  #  #
    nodes = deque()
    Parents = deque()
    New_Nodes = deque()
    father = {'state': Initial, 'parent': None}
    # Create the queue with the root node in it.
    node = copy.deepcopy(father)

    #New_Layer=[]
    Parents.append(node)

    x = 0


    while True:
        father = node['state']
        if node['state'] == Goal:
            break
        else:
            New_Nodes = branch_nodes(node['state'], father)  # calculate the possible nodes excluding the ones that have been already calculated.
            parentsStates = [parent['state'] for parent in Parents]
            for New_Node in New_Nodes:                                     # Condition to store only new nodes
                if New_Node['state'] not in parentsStates:
                    Parents.append(New_Node)
        node = Parents[x+1]                         # this instruction refress the node to continue with the next iteration
        x = x+1
        #print([parent['parent'] for parent in Parents])
    backParents = [parent for parent in Parents if parent['state'] == goal]
    print('Goal:\t\t', goal)
    print('Init:\t\t', In)

    while True:
        parentGoal = backParents[-1]
        if parentGoal['state'] == In:
            break
        parentForGoal = [parent for parent in Parents if parent['state'] == parentGoal['parent']]
        backParents.append(parentForGoal[0])
        #print(parentForGoal)
    # CHEcKING RESULTS

    # print([parent['Node_ind'] for parent in backParents])
    # print(len(backParents))


    for i in range(len(backParents)):

        print(backParents[-i-1]['state'])

