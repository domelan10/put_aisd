from show import print_graph
from generate import generate_30, generate_50, generate_70
from algorithms import DFS_Euler, hamilton_cycle
from time import time
import sys
import matplotlib.pyplot as plt

test_slope = 100
test_range = 10
sys.setrecursionlimit(1_000_000_000)

def test() -> None:
    scale = [test_slope * i for i in range(1, test_range + 1)]
    scale_for_broken = range(20, 23)
    # options = ["hamilton_30_70", "hamilton_50", "euler_30_70"]
    options = ["hamilton_50"] # change type of tests

    for option in options:
        match option:
            case "hamilton_30_70":
                print(f"Starting operation: {option}")
                _, axes = plt.subplots()
                axes.set_xlabel("Test size")
                axes.set_ylabel("Time of execution (seconds)")
                axes.set_title(f"Hamilton cycle t(n)")
                times = {}
                
                for data_type in ["filled 30%", "filled 70%"]:
                    times[data_type] = [0]
                    
                    for test_size in scale:
                        print(f"\tStarting test_size: {test_size}")
                        match data_type:
                            case "filled 30%":
                                print(f"\t\tStarting type: {data_type}")
                                graph = generate_30(test_size)
                                start = time()
                                hamilton_cycle(graph)
                                end = time()
                                
                            case "filled 70%":
                                print(f"\t\tStarting type: {data_type}")
                                graph = generate_70(test_size)
                                start = time()
                                hamilton_cycle(graph)
                                end = time()
                                
                        times[data_type].append(end - start)
                        
                    axes.plot([0]+[element for element in scale], times[data_type], label=data_type)
                    
                axes.legend()
                
            case "hamilton_50":
                print(f"Starting operation: {option}")
                _, axes = plt.subplots()
                axes.set_xlabel("Test size")
                axes.set_ylabel("Time of execution (seconds)")
                axes.set_title(f"Hamilton cycle t(n)")
                times = [0]
                
                for test_size in scale_for_broken:
                    print(f"\tStarting test_size: {test_size}")
                    graph = generate_50(test_size)
                    start = time()
                    hamilton_cycle(graph)
                    end = time()
                    times.append(end - start)
                    
                axes.plot([element for element in scale_for_broken], times, label="filled 50% (n ∈ <20-22>)")
                axes.legend()
                
            case "euler_30_70":
                print(f"Starting operation: {option}")
                _, axes = plt.subplots()
                axes.set_xlabel("Test size")
                axes.set_ylabel("Time of execution (seconds)")
                axes.set_title(f"Euler cycle t(n)")
                times = {}
                
                for data_type in ["filled 30%", "filled 70%"]:
                    times[data_type] = [0]
                    
                    for test_size in scale:
                        print(f"\tStarting test_size: {test_size}")
                        match data_type:
                            case "filled 30%":
                                print(f"\t\tStarting type: {data_type}")
                                graph = generate_30(test_size)
                                start = time()
                                DFS_Euler(graph)
                                end = time()
                                
                            case "filled 70%":
                                print(f"\t\tStarting type: {data_type}")
                                graph = generate_70(test_size)
                                start = time()
                                DFS_Euler(graph)
                                end = time()
                                
                        times[data_type].append(end - start)
                        
                    axes.plot([0]+[element for element in scale], times[data_type], label=data_type)
                    
                axes.legend()
                
    print("\n")
    plt.show()

if __name__ == '__main__':
    test()
    