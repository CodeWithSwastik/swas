from .swas_lexer import SwasLexer
from .swas_parser import SwasParser

VERSION = "1.8.3"

names = {}

def get_obj_type(_obj):
    return str(type(_obj)).split("'")[1]

def evaluate(tree):
    global names
    undefined = "Swas says: {0} hasn't been defined!"
    type_error = "Swas says: You can't use '{op}' with types '{obj1}' and '{obj2}'!"
    single_te = "Swas says: You can't use '{op}' with type '{obj}'!"

    try:
        rule = tree[0]
    except TypeError:
        return print("Swas says: Error!!")

    if rule == 'main':
        evaluate(tree[1])
    elif rule == 'statements':
        results = []
        for i in tree[1]:
            results.append(evaluate(i))
        return results
    elif rule == 'statement-expr':
        value = evaluate(tree[1])
        return value
    elif rule == 'assign':
        value = evaluate(tree[2])
        name = tree[1]
        names[name] = value
        return value

    elif rule == 'times':
        multiplier = evaluate(tree[1])
        multiplicand = evaluate(tree[2])
        try:
            return multiplier * multiplicand
        except TypeError:
            return print(type_error.format(op="*", obj1=get_obj_type(multiplier), obj2=get_obj_type(multiplicand)))
    elif rule == 'plus':
        addend1 = evaluate(tree[1])
        addend2 = evaluate(tree[2])
        try:
            return addend1 + addend2
        except TypeError:
            return print(type_error.format(op="+", obj1=get_obj_type(addend1), obj2=get_obj_type(addend2)))
    elif rule == 'minus':
        minuend = evaluate(tree[1])
        subtrahend = evaluate(tree[2])
        try:
            return minuend - subtrahend
        except TypeError:
            return print(type_error.format(op="-", obj1=get_obj_type(minuend), obj2=get_obj_type(subtrahend)))
    elif rule == 'divide':
        dividend = evaluate(tree[1])
        divisor = evaluate(tree[2])
        try:
            return dividend / divisor
        except TypeError:
            return print(type_error.format(op="/", obj1=get_obj_type(dividend), obj2=get_obj_type(divisor)))
    elif rule == 'mod':
        a = evaluate(tree[1])
        n = evaluate(tree[2])
        try:
            return a % n
        except TypeError:
            return print(type_error.format(op="%", obj1=get_obj_type(a), obj2=get_obj_type(n)))
    elif rule == 'pow':
        target_num = evaluate(tree[1])
        exponent = evaluate(tree[2])
        try:
            return target_num ** exponent
        except TypeError:
            return print(type_error.format(op="^", obj1=get_obj_type(target_num), obj2=get_obj_type(exponent)))
    
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
            return print(undefined.format(varname)) 

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
    elif rule == 'list':
        #print(tree)
        results = []
        for i in tree[1][1]:
            results.append(evaluate(i))
        return results
    elif rule == 'name':
        varname = tree[1]
        try:
            return names[varname]
        except KeyError:
            print(undefined.format(varname))
    elif rule == 'index':
        op = evaluate(tree[1])
        index = evaluate(tree[2])
        try:
            return op[index]
        except IndexError as e:
            print(f'Swas says: {e}')
        except TypeError as e:
            print(f'Says says: Only lists and strings can be indexed')
    elif rule == 'paren':
        return evaluate(tree[1])
    elif rule == 'pass':
        pass
    elif rule == 'break':
        return Break()
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
            results = evaluate(tree[2])
            
            if any([isinstance(res,Break) for res in results]):
                break
    else:
        #print(rule, tree)
        pass
class Break:
    pass

def execute(text):
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

