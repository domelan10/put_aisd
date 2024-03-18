import main as gen
import matplotlib.pyplot as plt
import math

from py_tests.test_size import test_slope, test_range, test_3_range

import sys
sys.setrecursionlimit(1000000000)

def test():
    # sorts = ["insertion", "selection", "quick_left", "quick_random", "heap", "shell"]
    sorts = ["quick_left", "quick_random"]
    tests = ["random", "increase", "decrease", "hill", "stable"]
    scale = [test_slope * i for i in range(1, test_range + 1)]

    for sort in sorts:
        print(f"Starting sort: {sort}")
        times = {}
        _, axes = plt.subplots()
        axes.set_title(f"Sort type: {sort}")
        axes.set_xlabel("Test size")
        axes.set_ylabel("Time of execution")

        for test in tests:
            print(f"\tStarting test: {test}")
            times[test] = [0]
            for test_size in scale:
                print(f"\tTest size: {test_size}")
                times[test].append(gen.main(f"{sort}", f"{test}", test_size))

            axes.plot([0]+[element for element in scale], times[test], label = f"{test}")

        axes.legend()
        print("\n")
    plt.show()

def data_test():
    sorts = ["insertion", "selection", "quick_left", "quick_random", "heap", "shell"]
    # sorts = ["shell"]
    tests = ["random", "increase", "decrease", "hill", "stable"]
    # tests = ["stable"]
    scale = [test_slope * i for i in range(1, test_range + 1)]

    for sort in sorts:
        print(f"Starting sort: {sort}")
        times = {}
        figure, axes = plt.subplots()
        axes.set_title(f"Sort type: {sort} (odchylenie standardowe)")
        axes.set_xlabel("Test size")
        axes.set_ylabel("Time of execution")

        for test in tests:
            print(f"\tStarting test: {test}")
            times[test] = [0]
            for test_size in scale:
                times[test].append([])
                test_avg = 0
                test_sum = 0
                
                for _ in range(0, test_3_range):
                    print(f"\tTest size: {test_size}")
                    times[test][-1].append(gen.main(f"{sort}", f"{test}", test_size))
                    test_avg += times[test][-1][-1]
                
                test_avg /= test_3_range
                
                for test_result in times[test][-1]:
                    test_sum += math.pow(test_result - test_avg, 2)
                
                times[test][-1] = math.pow(test_sum / test_3_range, 0.5)
            
            axes.plot([0]+[element for element in scale], times[test], label = f"{test}")
        
        axes.legend()
        print("\n")
    plt.show()

if __name__ == "__main__":
    test()
    # data_test()
