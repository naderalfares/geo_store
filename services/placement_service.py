from constants.opt_consts import FUNC_HEURISTIC_MAP

def min_cost():
    pass

def min_latency():
    pass

def brute_force():
    pass

def find_placement_wrapper(heuristic):
    eval(FUNC_HEURISTIC_MAP[heuristic])()
