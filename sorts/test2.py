import main as gen
import matplotlib.pyplot as plt
from py_tests.test_size import test_slope, test_range

import sys
sys.setrecursionlimit(1000000000)

def test():
    sorts = ["insertion", "selection", "quick_left", "quick_random", "heap", "shell"]
    tests = ["random", "increase", "decrease", "hill", "stable"]
    scale = [test_slope * i for i in range(1, test_range + 1)]
    
    for test in tests:
        print(f"Starting test: {test}")
        times = {}
        _, axes = plt.subplots()
        axes.set_title(f"Test type: {test}")
        axes.set_xlabel("Test size")
        axes.set_ylabel("Time of execution")
        
        for sort in sorts:
                print(f"\tStarting sort: {sort}")
                times[test] = [0]
                for test_size in scale:
                    print(f"\tTest size: {test_size}")
                    times[test].append(gen.main(f"{sort}", f"{test}", test_size))

                axes.plot([0]+[element for element in scale], times[test], label = f"{sort}")
        
        axes.legend()
        print("\n")
    plt.show()

if __name__ == "__main__":
    test()