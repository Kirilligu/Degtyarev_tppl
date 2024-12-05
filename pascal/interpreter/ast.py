class ASTNode:
    pass
class NumberNode(ASTNode):
    def __init__(self, token):
        self.token = token
    def __str__(self):
        return f"Number({self.token})"
class BinaryOperation(ASTNode):
    def __init__(self, left, operator, right):
        self.left, self.operator, self.right = left, operator, right
    def __str__(self):
        return f"BinaryOperation({self.operator.value}, {self.left}, {self.right})"
class UnaryOperation(ASTNode):
    def __init__(self, operator, expression):
        self.operator, self.expression = operator, expression
    def __str__(self):
        return f"UnaryOperation({self.operator.value}, {self.expression})"
class VariableNode(ASTNode):
    def __init__(self, name, expression):
        self.name, self.expression = name, expression
    def __str__(self):
        return f"Variable({self.name.value} = {self.expression})"

