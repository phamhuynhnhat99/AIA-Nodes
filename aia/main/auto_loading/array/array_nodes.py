from aia.NENV import *
import numpy as np

class ArrayNodeBase(Node):

    def __init__(self):
        super().__init__()
        self.arr = list()

    def update_event(self):
        self.arr = self.get_arr()
        self.set_data_output(key="unique", obj=self.arr)


class ReadArray(ArrayNodeBase):
    title = "Read Array"
    
    def get_arr(self):
        if len(self.prev_nodes) == 0:
            self.push_prev_nodes(None)
        else:
            self.set_prev_nodes(ind=0, obj=None)
        self.set_fake_input(["/home/aia/Nhat/AIA-Nodes/aia/main/auto_loading/array/arr.txt"])
        
        arr_path = self.get_fake_input()[0]
        with open(arr_path, "r") as fi:
            content = fi.read().split(" ")
            arr = [float(_) for _ in content]
            fi.close()

        return arr


class ShowArray(ArrayNodeBase):
    title = "Show Array"

    def get_arr(self):

        input = self.get_data_inputs(ind=0)
        if input:
            arr = input["unique"]
            print("Show Array")
            print(arr)
        else:
            arr = list()
        return arr


export_nodes = [
    ReadArray,
    ShowArray,
    
]