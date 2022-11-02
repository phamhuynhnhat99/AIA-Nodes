from aia.NENV import *
import numpy as np

class ArrayNodeBase(Node):

    def __init__(self):
        super().__init__()
        self.arr = list()

    def set_arr(self, new_arr):
        self.arr = new_arr

    def update_event(self):
        self.arr = self.get_arr()
        self.set_data_outputs(type=0, obj=self.arr)


class ReadArray(ArrayNodeBase):
    title = "Read Array"

    def read_arr(self):
        self.push_prev_nodes(None)
        self.push_data_inputs("/home/aia/Nhat/AIA-Nodes/aia/main/auto_loading/array/arr.txt")
        arr_path = self.get_data_inputs(type=0)
        with open(arr_path, "r") as fi:
            content = fi.read().split(" ")
            arr = [float(_) for _ in content]
            fi.close()
        obj = [arr]
        self.set_arr(arr)
        self.set_data_outputs(type=-1, obj=obj)
    
    def get_arr(self):
        return self.arr


class ShowArray(ArrayNodeBase):
    title = "Show Array"

    def set_prev(self, node):
        if len(self.prev_nodes) == 0:
            self.push_prev_nodes(node)
        else:
            self.set_prev_nodes(type=0, obj=node)

        data = node.get_data_outputs(type = 0)
        if len(self.data_inputs) == 0:
            self.push_data_inputs(data)
        else:
            self.set_data_inputs(type=0, obj=data)
        

    def show_arr(self):
        inputs = self.get_data_inputs()
        if len(inputs) >= 1:
            self.arr = inputs[0]
            print("Show Array")
            print(self.arr)
            if len(self.data_outputs) == 0:
                self.push_data_outputs(self.arr)
            else:
                self.set_data_outputs(type=0, obj=self.arr)
        else:
            print("Empty Array")
            self.set_data_outputs(type=-1, obj=list())
        

    def get_arr(self):
        return self.arr


export_nodes = [
    ReadArray,
    ShowArray,
    
]