from exp import main
import time


def test_performance():
    params = [
        ('CLAW', 0, 'false', 'false', 'symmetrical', 9, 20, -1),
        ('FINGERTIP', 2, 'false', 'false', 'symmetrical', 9, 20, -1),
        ('CLAW', 3, 'true', 'false', 'both', 9, 20, -1),
        ('PALM', 4, 'true', 'false', 'asymmetrical', 9, 20, -1),
        # Add more test cases here as needed
    ]

    for i, param_set in enumerate(params):
        elapsed_times = []
        for _ in range(3):  # Run each test case three times
            start_time = time.time()
            result = main(*param_set)
            end_time = time.time()
            elapsed_time = end_time - start_time
            elapsed_times.append(elapsed_time)
            print(f"Test Case {i + 1}: Time taken for request {_ + 1}: {elapsed_time:.2f} seconds")

        average_elapsed_time = sum(elapsed_times) / len(elapsed_times)
        print(f"Test Case {i + 1}: Average Time: {average_elapsed_time:.2f} seconds")

        # Calculate percentage difference between times
        percentage_diff = ((max(elapsed_times) - min(elapsed_times)) / min(elapsed_times)) * 100
        print(f"Test Case {i + 1}: Percentage difference between max and min times: {percentage_diff:.2f}%")

        # Print "Bad" if percentage difference is above 70%
        if percentage_diff > 10:
            print(f"Test Case {i + 1}:Bad performance detected")


if __name__ == "__main__":
    test_performance()
