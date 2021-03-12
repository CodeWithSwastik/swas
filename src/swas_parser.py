from sly import Parser
from swas_lexer import SwasLexer

class SwasParser(Parser):
    tokens = SwasLexer.tokens
    #debugfile = "log.out"
    precedence = (
        ('left', EQUALS), 
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),      
        ('left', MOD),
        ('right', UMINUS),
        ('left', WHILE, DO),
        ('left', JOIN),
        ('left', IF, ARROW,ELSE),        
        ('left', PRINT)
        )

    def __init__(self):
        self.names = { }
        self.prompt = True


    @_('statement JOIN statement')
    def statement(self, p):
        return ('join-statement', p.statement0, p.statement1) 

    @_('expr')
    def statement(self, p):
        return ('statement-expr', p.expr)

    @_('PRINT statement')
    def statement(self, p):
        return ('print', p.statement)


    @_('NAME ARROW expr')
    def statement(self, p):
        return ('assign', p.NAME, p.expr)

    @_('IF expr ARROW statement ELSE ARROW statement')
    def statement(self, p):
        return ('if-else', p.expr,p.statement0, p.statement1)


    @_('WHILE expr DO statement')
    def statement(self, p):
        return ('while', p.expr, p.statement)


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

    @_('expr EQUALS expr')
    def expr(self, p):
        return ('equals', p.expr0, p.expr1)

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
