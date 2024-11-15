from add import add
import os

def main():
    print("Process id: ", os.getpid())
    add(1, 2)

if __name__ == '__main__':
    main()