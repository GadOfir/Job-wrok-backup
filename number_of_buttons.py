from exp import main
import re

def number_of_buttons():
    params = [
        ('CLAW', 0, 'false', 'false', 'symmetrical', 9, 20, 3, '3 buttons, leniency set to 0'),
        ('CLAW', 0, 'false', 'false', 'symmetrical', 9, 20, 4, '4 buttons, leniency set to 0'),
        ('CLAW', 0, 'true', 'false', 'asymmetrical', 9, 20, 5, '5 buttons, leniency set to 0 '),
        ('CLAW', 0, 'true', 'false', 'both', 9, 20, 6, '6 buttons, leniency set to 0'),
        ('CLAW', 0, 'true', 'false', 'both', 9, 20, 7, '7 buttons, leniency set to 0'),
        # Add more test cases here as needed
    ]

    for i, param_set in enumerate(params):
        result = main(*param_set[:-1])  # Exclude the description
        description = param_set[-1]  # Extract the description
        for key in result.keys():
            issue_name = result[key].get('Name', f"No name found for test case {i+1}")  # Get the name value
            number_of_buttons = result[key].get('Buttons')  # Use i as the key
            #print(f"Test Case {i+1}: Description: {description}, Name: {issue_name}, Wireless Integrity Result: {wireless_result}")
            pattern = r'Expected Buttons: (\S+) \| Actual Buttons: (\S+)'
            match = re.search(pattern, number_of_buttons)
            expected_buttons = match.group(1)
            actual_buttons = match.group(2)
            if expected_buttons != '-1':
                if expected_buttons != actual_buttons:
                    print(f"Test Case {i + 1}: Description: {description}, Name: {issue_name}, Number of Buttons: {number_of_buttons}")
            else:
                #print(
                #    f"Test Case {i + 1}: Description: {description}, Name: {issue_name}, Number of Buttons: {number_of_buttons}")
                continue


if __name__ == "__main__":
    number_of_buttons()
