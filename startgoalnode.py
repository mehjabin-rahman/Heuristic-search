#from wastar import weighted_astar
from wAstar_withoutreopen import wastarw
#from Astar import astar
from wAstar_reopen import wastarr
#from anytimeWaStar import anytime_weighted_astar_threaded
#from anytimeweighted import anytime_weighted_astar
#from Visualization1 import visualize_predefined_map_and_path
#from combine import wastar,wastarReopen
import time
import random
from map1 import map


if __name__ == '__main__':
    #map = generate_manual_map()
    start = [(7, 0), (10, 0), (44, 1), (26, 3), (5, 6), (25, 0)]
    #hueristic_weight = 5
    hueristic_weight = 3
    '''
    start = (25, 2)
    goal = (30, 47)
    '''
    #start = (25, 0)
    #goal = (17, 47)
   # '''
    for x in range(0,100):
        print("instance :",x)
        print('-------------------------------------------------------------------------')

        i1=random.randrange(34,100)
        i2 = random.randrange(80, 250)
    #print(i1)
    #print(i2)
        g1 = random.randrange(210, 230)
        g2 = random.randrange(200, 260)
        start = (i1,i2 )
        goal = (g1, g2)
        print("[",i1,",",i2,",",g1,",",g2,"]")
        '''
        timer_start = time.time()
        astar_output = astar(start, goal, map)
        timer_stop = time.time()
        AT=timer_stop - timer_start
        #print("\nA-star\nExecution Time: ", timer_stop - timer_start)
        '''

        timer_start = time.time()
        wastar_output = wastarw(start, goal, map, 1,hueristic_weight)
        timer_stop = time.time()
        WAW=timer_stop - timer_start
        #print("\nwA-star (without)\nExecution Time: ", timer_stop - timer_start)

        timer_start = time.time()
        wastarReopen_output = wastarr(start, goal, map,1, hueristic_weight)
        timer_stop = time.time()
        WAR=timer_stop - timer_start
        #print("\nwA-star (reopen)\nExecution Time: ", timer_stop - timer_start)
        #print("\n","\t",WAW,"\t",WAR)
        '''
        timer_start = time.time()
        (anytime_wastar_output, error) = anytime_weighted_astar(start, goal, map, hueristic_weight)
        timer_stop = time.time()
        print("Anytime A-star error: ", error)
        print("\nAnytime Weighted A-star\nExecution Time: ", timer_stop - timer_start)
        '''
    '''
    timer_start = time.time()
    astar_output = astar(start, goal, map)
    timer_stop = time.time()
    print("\nA-star\nExecution Time: ", timer_stop - timer_start)

    timer_start = time.time()
    wastar_output = wastar(start, goal, map, hueristic_weight)
    timer_stop = time.time()
    print("\nwA-star (without)\nExecution Time: ", timer_stop - timer_start)

    timer_start = time.time()
    wastarReopen_output = wastarReopen(start, goal, map, hueristic_weight)
    timer_stop = time.time()
    print("\nwA-star (reopen)\nExecution Time: ", timer_stop - timer_start)

    '''
    '''
    regular_a_star_time = timer_stop-timer_start
    '''
    '''
    timer_start = time.time()
    wastar_output_reopen = weighted_astar(start, goal, map, hueristic_weight)
    timer_stop = time.time()
    print("\nweighted wA-star (reopen)\nExecution Time: ", timer_stop-timer_start)
    '''


    '''
    timer_start = time.time()
    (anytime_wastar_output, error) = anytime_weighted_astar(start, goal, map, hueristic_weight)
    timer_stop = time.time()
    print("Anytime A-star error: ", error)
    print("\nAnytime Weighted A-star\nExecution Time: ", timer_stop-timer_start)
    '''
    #visualize_predefined_map_and_path(map, wastar_output, -4, 'wastar-output')
    #visualize_predefined_map_and_path(map, astar_output, -4, 'wastar-output')
    #visualize_predefined_map_and_path(map, wastar_output, -4, 'wastar-output')
    #visualize_predefined_map_and_path(map, wastarReopen_output, -4, 'wastar-output')
    #visualize_predefined_map_and_path(map, wastar_output, -4, 'weighted-astar-output')
    #visualize_predefined_map_and_path(map, anytime_wastar_output, -4, 'anytime-weighted-astar-output')
