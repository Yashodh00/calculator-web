def calculate_expression(expression):
    expression = expression.strip()

    operators = ["+", "-", "*", "/"]

    for operator in operators:
        if operator in expression:
            numbers = expression.split(operator)

            if len(numbers) != 2:
                return "Error"

            try:
                first = float(numbers[0])
                second = float(numbers[1])
            except ValueError:
                return "Error"

            if operator == "+":
                return first + second

            elif operator == "-":
                return first - second

            elif operator == "*":
                return first * second

            elif operator == "/":
                if second == 0:
                    return "Error"

                return first / second

    return "Error"