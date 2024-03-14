import main as gen
import matplotlib.pyplot as plt
from py_tests.test_size import test_slope, test_range

def test():
    sorts = ["insertion", "selection", "quick_left", "quick_random", "heap", "shell"]
    # sorts = ["quick_left", "quick_random", "shell"]
    sorts_breaking = ["quick_left", "quick_random"]
    tests = ["random", "increase", "decrease", "hill", "stable"]
    tests_shell = ["random", "increase", "decrease", "hill"]
    scale = [test_slope * i for i in range(1, test_range + 1)]
    
    for sort in sorts:
        print(f"Starting sort: {sort}")
        times = {}
        figure, axes = plt.subplots()
        axes.set_title(f"Sort type: {sort}")
        axes.set_xlabel("Test size")
        axes.set_ylabel("Time of execution")
        
        for test in tests_shell if sort == "shell" else tests:
            print(f"\tStarting test: {test}")
            times[test] = []
            for test_size in scale:
                times[test].append(gen.main(f"{sort}", f"{test}", test_size // 20 if sort in sorts_breaking else test_size))

            axes.plot([element // 20 if sort in sorts_breaking else element for element in scale], times[test], label = f"{test}")
        
        axes.legend()
        print("\n")
    plt.show()

if __name__ == "__main__":
    test()