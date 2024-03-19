from exp import main
import re

def test_wireless_integrity():
    params = [
        ('CLAW', 0, 'false', 'false', 'both', 9, 20, -1, 'Wireless false, low leniency'),
        ('CLAW-PALM', 0, 'true', 'false', 'both', 9, 20, -1, 'Wireless true, low leniency'),
        ('PALM', 4, 'false', 'false', 'both', 9, 20, -1, 'Wireless false, high leniency'),
        ('FINGERTIP', 4, 'true', 'false', 'both', 9, 20, -1, 'Wireless true , high leniency'),
        # Add more test cases here as needed
    ]

    for i, param_set in enumerate(params):
        result = main(*param_set[:-1])  # Exclude the description
        description = param_set[-1]  # Extract the description
        for key in result.keys():
            issue_name = result[key].get('Name', f"No name found for test case {i+1}")  # Get the name value
            wireless_result = result[key].get('Wireless')  # Use i as the key
            #print(f"Test Case {i+1}: Description: {description}, Name: {issue_name}, Wireless Integrity Result: {wireless_result}")
            pattern = r'expected wireless: (\w+) \| actual wireless: (\w+)'
            match = re.search(pattern, wireless_result)
            if match:
                expected_wireless = match.group(1)
                actual_wireless = match.group(2)
                if match.group(1) != match.group(2):
                    print(f"Test Case {i+1}: Description: {description},Issue With Name: {issue_name}, Wireless Integrity Result: {wireless_result}")
            else:
                print("No match found")



if __name__ == "__main__":
    test_wireless_integrity()

