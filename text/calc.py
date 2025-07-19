import ast
import math


def my_eval(expression):
    tree = ast.parse(expression, mode='eval')
    #dump(tree)
    validate_ast(tree)
    code = compile(tree, filename='', mode='eval')
    context = {
        '__builtins__': {},
        'sin': math.sin,
        'cos': math.cos
    }
    return eval(code, context)


_allowed_nodes = (
    # базовые узлы:
    ast.BinOp, ast.UnaryOp, ast.Constant, ast.Call, ast.Name, ast.Load,

    # основные BinOps:
    ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod, ast.Pow,

    # основные UnaryOps:
    ast.UAdd, ast.USub
)

def validate_ast(tree):

    # валидируем корень дерева
    if not isinstance(tree, ast.Expression):
        raise Exception('Неправильное выражение')

    # валидируем узлы
    def validate_children(node):
        for child in ast.iter_child_nodes(node):
            if isinstance(child, list):
                for grandchild in child:
                    validate_children(grandchild)
            else:
                if not isinstance(child, _allowed_nodes):
                    raise Exception('Неправильное выражение')
                validate_children(child)

    validate_children(tree)


def dump(node):
    def _format(node, indent):
        if isinstance(node, ast.AST):
            print('%sAST %s' % (' ' * indent, node.__class__.__name__))
            for a, b in ast.iter_fields(node):
                print('%s%s' % (' ' * indent, a))
                _format(b, indent + 4)
        elif isinstance(node, list):
            print('%sLIST %s' % (' ' * indent, node.__class__.__name__))
            for x in node:
                _format(x, indent)
        else:
            print('%s%s' % (' ' * indent, repr(node)))
    _format(node, 0)


print(my_eval(input()))