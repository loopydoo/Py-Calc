import sys

def is_op(string):
    operators = [
        "+",
        "-",
        "*",
        "/"
    ]

    for i in range(len(operators)):
        if operators[i] == string:
            return True
    return False

def tokenize(c):
    contents = list(c)
    tokens = []
    for i in range(len(contents)):
        if contents[i].isdigit():
            tokens.append(contents[i])
        elif is_op(contents[i]):
            tokens.append(contents[i])
        elif contents[i] == " ":
            continue
        elif contents[i] == ".":
            tokens.append(contents[i])
        else:
            sys.exit("That is not a valid Operation")
    return tokens

def parse(tokens):
    buffer = ""
    op_buffer = ""
    new_buffer = ""
    setting = True
    setting2 = True
    setting3 = False
    for i in range(len(tokens)):
        if tokens[i].isdigit():
            if setting == True:
                buffer += tokens[i]
            else:
                new_buffer += tokens[i]
        if setting == True and is_op(tokens[i]):
            op_buffer += tokens[i]
            setting = False
            setting3 = True
            setting2 = False
        if setting2 == True and tokens[i] == ".":
            buffer += tokens[i]
            setting2 == False
        if setting3 == True and tokens[i] == ".":
                new_buffer += tokens[i]
                setting3 == False
    new_tokens = [buffer, op_buffer, new_buffer]
    return new_tokens

def operate(n1, op, n2):
    num1 = 0
    num2 = 0
    if n1.isalpha():
        sys.exit("That is not a valid Operation")
    else:
        num1 += round(float(n1), 3)
    if n2.isalpha():
        sys.exit("That is not a valid Operation")
    else:
        num2 += round(float(n2), 3)
    
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2


def loop():
    contents = input("Please enter an operation: \n")
    if contents == "q":
        sys.exit("Thank you for using this Calculator \n")
    tokens = tokenize(contents)
    new_tok = parse(tokens)
    final = operate(new_tok[0], new_tok[1], new_tok[2])
    print(final)
    loop()

loop()