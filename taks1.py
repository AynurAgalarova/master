import sys

def circular_array_path(n, m):
    circular_array = list(range(1, n + 1))
    path = []

    current_index = 0
    while len(path) < n:
        path.append(circular_array[current_index])
        current_index = (current_index + m - 1) % len(circular_array)
        circular_array.pop(current_index)
        if circular_array:
            current_index %= len(circular_array)
    
    return path

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py n m")
    else:
        try:
            n = int(sys.argv[1])
            m = int(sys.argv[2])
            result = circular_array_path(n, m)
            print("".join(map(str, result)))
        except ValueError:
            print("Error: Both arguments n and m should be integers.")
