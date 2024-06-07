import json

def calculate_position(center, radius, points):
    results = []
    for point in points:
        distance_squared = (point[0] - center[0])**2 + (point[1] - center[1])**2
        if distance_squared < radius**2:
            results.append(1)  # Inside
        elif distance_squared == radius**2:
            results.append(0)  # On the circle
        else:
            results.append(2)  # Outside
    return results

def main(values_file, tests_file, report_file):
    with open(values_file, 'r') as f:
        values_data = json.load(f)
    with open(tests_file, 'r') as f:
        tests_data = json.load(f)

    center = values_data['center']
    radius = values_data['radius']
    points = tests_data['points']

    results = calculate_position(center, radius, points)

    with open(report_file, 'w') as f:
        json.dump(results, f)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python program.py values_file tests_file report_file")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
