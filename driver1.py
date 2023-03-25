from map1 import map
from map2 import Map
import time
import random
from sg1 import input
from wAstar_withoutreopen import wastarw
from wAstar_reopen import wastarr
from reopen_good import reopengood
if __name__ == '__main__':

    # hueristic_weight = 5
    hueristic_weight = 3
    '''
    start = (25, 2)
    goal = (30, 47)
    '''
    # start = (25, 0)
    # goal = (17, 47)
    # '''
    #for x in range(0, 26):
    for x in range(0, 200):
        print("instance :", x)
        print('-------------------------------------------------------------------------')

        i1 = random.randrange(80, 100)
        i2 = random.randrange(300, 400)
            # print(i1)
            # print(i2)
        g1 = random.randrange(300, 500)
        g2 = random.randrange(400, 500)
        start = (i1, i2)
        goal = (g1, g2)
        print("[", i1, ",", i2, ",", g1, ",", g2, "]")

        timer_start = time.time()
        wastar_output = wastarw(start, goal, Map,hueristic_weight,x)
        timer_stop = time.time()
        WAT=timer_stop - timer_start
        #print("\nwA-star\nExecution Time: ", timer_stop - timer_start)

        #timer_start = time.time()
        #wastar_outputre = wastarr(start, goal, map, hueristic_weight, x)
        #timer_stop = time.time()
        #WAR = timer_stop - timer_start
        #print("\nwA-star\nwithreopen: ", timer_stop - timer_start)




