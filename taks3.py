import json
import sys

def read_json_file(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def write_json_file(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def process_reports(values_data, tests_data):
    # Prepare a dictionary from values.json
    value_dict = {item['id']: item['value'] for item in values_data}

    # Initialize report structure based on tests.json
    report_data = tests_data.copy()

    # Fill in 'value' field based on value_dict
    for test in report_data['tests']:
        test_id = test['id']
        if test_id in value_dict:
            test['value'] = value_dict[test_id]

    return report_data

def main():
    if len(sys.argv) != 4:
        print("Usage: python program.py values.json tests.json report.json")
        return

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    # Read data from files
    values_data = read_json_file(values_file)
    tests_data = read_json_file(tests_file)

    # Process data to create report
    report_data = process_reports(values_data, tests_data)

    # Write report data to report.json
    write_json_file(report_data, report_file)
    print(f"Report generated successfully in {report_file}")

if __name__ == "__main__":
    main()
