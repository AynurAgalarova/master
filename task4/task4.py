import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def min_moves(nums):
    if not nums:
        return 0
    gcd_val = nums[0]
    for num in nums[1:]:
        gcd_val = gcd(gcd_val, num)
    return sum(abs(num - gcd_val) for num in nums)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python program.py input_file")
        sys.exit(1)
    input_file = sys.argv[1]
    with open(input_file, 'r') as file:
        nums = [int(line.strip()) for line in file]
    print("Минимальное количество ходов:", min_moves(nums))

