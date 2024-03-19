from main import BaseTest

def main(grip_type, leniency, wireless, lefthanded, shape, h_width, h_length, buttons):
    base_test_instance = BaseTest()
    base_test_instance.setUp()  # Call setUp method to initialize base_url

    # Send a test request with custom parameters
    custom_params = {
        'grip_type': grip_type,
        'leniency': leniency,
        'wireless': wireless,
        'lefthanded': lefthanded,
        'shape': shape,
        'h_width': h_width,
        'h_length': h_length,
        'buttons': buttons#-1
    }

    response_custom = base_test_instance.send_test_request(custom_params)
    search_parameters = response_custom.get('search_parameters', {})

    # Create a dictionary to store mouse details
    mice_details = {}

    # Print search parameters
    # print("Search Parameters:")
    # for key, value in search_parameters.items():
    #     print(f"{key}: {value}")

    # Get the 'mice' list from the response, defaulting to an empty list if not found
    mice_list = response_custom.get('mice', [])

    # Print the number of mice objects
    print("Number of mice objects:", len(mice_list))

    # Iterate over each mouse object and print its details if not empty
    for mouse in mice_list:
        if mouse:
            #print("\nMouse details:")
            expected_leniency = custom_params.get('leniency')
            expected_grip = custom_params.get('grip_type')
            #print(f"Expected Leniency: {expected_leniency}")
            #print(f"Expected Grip: {expected_grip}")
            #print("Name:", mouse['name'])
            expected_wireless = custom_params['wireless']
            #print(f"Expected Wireless: {expected_wireless} | Actual Wireless: {mouse['wireless']}")
            expected_wireless = (f"Expected Wireless: {expected_wireless} | Actual Wireless: {mouse['wireless']}").lower()

            # Assuming mouse['grip_width'] contains the grip width value
            grip_width = mouse['grip_width']
            max_width = search_parameters.get('max_width', float('inf'))  # Default to positive infinity if not specified
            min_width = search_parameters.get('min_width', float('-inf'))  # Default to negative infinity if not specified

            if min_width <= grip_width <= max_width:
                #print(f"Grip width {grip_width} falls within the specified boundaries ({min_width} - {max_width}).")
                grip_width = (f"Grip width {grip_width} falls within the specified boundaries ({min_width} - {max_width}).")
            else:
                #print(f"Grip width {grip_width} falls outside the specified boundaries ({min_width} - {max_width}).")
                grip_width = (f"Grip width {grip_width} falls outside the specified boundaries ({min_width} - {max_width}).")
                # Check length
            length = mouse['length']
            max_length = search_parameters.get('max_length', float('inf'))  # Default to positive infinity if not specified
            min_length = search_parameters.get('min_length', float('-inf'))  # Default to negative infinity if not specified

            if min_length <= length <= max_length:
               # print(f"Length {length} falls within the specified boundaries ({min_length} - {max_length}).")
                length = (f"Length {length} falls within the specified boundaries ({min_length} - {max_length}).")
            else:
              #  print(f"Length {length} falls outside the specified boundaries ({min_length} - {max_length}).")
                length = (f"Length {length} falls outside the specified boundaries ({min_length} - {max_length}).")
            # Compare the number of buttons with expected value from custom_params
            expected_buttons = custom_params['buttons']
            if mouse['buttons'] != expected_buttons:
             #   print(f"Expected Buttons: {expected_buttons} | Actual Buttons: {mouse['buttons']}")
                expected_buttons = (f"Expected Buttons: {expected_buttons} | Actual Buttons: {mouse['buttons']}")
            else:
            #    print(f"Expected Buttons: {expected_buttons} | Actual Buttons: {mouse['buttons']}")
                expected_buttons = (f"Expected Buttons: {expected_buttons} | Actual Buttons: {mouse['buttons']}")

            lefthanded_value = custom_params['lefthanded']
            side_buttons_expected = "both" if lefthanded_value == "true" else "left"
            #print(f"Expected Side Buttons: {side_buttons_expected} | Actual Side Buttons: {mouse['side_buttons']}")
            lefthanded_value = (f"Expected Side Buttons: {side_buttons_expected} | Actual Side Buttons: {mouse['side_buttons']}")

            # Compare the shape with expected value from custom_params
            expected_shape = custom_params['shape']
            if expected_shape.lower() != "both" and mouse['shape'].lower() != expected_shape.lower():
            #    print(f"Expected Shape: {expected_shape} | Actual Shape: {mouse['shape']}")
                expected_shape=(f"Expected Shape: {expected_shape} | Actual Shape: {mouse['shape']}")
            else:
            #    print(f"Expected Shape: {expected_shape} | Actual Shape: {mouse['shape']}")
                expected_shape = (f"Expected Shape: {expected_shape} | Actual Shape: {mouse['shape']}")

            # Storing details in the mice_details dictionary
            mouse_name = mouse['name']
            mice_details[mouse_name] = {
                'Leniency': expected_leniency,
                'Grip': expected_grip,
                'Name': mouse_name,
                'Wireless': expected_wireless,
                'Grip Width': grip_width,
                'Length': length,
                'Buttons': expected_buttons,
                'Side Buttons': lefthanded_value,
                'Shape': expected_shape

            }
    return mice_details
    # Now you have all the mouse details in the mice_details dictionary
    # You can further process or use this data as per your requirement

if __name__ == '__main__':
    main()
