import sys

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = [int(line.strip()) for line in file.readlines()]
    return lines

def min_moves_to_same_number(nums):
    # Find the target number that minimizes the total moves
    target = sum(nums) // len(nums)

    # Calculate the total moves needed to reach the target number
    total_moves = sum(abs(num - target) for num in nums)

    return total_moves

def main():
    if len(sys.argv) != 2:
        print("Usage: python program.py input_file.txt")
        return

    input_file = sys.argv[1]

    nums = read_file(input_file)
    moves = min_moves_to_same_number(nums)

    print(moves)

if __name__ == "__main__":
    main()
