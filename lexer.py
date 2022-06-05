from tokens import Token, TokenType

WHITESPACE = ' \n\t'
DIGITS = '0123456789'


class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.current_char = None
        self.advanced()

    def advanced(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char is not None:
            if self.current_char in WHITESPACE:
                self.advanced()
            elif self.current_char == '.' or self.current_char in DIGITS:
                yield self.generate_number()
            elif self.current_char == '+':
                self.advanced()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advanced()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*':
                self.advanced()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advanced()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '(':
                self.advanced()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.advanced()
                yield Token(TokenType.RPAREN)
            else:
                raise Exception(f"Illegal Character '{self.current_char}'")

    def generate_number(self):
        decimal_point_count = 0
        number_str = self.current_char
        self.advanced()

        while self.current_char is not None and (self.current_char == '.' or self.current_char in DIGITS):
            if self.current_char == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break

            number_str += self.current_char
            self.advanced()

        if number_str.startswith('.'):
            number_str = '0' + number_str
        if number_str.endswith('.'):
            number_str += '0'

        return Token(TokenType.NUMBER, float(number_str))


