def safe_divide(float(numerator), float(denominator)):
   try:
       result = numerator /denominator 
       print(f"The result of the division is {result:.2f}")
   except TypeError: 
       print("Error: Please enter numeric values only.")
   except ZeroDivisionError : 
       print("Error: Cannot divide by zero.") 
