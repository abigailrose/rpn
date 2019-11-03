import readline
import operator
from termcolor import colored

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}

def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)


        #print(stack)
    if len(stack) != 1:
        raise TypeError('malformed input')
    return stack.pop()


def hello_world():
    print("hello world")


def main():
    while True:
        result = calculate(input("rpn calc> "))
        
        if result < 0:
            print(colored(result, 'red'))
        else:
            print(colored(result, 'cyan'))

if __name__ == '__main__':
    main()
