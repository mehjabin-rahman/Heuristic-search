from Node import Node
from Open import Open
import multiprocessing
import time
import csv



def calculate_heuristic(start, goal, movement_cost):
    heuristic = (abs(start[0]-goal[0])+abs(start[1]-goal[1]))*movement_cost
    return heuristic

def calculate_zero_heuristic(start, goal, movement_cost):
    #heuristic = (abs(start[0]-goal[0])+abs(start[1]-goal[1]))*movement_cost
    return 0

def calculate_weighted_heuristic(start, goal, weight, movement_cost):
    heuristic = (abs(start[0]-goal[0])+abs(start[1]-goal[1]))*weight*movement_cost
    return heuristic


def retrace_path(start_node, node):
    path = []
    while(not(node == start_node)):
        path.append(node.state)
        node = node.parent
    path.append(node.state)
    #print("REopen expand: ",expand)
    return path
'''
def retrace_path1(start_node, node):
    path = []
    while(not(node == start_node)):
        path.append(node.state)
        node = node.parent
    path.append(node.state)
    print("REopen expand: ",expand)
    return path
'''
def verify_traversibility(map, neighbors=None):
    traversible_neighbors = []
    x_dims = len(map)
    y_dims = len(map[0])

    if(neighbors == None):
        return None
    for location in neighbors:
        if(location[0]>=x_dims or location[1]>=y_dims):
            continue
        if(not(map[location[0]][location[1]]=='T') and ((map[location[0]][location[1]]=='.') or (map[location[0]][location[1]]=='S') or (map[location[0]][location[1]]=='G'))):
            traversible_neighbors.append(location)
    return traversible_neighbors


def get_neighbors_4(node):
    moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    neighbors = []
    for move in moves:
        neighbor_state = (node.state[0]+move[0], node.state[1]+move[1])
        if(neighbor_state[0] < 0 or neighbor_state[1] < 0):
            continue
        neighbors.append(neighbor_state)
    return neighbors

def anytime_weighted_astarw(start, goal, map, hueristic_weight, movement_cost=1):

    start_node = Node(start, calculate_heuristic(start, goal, movement_cost), h_cost2=calculate_weighted_heuristic(start, goal, hueristic_weight, movement_cost))
    goal_node = Node(goal, 0, None, -1)
    open_list = Open()
    closed_list = {}
    open_list.anytime_insert(start_node)
    incumbent_node = None
    incumbent_flag = 0
    expand=0


    while(len(open_list)>0):
        try:
            current_node = open_list.next()
            '''
            if(current_node == goal_node):
                #print("Path found!")
                incumbent_flag = 1
                incumbent_node = current_node
                #time.sleep(0.5)
            '''
            if(incumbent_flag == 0):
                pass#The purpose for pass is to create empty blocks, it will do nothing
            elif((current_node<incumbent_node)[2]):
                pass
            else:
                continue

            closed_list[hash(current_node.state)] = current_node
            neighbors = current_node.get_neighbors()

            if(neighbors == None):
                continue

            neighbors = verify_traversibility(map, neighbors)

            for neighbor in neighbors:

                neighbor_node = Node(neighbor, calculate_heuristic(neighbor, goal, movement_cost), current_node, current_node.g_cost+movement_cost, calculate_weighted_hueristic(neighbor, goal, hueristic_weight, movement_cost))

                if(incumbent_flag == 0):
                    pass
                elif((neighbor_node<incumbent_node)[2]):
                    pass
                else:
                    continue

                if(neighbor_node == goal_node):
                    #print("Path found!")
                    incumbent_flag = 1
                    incumbent_node = neighbor_node
                    #time.sleep(0.5)

                output = open_list.test_membership(neighbor_node)

                if (output[0]):
                    node = output[1]

                    if((neighbor_node < node)[0]):
                        node.update(current_node, neighbor_node.g_cost, neighbor_node.h_cost, neighbor_node.h_cost2)

                elif(hash(neighbor_node.state) in closed_list):
                    node = closed_list.get(hash(neighbor_node.state))

                    if ((neighbor_node < node)[0]):
                        continue
                        #open_list.anytime_insert(neighbor_node)
                        #closed_list.pop(hash(neighbor_node.state))
                        #expand=expand+1

                else:
                    open_list.anytime_insert(neighbor_node)
                    expand=expand+1

        except KeyboardInterrupt:
            break

    if(len(open_list)==0):
        error = 0
    else:
        error = incumbent_node.f_cost-open_list.next().f_cost
    #print(expand)
    path = retrace_path(start_node, incumbent_node)
    return (path, error)
