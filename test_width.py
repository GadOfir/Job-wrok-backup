from exp import main
import re


def test_width():
    params = [
        ('CLAW', 0, 'false', 'false', 'both', 9, 20, 5, 'set width 9 leniency set to 0'),
        ('CLAW', 1, 'false', 'false', 'both', 11, 20, 5, 'set width 11 leniency set to '),
        ('CLAW', 4, 'false', 'false', 'both', 12, 20, 5, 'set width 12 leniency set to'),

        # Add more test cases here as needed
    ]
    for i, param_set in enumerate(params):
        result = main(*param_set[:-1])  # Exclude the description
        description = param_set[-1]  # Extract the description
        for key in result.keys():
            issue_name = result[key].get('Name', f"No name found for test case {i+1}")  # Get the name value
            grip_width = result[key].get('Grip Width')  # Extract grip_width instead of wireless_result

            print(f"Test Case {i+1}: Description: {description}, Name: {issue_name}, Grip Width: {grip_width}")

if __name__ == "__main__":

    test_width()

