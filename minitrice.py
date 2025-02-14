import sys
import re

def minitrice(expression):
    # Validate and parse the expression
    match = re.match(r'^\s*(\d+)\s*([\+\-\*/])\s*(\d+)\s*$', expression)
    if not match:
        return "Erreur de syntaxe pour le calcul: {}".format(expression), 1

    num1, operator, num2 = match.groups()
    num1 = int(num1)
    num2 = int(num2)

    # Perform the calculation based on the operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Division par zéro", 1
        result = num1 / num2
    else:
        return "Erreur de syntaxe pour le calcul: {}".format(expression), 1

    return round(result, 2), 0

def main():
    if sys.stdin.isatty():
        # Interactive mode
        while True:
            try:
                expression = input("> ")
                if expression == "":
                    break
                result, code = minitrice(expression)
                print(result)
            except EOFError:
                print("Fin des calculs :)")
                sys.exit(0)
    else:
        # Reading from stdin
        for line in sys.stdin:
            result, code = minitrice(line.strip())
            print(result)
        sys.exit(code)

if __name__ == "__main__":
    main()