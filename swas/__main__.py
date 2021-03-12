from sys import argv
from .executor import execute, shell

def main():
    
    if len(argv) <= 1:
        shell()
    else:
        fp = argv[1]
        execute(fp)

if __name__ == '__main__':
    main()
