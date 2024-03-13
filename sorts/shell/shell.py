def generate_sedgwick_sequence(n: int) -> list:
    seq = [1]

    while seq[-1] < n:
        seq.append((4**(len(seq)) + 3*2**(len(seq) - 1) + 1))

    seq.pop()
    seq.reverse()

    return seq


def shell_sort(to_sort: list) -> list:
    n = len(to_sort)

    seq = generate_sedgwick_sequence(n)

    for gap in seq:
        j = gap

        while j < n:
            i = j - gap
            
            while i >= 0:

                if to_sort[i+gap] > to_sort[i]:
                    break

                else:
                    to_sort[i+gap], to_sort[i] = to_sort[i], to_sort[i+gap]
                
                i -= gap

            j += 1
        
    return to_sort 
