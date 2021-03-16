from sly import Parser
from .swas_lexer import SwasLexer

class SwasParser(Parser):
    tokens = SwasLexer.tokens
    #debugfile = "log.out"
    precedence = (
        ('left', OR, AND), 
        ('left', EQ, LT , GT ,NE, GTE, LTE), 
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),   
        ('left', POW), 
        ('left', MOD),
        ('right', UMINUS),
        ('left', WHILE, DO),
        ('left', IF, ELIF, ELSE),  
        ('left', PRINT, INPUT)
        )

    def __init__(self):
        self.names = { }
        self.prompt = True

    ############################################################
    # MAIN
    ############################################################

    @_('statements')
    def main(self, p):
        return ('main', p.statements)

    @_('statement')
    def statements(self,p):
        return ('statements', [p.statement])

    @_('statements statement')
    def statements(self,p):
        return ('statements', p.statements[1] + [p.statement])


    ############################################################
    # STATEMENTS
    ############################################################

    @_('PRINT statement')
    def statement(self, p):
        return ('print', p.statement)

    @_('INPUT statement')
    def statement(self, p):
        return ('input', p.statement)

    @_('expr')
    def statement(self, p):
        return ('statement-expr', p.expr)

    @_('NAME ARROW statement')
    def statement(self, p):
        return ('assign', p.NAME, p.statement)

    @_('IF expr LBRAC statements RBRAC [ ELIF expr LBRAC statements RBRAC ] [ ELSE LBRAC statements RBRAC ] ')
    def statement(self, p):
        return ('if-elif-else', p.expr0 ,p.statements0, p.expr1, p.statements1, p.statements2)

    @_('WHILE expr DO LBRAC statements RBRAC')
    def statement(self, p):
        return ('while', p.expr, p.statements)

    @_('PASS')
    def statement(self, p):
        return ('pass',)

    @_('BREAK')
    def statement(self, p):
        return ('break',)

    ############################################################
    # Expressions
    ############################################################


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

    @_('expr POW expr')
    def expr(self, p):
        return ('pow', p.expr0, p.expr1)
   
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

    @_('expr AND expr')
    def expr(self, p):
        return ('and', p.expr0, p.expr1)

    @_('expr OR expr')
    def expr(self, p):
        return ('or', p.expr0, p.expr1)


    @_('INC NAME %prec UMINUS')
    def expr(self, p):
        return ('inc', p.NAME)    

    @_('DEC NAME %prec UMINUS')
    def expr(self, p):
        return ('dec', p.NAME)    

    # Weird
    # @_('MINUS expr %prec UMINUS')
    # def expr(self, p):
    #     return ('uminus', p.expr)

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
