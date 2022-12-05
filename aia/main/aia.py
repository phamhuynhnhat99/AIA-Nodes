import os

from aia.NENV import init_node_env, import_widgets

utils = import_widgets(__file__, "utils.py")


def run():
    os.environ['AIA_MODE'] = 'no-gui'
    init_node_env()

    coordinator = utils.Coordinator()
    coordinator.auto_loading()
    
    """ Infinity Loop """
    while True:
        # os.system('clear')
        print("----------------------------------------")
        coordinator.display_no_gui_nodes()
        print("----------------------------------------")
        print("-oOo-       Registered Nodes       -oOo-")
        coordinator.display_registered_nodes()
        print("----------------------------------------")
        print("-oOo-     Registered Directions    -oOo-")
        coordinator.display_arrows()
        print("----------------------------------------")
        print("-oOo-           Toposort           -oOo-")
        coordinator.display_order()
        print("----------------------------------------")
        print("❤️ ❤️ ❤️ ❤️ ❤️  Welcome to my world ❤️ ❤️ ❤️ ❤️ ❤️")
        print("0: Exit Program")
        print("1: Registering a new node")
        print("2: Registering a direction")
        print("3: Updating a node")
        print("4: Removing a registered node")
        print("5: Removing a registered arrow")
        choice = input("You choice is: ")
        print("----------------------------------------")
        if choice == "1":
            try:
                ind = int(input("New node's index is: "))
            except:
                ind = -1 # out of list range
            coordinator.registering_a_new_node(ind)

        elif choice == "2":
            arrow = input("Enter an arrow: ").split(" ")
            try:
                u = int(arrow[0])
                v = int(arrow[1])
                ind = int(arrow[2])
            except:
                u, v, ind = -1, -1, -1 # out of list range
            coordinator.registering_a_new_arrow(u, v, ind)

        elif choice == "3":
            try:
                gid = int(input("Node's Global ID is: "))
            except:
                gid = -1
            coordinator.updating_a_registered_node(gid)
        
        elif choice == "4":
            try:
                gid = int(input("Node's Global ID is: "))
            except:
                gid = -1
            coordinator.removing_a_registered_node(gid)

        elif choice == "5":
            arrow = input("Enter an arrow: ").split(" ")
            try:
                u = int(arrow[0])
                v = int(arrow[1])
            except:
                u, v = -1, -1
            coordinator.removing_a_registered_arrow(u, v)

        else:
            break

    print("----------------------------------------")
    print("Good luck Have fun.")


if __name__ == '__main__':
    run()