from Node import Node
from Open import Open


# h cost
def calculate_hueristic(start, goal):
    heuristic = (abs(start[0]-goal[0])+abs(start[1]-goal[1]))
    return heuristic

def calculate_zero_hueristic(start, goal):
    #heuristic = (abs(start[0]-goal[0])+abs(start[1]-goal[1]))
    return 0
# wh cost
def calculate_weighted_hueristic(start, goal, weight):
   # print(type(start))
    heuristic = (abs(start[0]-goal[0])+abs(start[1]-goal[1]))*weight
    return heuristic


def retrace_path(start_node, node):
    pathlength=0
    path = []
    while(not(node == start_node)):
        pathlength+=1
        path.append(node.state)
        node = node.parent
    path.append(node.state)
    #print("wA* (without) path length =",pathlength)
    return path


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


def wastarr(start, goal, map,hueristic_weight=1, movement_cost=1):
    node_expanded=0
    cost_so_far=[]
    #-----------
    dhlist_status=[]
    dhlist_g=[]
    dhlist_h=[]
    newcost=0
    #fvalue=[]
    goal_node = Node(goal, 0, None, -1)
    start_node = Node(start, calculate_weighted_hueristic(start, goal,hueristic_weight))
    goal_node = Node(goal, 0, None, -1)
    open_list = Open()
    closed_list = {}
    open_list.insert(start_node)

    while(len(open_list)>0):

        current_node = open_list.next()
        if(current_node == goal_node):
            solution = retrace_path(start_node, current_node)
            return solution
            #return node_expanded

        closed_list[hash(current_node.state)] = current_node
        neighbors = current_node.get_neighbors()
        if(neighbors != None):
            pass
        neighbors = verify_traversibility(map, neighbors)
        for neighbor in neighbors:

            #neighbor_node = Node(neighbor, calculate_hueristic(neighbor, goal, movement_cost), current_node, current_node.g_cost+movement_cost)
            neighbor_node = Node(neighbor, calculate_weighted_hueristic(neighbor, goal,hueristic_weight), current_node,
                                 current_node.g_cost + movement_cost)
            newcost= current_node.g_cost+movement_cost
            dhlist_status.append(neighbor_node)
            dhlist_g.append(neighbor_node.g_cost)
            dhlist_h.append(neighbor_node.h_cost)
            if(neighbor_node == goal_node):
                solution = retrace_path(start_node, neighbor_node)
                #print("wA* (reopen) node expand :",node_expanded)
                print(node_expanded)
                return solution
                #return node_expanded

            output = open_list.test_membership(neighbor_node)
            if (output[0]):
                node = output[1]
                if((neighbor_node < node)[0]):
                    node.update(current_node, neighbor_node.g_cost, (hueristic_weight*neighbor_node.h_cost))

            elif(hash(neighbor_node.state) in closed_list):
                #print("Notreopen\t", neighbor_node.g_cost, "\t", neighbor_node.h_cost, "\t", neighbor_node.f_cost)

                #continue
                node = closed_list.get(hash(neighbor_node.state))
                if ((neighbor_node < node)[0]):
                    #continue
                    closed_list.pop(hash(neighbor_node.state))
                    open_list.insert(neighbor_node)
                    node_expanded = node_expanded + 1
                    #print("reopen")
            else:
                cost_so_far.append(newcost)
                open_list.insert(neighbor_node)
                node_expanded=node_expanded+1
                #print("fvalue,g,h : ", Node.f_cost2, Node.g_cost, Node.h)

    print('PATH NOT FOUND')
    return None
    #return node_expanded
