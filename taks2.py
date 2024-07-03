import sys
import math

def read_circle_data(filename):
    with open(filename, 'r') as f:
        x, y = map(float, f.readline().strip().split())
        radius = float(f.readline().strip())
    return x, y, radius

def read_points_data(filename):
    points = []
    with open(filename, 'r') as f:
        for line in f:
            if line.strip():
                x, y = map(float, line.strip().split())
                points.append((x, y))
    return points

def point_position_to_circle(center_x, center_y, radius, point_x, point_y):
    distance = math.sqrt((point_x - center_x)**2 + (point_y - center_y)**2)
    if abs(distance - radius) < 1e-9:  # точка лежит на окружности
        return 0
    elif distance < radius:  # точка внутри окружности
        return 1
    else:  
        return 2

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <circle_file> <points_file>")
        sys.exit(1)
    
    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    
    center_x, center_y, radius = read_circle_data(circle_file)
    points = read_points_data(points_file)
