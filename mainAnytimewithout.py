from map1 import map
import time
import random
from sg1 import input
from anytimewastarwithout import anytime_weighted_astarw
from wAstar_withoutreopen import wastarw
from wAstar_reopen import wastarr
from reopen_good import reopengood
from anytimewastarwithreopen import anytime_weighted_astar
if __name__ == '__main__':
    start = [(7, 0), (10, 0), (44, 1), (26, 3), (5, 6), (25, 0)]
    # hueristic_weight = 5
    hueristic_weight = 30
    '''
    start = (25, 2)
    goal = (30, 47)
    '''
    # start = (25, 0)
    # goal = (17, 47)
    # '''
    for x in range(0, 200):
        #print("instance :", x)
        #print('-------------------------------------------------------------------------')

        # i1=random.randrange(0,250)
        # i2 = random.randrange(0, 250)
        # print(i1)
        # print(i2)
        # g1 = random.randrange(10, 250)
        # g2 = random.randrange(10, 250)
        start = (input[x][0], input[x][1])
        goal = (input[x][2], input[x][3])
        #start = (reopengood[x][0], reopengood[x][1])
        #goal = (reopengood[x][2], reopengood[x][3])
        '''

        timer_start = time.time()
        wastar_output = wastarw(start, goal, map,hueristic_weight,x)
        timer_stop = time.time()
        WAT=timer_stop - timer_start
        #print("\nwA-star\nExecution Time: ", timer_stop - timer_start)
        '''

        timer_start = time.time()
        anytimewastar_outputw = anytime_weighted_astarw(start, goal, map, hueristic_weight)
        timer_stop = time.time()
        WAR = timer_stop - timer_start
        #print("\nwA-star\nwithreopen: ", timer_stop - timer_start)
        '''
        print("Without : ",WAT,"Reopen :",WAR)
        '''
    # visualize_predefined_map_and_path(map, wastar_output, -4, 'wastar-output')
    # visualize_predefined_map_and_path(map, astar_output, -4, 'wastar-output')
    # visualize_predefined_map_and_path(map, wastar_output, -4, 'wastar-output')
    # visualize_predefined_map_and_path(map, wastarReopen_output, -4, 'wastar-output')
    # visualize_predefined_map_and_path(map, wastar_output, -4, 'weighted-astar-output')
    # visualize_predefined_map_and_path(map, anytime_wastar_output, -4, 'anytime-weighted-astar-output')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
