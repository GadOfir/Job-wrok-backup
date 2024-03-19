from exp import main
import re



def left_handed():
    params = [
        ('CLAW', 0, 'false', 'false', 'both', 9, 20, -1, 'left_handed false leniency 0'),
        ('PALM', 4, 'true', 'false', 'both', 9, 20, -1, 'left_handed false leniency 4'),
        ('FINGERTIP', 0, 'false', 'true', 'both', 9, 20, -1, 'left_handed true leniency 0'),
        ('CLAW', 4, 'true', 'false', 'both', 9, 20, -1, 'left_handed true leniency 0'),
    ]
        # Add more test cases here as needed
    for i, param_set in enumerate(params):
        result = main(*param_set[:-1])  # Exclude the description
        description = param_set[-1]  # Extract the description
        for key in result.keys():
            issue_name = result[key].get('Name', f"No name found for test case {i+1}")  # Get the name value
            left_handed= result[key].get('Side Buttons')
            pattern = r'Expected Side Buttons: (\w+) \| Actual Side Buttons: (\w+)'
            match = re.search(pattern, left_handed)
            expected_left_handed = match.group(1)
            actual_left_handed = match.group(2)
            #print(f"Name: {issue_name}, Left Handed: {left_handed}")
            if expected_left_handed != actual_left_handed:
                if actual_left_handed != 'both':
                    print(f"Test Case {i + 1}: Description: {description}, Name: {issue_name}, Left Handed: {left_handed}")
            else:
                continue


            print('--------------------------')





if __name__ == "__main__":

    left_handed()