import main as gen
import matplotlib.pyplot as plt
from py_tests.test_size import test_slope, test_range

def test():
    sorts = [1, 2, 4, 5, 6, 8]
    tests = [1, 2, 3, 4, 5]
    scale = [test_slope * i for i in range(1, test_range + 1)]
    
    for sort in sorts:
        print(f"Starting sort: {sort}")
        times = {}
        for test in tests:
            print(f"\tStarting test: {test}")
            times[test] = []
            for test_size in scale:
                times[test].append(gen.main(f"{sort}", f"{test}", test_size))

            figure, axes = plt.subplots()
            axes.plot(scale, times[test])
            axes.set_title(f"Sort type: {sort}")
            axes.set_xlabel("Test size")
            axes.set_ylabel("Time of execution")
        plt.show()
        print("\n")

if __name__ == "__main__":
    test()