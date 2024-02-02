#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (ZeroDivisionError):
        result = None
    finally:
        if result is not None:
            print("Inside result: {:.2f}".format(result))
        else:
            print("Inside result: None")
            return None
        return result
