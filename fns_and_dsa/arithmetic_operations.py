def perform_operation(num1, num2, operation):
    match operation:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num2 == 0:
                raise ValueError("Cannot divide by zero.")
            result = num1 / num2
        case _:
            raise ValueError("Invalid operation")
    return result
