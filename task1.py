import sys


def taks1(n, m):
    circular_array = [i for i in range(1, n + 1)]
    path = []
    start = 0

    for _ in range(n - 1):
        start = (start + m - 1) % len(circular_array)
        path.append(circular_array[start])
        circular_array.pop(start)

    return ''.join(map(str, path))


if __name__ == "__main__":
    if len(sys.argv) == 3:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        result = taks1(n, m)
        print(result)
    else:
        print("Usage: python circular_array.py n m")
