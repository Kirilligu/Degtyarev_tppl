from .ast import NumberNode, BinaryOperation, UnaryOperation, VariableNode
from .my_parser import Parser
class Interpreter:
    def __init__(self):
        self._parser = Parser()
        self._vars = {}
    def visit(self, node):
        if isinstance(node, NumberNode):
            return float(node.token.value)
        if isinstance(node, BinaryOperation):
            left = self.visit(node.left)
            right = self.visit(node.right)
            op = node.operator.value
            if op == "+":
                return left + right
            elif op == "-":
                return left - right
            elif op == "*":
                return left * right
            elif op == "/":
                if right == 0:
                    return 0
                return left / right
        if isinstance(node, UnaryOperation):
            value = self.visit(node.expression)
            return value if node.operator.value == "+" else -value
        if isinstance(node, VariableNode):
            if node.name.value in self._vars:
                return self._vars[node.name.value]
            return 0
        return 0
    def eval(self, code: str) -> dict:
        trees = self._parser.parse(code)
        self._vars = {}
        for tree in trees:
            self._vars[tree.name.value] = self.visit(tree.expression)
        return self._vars
