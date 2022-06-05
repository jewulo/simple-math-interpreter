# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# https://www.youtube.com/playlist?list=PLZQftyCk7_Sdu5BFaXB_jLeJ9C78si5_3
# PART 1 - https://www.youtube.com/watch?v=88lmIMHhYNs
# PART 2 - https://www.youtube.com/watch?v=TwKWUj033vY
# PART 3 - https://www.youtube.com/watch?v=45epnUwFALo
# PART 4 - https://www.youtube.com/watch?v=tczjDCbykyM

# GitHub https://github.com/davidcallanan/py-simple-math-interpreter

from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        try:
            text = input("calc > ")
            lexer = Lexer(text)
            tokens = lexer.generate_tokens()
            print(list(tokens))

            parser = Parser(tokens)
            tree = parser.parse()
            print(tree)

            if not tree:
                print("empty tree")
                continue

            interpreter = Interpreter()
            result = interpreter.visit(tree)
            print(result.value)
        except Exception as e:
            print(e)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
