from .token import Token, TokenType
class Lexer():
    def __init__(self):
        self.position = 0
        self.text = ""
        self.current_char = None
    def init(self, input_text: str):
        self.position = 0
        self.text = input_text
        self.current_char = self.text[self.position] if self.text else None
    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()
    def advance(self):
        self.position += 1
        if self.position >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.position]
    def read_number(self):
        number = ""
        while self.current_char and (self.current_char.isdigit() or self.current_char == "."):
            number += self.current_char
            self.advance()
        return number
    def read_identifier(self):
        identifier = ""
        while self.current_char and self.current_char.isalpha():
            identifier += self.current_char
            self.advance()
        if identifier == "BEGIN":
            return Token(TokenType.BEGIN, '')
        elif identifier == "END":
            return Token(TokenType.END, '')
        else:
            return Token(TokenType.ID, identifier)
    def read_assign(self):
        self.advance()
        return Token(TokenType.ASSIGN, ":=")
    def next_token(self) -> Token:
        while self.current_char:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            elif self.current_char.isdigit():
                return Token(TokenType.NUMBER, self.read_number())
            elif self.current_char in "+-*/":
                operator = self.current_char
                self.advance()
                return Token(TokenType.OPERATOR, operator)
            elif self.current_char == "(":
                self.advance()
                return Token(TokenType.LPAREN, "(")
            elif self.current_char == ")":
                self.advance()
                return Token(TokenType.RPAREN, ")")
            elif self.current_char.isalpha():
                return self.read_identifier()
            elif self.current_char == ";":
                self.advance()
                return Token(TokenType.SEMI, ";")
            elif self.current_char == ":":
                return self.read_assign()
            elif self.current_char == ".":
                self.advance()
                return Token(TokenType.EOL, "")
            else:
                self.advance()
        return Token(TokenType.EOL, "")
