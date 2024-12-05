from .token import TokenType
from .lexer import Lexer
from .ast import NumberNode, BinaryOperation, UnaryOperation, VariableNode
class Parser:
    def __init__(self):
        self.lexer = Lexer()
        self.current_token = None
        self.variables = []
    def _consume(self, expected_type):
        if self.current_token.type_ == expected_type:
            self.current_token = self.lexer.next_token()
        else:
            raise SyntaxError(f"Expected {expected_type}, but got {self.current_token.type_}")
    def _parse_factor(self):
        if self.current_token.value in {"+", "-"}:
            token = self.current_token
            self._consume(TokenType.OPERATOR)
            return UnaryOperation(token, self._parse_factor())
        elif self.current_token.type_ == TokenType.NUMBER:
            token = self.current_token
            self._consume(TokenType.NUMBER)
            return NumberNode(token)
        elif self.current_token.type_ == TokenType.ID:
            token = self.current_token
            self._consume(TokenType.ID)
            return VariableNode(token, None)
        elif self.current_token.type_ == TokenType.LPAREN:
            self._consume(TokenType.LPAREN)
            result = self._parse_expression()
            self._consume(TokenType.RPAREN)
            return result
        raise SyntaxError("Invalid token")
    def _parse_term(self):
        result = self._parse_factor()
        while self.current_token and self.current_token.value in {"*", "/"}:
            token = self.current_token
            self._consume(TokenType.OPERATOR)
            result = BinaryOperation(result, token, self._parse_factor())
        return result
    def _parse_expression(self):
        result = self._parse_term()
        while self.current_token and self.current_token.value in {"+", "-"}:
            token = self.current_token
            self._consume(TokenType.OPERATOR)
            result = BinaryOperation(result, token, self._parse_term())
        return result
    def _parse_statement(self):
        if self.current_token.type_ == TokenType.ID:
            token = self.current_token
            self._consume(TokenType.ID)
            self._consume(TokenType.ASSIGN)
            self.variables.append(VariableNode(token, self._parse_expression()))
        elif self.current_token.type_ == TokenType.BEGIN:
            self._consume(TokenType.BEGIN)
            while self.current_token.type_ != TokenType.END:
                self._parse_statement()
                if self.current_token.type_ == TokenType.SEMI:
                    self._consume(TokenType.SEMI)
            self._consume(TokenType.END)
        else:
            raise SyntaxError("Unexpected token")
    def parse(self, input_string):
        self.lexer.init(input_string)
        self.current_token = self.lexer.next_token()
        self._parse_statement()
        self._consume(TokenType.EOL)
        return self.variables
