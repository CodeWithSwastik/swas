from sly import Parser
from .swas_lexer import SwasLexer

class SwasParser(Parser):
    tokens = SwasLexer.tokens
    #debugfile = "log.out"
    precedence = (
        ('left', EQ, LT , GT ,NE, GTE, LTE), 
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),      
        ('left', MOD),
        ('right', UMINUS),
        ('left', WHILE, DO),
        ('left', JOIN),
        ('left', IF, ARROW,ELSE),        
        ('left', PRINT, INPUT)
        )

    def __init__(self):
        self.names = { }
        self.prompt = True



    @_('PRINT statement')
    def statement(self, p):
        return ('print', p.statement)

    @_('INPUT statement')
    def statement(self, p):
        return ('input', p.statement)

    @_('statement JOIN statement')
    def statement(self, p):
        return ('join-statement', p.statement0, p.statement1) 

    @_('expr')
    def statement(self, p):
        return ('statement-expr', p.expr)

    @_('NAME ARROW statement')
    def statement(self, p):
        return ('assign', p.NAME, p.statement)

    @_('IF expr ARROW LBRAC statement RBRAC ELSE ARROW LBRAC statement RBRAC')
    def statement(self, p):
        return ('if-else', p.expr,p.statement0, p.statement1)

    @_('WHILE expr DO LBRAC statement RBRAC')
    def statement(self, p):
        return ('while', p.expr, p.statement)

    @_('PASS')
    def statement(self, p):
        return ('pass')

    @_('expr PLUS expr')
    def expr(self, p):
        return ('plus', p.expr0, p.expr1)

    @_('expr MINUS expr')
    def expr(self, p):
        return ('minus', p.expr0, p.expr1)

    @_('expr TIMES expr')
    def expr(self, p):
        return ('times', p.expr0, p.expr1)

    @_('expr DIVIDE expr')
    def expr(self, p):
        return ('divide', p.expr0, p.expr1)

    @_('expr MOD expr')
    def expr(self, p):
        return ('mod', p.expr0, p.expr1)

    @_('expr EQ expr')
    def expr(self, p):
        return ('equals', p.expr0, p.expr1)

    @_('expr NE expr')
    def expr(self, p):
        return ('ne', p.expr0, p.expr1)

    @_('expr GT expr')
    def expr(self, p):
        return ('gt', p.expr0, p.expr1)

    @_('expr GTE expr')
    def expr(self, p):
        return ('gte', p.expr0, p.expr1)

    @_('expr LT expr')
    def expr(self, p):
        return ('lt', p.expr0, p.expr1)

    @_('expr LTE expr')
    def expr(self, p):
        return ('lte', p.expr0, p.expr1)


    @_('INC NAME %prec UMINUS')
    def expr(self, p):
        return ('inc', p.NAME)    

    @_('DEC NAME %prec UMINUS')
    def expr(self, p):
        return ('dec', p.NAME)    

    @_('MINUS expr %prec UMINUS')
    def expr(self, p):
        return ('uminus', p.expr)

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return ('paren', p.expr)

    @_('NUMBER')
    def expr(self, p):
        return ('number', p.NUMBER)

    @_('STRING')
    def expr(self, p):
        return ('string', p.STRING)

    @_('NAME')
    def expr(self, p):
        return ('name', p.NAME)
