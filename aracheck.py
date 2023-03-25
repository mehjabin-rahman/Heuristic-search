from anytimewastar import anytime_weighted_astar
from map1 import map
import time
if __name__ == '__main__':
    start = (55, 90)  # grid[0][GRID_Y - 1]
    goal = (36, 180)  # grid[GRID_X - 1][0]
    heuristic_weight = 3
    timer_start = time.time()
    (anytime_wastar_output, error) = anytime_weighted_astar(start, goal, map, heuristic_weight)
    timer_stop = time.time()
    print("Anytime A-star error: ", error)
    print("\nAnytime Weighted A-star\nExecution Time: ", timer_stop - timer_start)
