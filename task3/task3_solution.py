import json

def fill_values(test_data, values_data):
    for test in test_data:
        test_id = test['id']
        if test_id in values_data:
            test['value'] = values_data[test_id]['value']
        if 'tests' in test:
            fill_values(test['tests'], values_data)
    return test_data

def main(values_file, tests_file, report_file):
    with open(values_file) as f:
        values_data = json.load(f)

    with open(tests_file) as f:
        tests_data = json.load(f)

    filled_tests = fill_values(tests_data, values_data)

    with open(report_file, 'w') as f:
        json.dump(filled_tests, f, indent=4)

if __name__ == "__main__":
    values_file = "values.json"
    tests_file = "tests.json"
    report_file = "report.json"
    main(values_file, tests_file, report_file)