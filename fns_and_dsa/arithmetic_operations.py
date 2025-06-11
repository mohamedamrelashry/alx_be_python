def perform_operation(num1,num2,operation ):
        match operation:
        case "+":
            result= num1+num2
        case "-":
            result = num1-num2
        case "*":
            result = num1 * num2
        case "/":
            if num2==0:
                result = "Cannot divide by zero."
            else: 
             result = num1/num2
    return resul
