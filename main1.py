from map1 import map
import time
import random
from sg1 import input
from iwAstar_withoutreopen import wastarw
from iwAstar_reopen import wastarr
from reopen_good import reopengood
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
    for x in range(0, 205):
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
        wastar_outputre = wastarr(start, goal, map, hueristic_weight, x)
        timer_stop = time.time()
        WAR = timer_stop - timer_start
        #print("\nwA-star\nwithreopen: ", timer_stop - timer_start)
        '''
        print("Without : ",WAT,"Reopen :",WAR)
        '''
