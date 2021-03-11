import sys 
import shell

def execute(fp):
    with open(fp, "r") as f:
        data = f.read()
    shell.execute(data)

def main():
    if len(sys.argv) <= 1:
        shell.run()
    else:
        fp = sys.argv[1]
        execute(fp)
main()