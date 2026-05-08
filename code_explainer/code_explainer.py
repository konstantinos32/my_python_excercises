import ast

class CodeExplainer(ast.NodeVisitor):
    def visit_Assign(self, node):
        target = self.visit(node.targets[0])
        value = self.visit(node.value)
        print(f"Set {target} to {value}")

    def visit_Name(self, node):
        return node.id

    def visit_Constant(self, node):
        return repr(node.value)

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        op = self.get_operator(node.op)
        return f"{left} {op} {right}"

    def visit_Compare(self, node):
        left = self.visit(node.left)
        right = self.visit(node.comparators[0])
        op = self.get_operator(node.ops[0])
        return f"{left} {op} {right}"

    def visit_If(self, node):
        condition = self.visit(node.test)
        print(f"Check if {condition}")
        print("If true:")
        for stmt in node.body:
            self.visit(stmt)

    def visit_Return(self, node):
        value = self.visit(node.value)
        print(f"Return {value}")

    def get_operator(self, op):
        if isinstance(op, ast.Add):
            return "plus"
        if isinstance(op, ast.Sub):
            return "minus"
        if isinstance(op, ast.Mult):
            return "multiplied by"
        if isinstance(op, ast.Div):
            return "divided by"
        if isinstance(op, ast.Eq):
            return "equals"
        if isinstance(op, ast.NotEq):
            return "does not equal"
        if isinstance(op, ast.Lt):
            return "is less than"
        if isinstance(op, ast.Gt):
            return "is greater than"
        return "unknown operator"


code = """
def end_destination(paths):
    start_cities = set()
    end_cities = set()

    for path in paths:
        start_cities.add(path[0])
        end_cities.add(path[1])
        

    for city in end_cities:
        if city not in start_cities:
            return city

    return None
print(end_destination(paths))  # Output: "Sao Paulo"
print(end_destination([["A","E"],["B","C"],["C","d"]]))
"""

tree = ast.parse(code)
explainer = CodeExplainer()
explainer.visit(tree)