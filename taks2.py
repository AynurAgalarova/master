import sys
import math

def read_circle(file_path):
    with open(file_path, 'r') as file:
        x, y = map(int, file.readline().split())
        radius = int(file.readline())
        return x, y, radius

def read_points(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(int, line.split())
            points.append((x, y))
        return points

def point_position(xc, yc, radius, x, y):
    distance = math.sqrt((x - xc)**2 + (y - yc)**2)
    if distance == radius:
        return 0
    elif distance < radius:
        return 1
    else:
        return 2

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python point_position.py <circle_file> <points_file>")
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    circle_x, circle_y, radius = read_circle(circle_file)
    points = read_points(points_file)

    for point in points:
        result = point_position(circle_x, circle_y, radius, point[0], point[1])
        print(result)
