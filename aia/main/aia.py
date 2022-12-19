import os

from aia.NENV import init_node_env, import_widgets

utils = import_widgets(__file__, "utils.py")


def run():

    init_node_env()

    coordinator = utils.Coordinator()
    coordinator.auto_loading()
    
    """ Infinity Loop """
    while True:
        os.system('clear')
        print("-oOo-             -oOo-             -oOo-")
        print("TITLE:", coordinator.title)
        print("VERSION:", coordinator.version)
        print("-----------------------------------------")
        coordinator.display_no_gui_nodes()
        print("-----------------------------------------")
        print("-oOo-       Registered Nodes        -oOo-")
        coordinator.display_registered_nodes()
        print("-----------------------------------------")
        print("-oOo-     Registered Directions     -oOo-")
        coordinator.display_arrows()
        print("-----------------------------------------")
        print("-oOo-           Toposort            -oOo-")
        coordinator.display_order()
        print("-----------------------------------------")
        print("❤️ ❤️ ❤️ ❤️ ❤️  Welcome to my world ❤️ ❤️ ❤️ ❤️ ❤️")
        print("save: Saving this project")
        print("load: Loading a json file")
        print("0: Exit Program")
        print("1: Registering a new node")
        print("2: Registering a direction")
        print("3: Updating program")
        print("4: Updating a registered node")
        print("5: Removing a registered node")
        print("6: Removing a registered arrow")
        choice = input("You choice is: ")
        print("----------------------------------------")
        if choice == "1":
            try:
                ind = int(input("New node's index is: "))
            except:
                ind = -1 # out of list range
            coordinator.registering_a_new_node(ind)

        elif choice == "2":
            try:
                arrow = input("Enter an arrow: ").split(" ")
                u = int(arrow[0])
                v = int(arrow[1])
                ind = int(arrow[2])
            except:
                u, v, ind = -1, -1, -1 # out of list range
            coordinator.registering_a_new_arrow(u, v, ind)

        elif choice == "3":
            coordinator.updating_order()

        elif choice == "4":
            try:
                gid = int(input("Node's Global ID is: "))
            except:
                gid = -1
            coordinator.updating_a_registered_node(gid)
        
        elif choice == "5":
            try:
                gid = int(input("Node's Global ID is: "))
            except:
                gid = -1
            coordinator.removing_a_registered_node(gid)

        elif choice == "6":
            try:
                arrow = input("Enter an arrow: ").split(" ")
                u = int(arrow[0])
                v = int(arrow[1])
            except:
                u, v = -1, -1
            coordinator.removing_a_registered_arrow(u, v)

        elif choice == "save":
            coordinator.save()
        elif choice == "load":
            coordinator.load()


        elif choice == "0":
            break
        else:
            continue

    print("----------------------------------------")
    print("Good luck Have fun.")


if __name__ == '__main__':
    run()