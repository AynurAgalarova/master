import sys

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [int(line.strip()) for line in file]
        return numbers
    except FileNotFoundError:
        print("Файл не найден")
        sys.exit(1)
    except ValueError:
        print("Ошибка при чтении чисел из файла")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Используйте: python script.py filename")
        sys.exit(1)

    filename = sys.argv[1]
    numbers = read_file(filename)

    total = sum(numbers)
    print(f"Вывод в консоль: {total}")

if __name__ == "__main__":
    main()

def min_moves(nums):
    avg = sum(nums) // len(nums)
    moves = 0
    for num in nums:
        moves += abs(num - avg)
    return moves

# Пример
nums = [1, 2, 3]
print("Минимальное количество ходов:", min_moves(nums))
