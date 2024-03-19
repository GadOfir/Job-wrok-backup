from exp import main
import time


def WithServerError():
    params = [
        ('CLAW', 0, 'false', 'false', 'symmetrical', 9, 20, 'XX'),
        ('FINGERTIP', 'xx', 'false', 'false', 'symmetrical', 9, 20, -1),
        ('CLAW', 3, 'true', 'false', 'both', 'xx', 20, -1),
        ('PALM', 4, 'true', 'false', 'asymmetrical', 9, 20, -1),
        # Add more test cases here as needed
    ]

    for i, param_set in enumerate(params):
       try:
        result = main(*param_set)
       except(Exception) as e:
        print("Internal Error Server machine broke! Please check back later")


if __name__ == "__main__":
    WithServerError()
