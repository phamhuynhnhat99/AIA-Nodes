import os

from ..NENV import init_node_env

def run():
    os.environ['AIA_MODE'] = 'no-gui'
    init_node_env()
    print("Good luck Have fun.")


if __name__ == '__main__':
    run()