def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    return result
print(safe_divide(10,2))
print(safe_divide(10,0))
