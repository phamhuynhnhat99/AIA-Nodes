from aia.NENV import *
import numpy as np

class ListNodeBase(Node):

    def __init__(self, params):
        super().__init__(params)
        self.arr = None

    def show_list(self):
        print(self.arr)

    def update_event(self):
        self.arr = self.get_arr()
        self.set_outputs(0, self.arr)


class ReadList(ListNodeBase):
    title = "Read List"
    def read_arr(self):
        with open("arr.txt", "r") as fi:
            content = fi.read().split(" ")
            arr = [float(_) for _ in content]
            fi.close()
        self.push_outputs(arr)


class ShowList(ListNodeBase):
    title = "Show List"
    def get_arr(self):
        inputs = self.get_inputs()
        if len(inputs) >= 1:
            return self.input(0)
        return None

