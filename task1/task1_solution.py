from itertools import cycle

if __name__ == '__main__':
    n, m = input().split()
    array_cycle = cycle([x for x in range(1, n + 1)])
    count = 1
    result = '1'
    next_item = next(array_cycle)
    while True:
        count += 1
        num = next(array_cycle)
        if num == 1 and count % m == 0:
            break
        elif count == m and num != 1:
            count = 1
            result += str(num)
    print(result)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        result = circular_array_path(n, m)
        print(result)
    else:
        print("Usage: python circular_array.py n m")
