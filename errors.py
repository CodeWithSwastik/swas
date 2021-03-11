class BaseError:
    def __init__(self, error_name, details):

        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result  = f'{self.error_name}: {self.details}\n'
        return result

class SyntaxError(BaseError):
    def __init__(self, details):
        super().__init__('Syntax Error', details)

class IllegalCharError(BaseError):
    def __init__(self, details):
        super().__init__('Illegal Character', details)

