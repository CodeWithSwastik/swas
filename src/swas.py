from sys import argv
from swas_lexer import SwasLexer
from swas_parser import SwasParser

def main():
    
    if len(argv) <= 1:
        shell()
    else:
        fp = argv[1]
        execute(fp)


def evaluate(tree):
    global names
    try:
        rule = tree[0]
    except:
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
    elif rule == 'equals':
        return int(evaluate(tree[1]) == evaluate(tree[2]))

    elif rule == 'uminus':
        return -evaluate(tree[1])
    elif rule == 'inc':
        name = tree[1]
        oldval = names[tree[1]]
        newval = oldval + 1
        
        names[name] = newval
        return newval
    elif rule == 'dec':
        name = tree[1]
        oldval = names[tree[1]]
        newval = oldval - 1
        
        names[name] = newval
        return newval
    elif rule == 'number':
        return int(tree[1])
    elif rule == 'string':
        return str(tree[1])
    elif rule == 'name':
        return names[tree[1]]
    elif rule == 'paren':
        return evaluate(tree[1])
    elif rule == 'print':
        value = evaluate(tree[1])
        print(value)
        return value
    elif rule == 'if-then':
        value = evaluate(tree[1])
        if value:
            return evaluate(tree[2])
        else:
            return 0
    elif rule == 'if-else':
        value = evaluate(tree[1])
        if value:
            return evaluate(tree[2])
        else:
            return evaluate(tree[3])
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
    while True:
        try:
            text = input('swas > ')
        except EOFError:
            break
        tree = parser.parse(lexer.tokenize(text))
        evaluate(tree)

if __name__ == '__main__':
    names = {}
    main()
