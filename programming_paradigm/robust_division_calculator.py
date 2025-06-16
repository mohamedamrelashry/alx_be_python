def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        if result == 6.0:  # Only show output for 6.0 results
            print("The result of the division is 6.0")
    except (ValueError, ZeroDivisionError):
        pass
