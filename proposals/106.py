def compute_next_position(current_position, n):
    x, y, z = current_position[0], current_position[1], current_position[2]

    return (y, z, (x + y + z) % n)

def bubble_sort(candidates):
    best_candidates = []

    for i in range(10):
        best_candidates.append((0, 0))

    for i in range(len(candidates)):
        for j in range(len(best_candidates)):
            if j < len(best_candidates) - 1:
                if candidates[i][1] > best_candidates[j + 1][1]:
                    mem = best_candidates[j+1]
                    best_candidates[j+1] = candidates[i]
                    best_candidates[j] = mem

    return best_candidates

def main():
    candidates = []
    best_n_candidates = []
    counter = 1
    n = 2
    
    while n <= 1000:
        current_position = compute_next_position((0,0,1), n)
        counter = 0

        while current_position != (0,0,1):
            current_position = compute_next_position(current_position, n)
            counter += 1
        
        candidates.append((n, counter))                
        n += 1

    best_candidates = bubble_sort(candidates)
    
    for i in range(len(best_candidates)):
        best_n_candidates.append(best_candidates[i][0])

    print(best_n_candidates)
    
if __name__ == "__main__":
    main()