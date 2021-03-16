from .swas_lexer import SwasLexer
from .swas_parser import SwasParser

VERSION = "1.7"

names = {}
def evaluate(tree):
    global names
    try:
        rule = tree[0]
    except TypeError:
        return print("Swas says: Error Above ^^^^^^")

    if rule == "join-statement":
        evaluate(tree[1])
        evaluate(tree[2])
    elif rule == 'statement-expr':
        value = evaluate(tree[1])
        return value
    elif rule == 'assign':
        value = evaluate(tree[2])
        name = tree[1]
        names[name] = value
        return value

    elif rule == 'times':
        return evaluate(tree[1]) * evaluate(tree[2])
    elif rule == 'plus':
        return evaluate(tree[1]) + evaluate(tree[2])
    elif rule == 'minus':
        return evaluate(tree[1]) - evaluate(tree[2])
    elif rule == 'divide':
        return evaluate(tree[1]) / evaluate(tree[2])
    elif rule == 'mod':
        return evaluate(tree[1]) % evaluate(tree[2])
    elif rule == 'pow':
        return evaluate(tree[1]) ** evaluate(tree[2])
            
    elif rule == 'equals':
        return int(evaluate(tree[1]) == evaluate(tree[2]))
    elif rule == 'ne':
        return int(evaluate(tree[1]) != evaluate(tree[2]))
    elif rule == 'gt':
        return int(evaluate(tree[1]) > evaluate(tree[2]))
    elif rule == 'gte':
        return int(evaluate(tree[1]) >= evaluate(tree[2]))
    elif rule == 'lt':
        return int(evaluate(tree[1]) < evaluate(tree[2]))
    elif rule == 'lte':
        return int(evaluate(tree[1]) <= evaluate(tree[2]))
    elif rule == 'and':
        return int(evaluate(tree[1]) and evaluate(tree[2]))
    elif rule == 'or':
        return int(evaluate(tree[1]) or evaluate(tree[2]))


    elif rule == 'uminus':
        return -evaluate(tree[1])
    elif rule == 'inc':
        name = tree[1]

        try:        
            oldval = names[tree[1]]
        except KeyError:
            return print(f"Swas says: {name} hasn't been defined!")        
        newval = oldval + 1
        
        names[name] = newval
        return newval
    elif rule == 'dec':
        name = tree[1]
        try:        
            oldval = names[tree[1]]
        except KeyError:
            return print(f"Swas says: {name} hasn't been defined!") 

        newval = oldval - 1
        
        names[name] = newval
        return newval
    elif rule == 'number':
        try:
            return int(tree[1])
        except ValueError:
            return float(tree[1])
    elif rule == 'string':
        return str(tree[1])
    elif rule == 'name':
        varname = tree[1]
        try:
            return names[varname]
        except KeyError:
            print(f"Swas says: {varname} hasn't been defined!")
    elif rule == 'paren':
        return evaluate(tree[1])
    elif rule == 'pass':
        pass
    elif rule == 'print':
        value = evaluate(tree[1])
        print(value)
        return value
    elif rule == 'input':
        value = evaluate(tree[1])
        res = input(value)
        try:
            res = float(res)
        except ValueError:
            pass
        return res
    elif rule == 'if-elif-else':
        expr1 = evaluate(tree[1])
        expr2 = None if tree[3] is None else evaluate(tree[3])
        if expr1:
            return evaluate(tree[2])
        elif expr2:
            return evaluate(tree[4])
        else:
            if tree[5]:
                return evaluate(tree[5])
            else:
                pass
    elif rule == 'while':
        while evaluate(tree[1]):
            evaluate(tree[2])

def execute(fp):
    with open(fp, "r") as f:
        text = f.read()

    lexer = SwasLexer()
    parser = SwasParser()
    tree = parser.parse(lexer.tokenize(text))
    evaluate(tree)

def shell():
    lexer = SwasLexer()
    parser = SwasParser()
    print(f"Swas {VERSION}")
    while True:
        try:
            text = input('swas > ')
        except EOFError:
            break
        tree = parser.parse(lexer.tokenize(text))
        evaluate(tree)

