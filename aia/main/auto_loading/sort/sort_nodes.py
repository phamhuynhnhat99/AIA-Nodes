from aia.NENV import *
import numpy as np

class SortAlgNodeBase(Node):

    def __init__(self):
        super().__init__()
        self.res = list()

    def set_inputs(self, node, data):
        self.reset_all()
        self.push_prev_nodes(node)
        self.push_data_inputs(data)

    def update_event(self):
        self.res = self.sort()
        if len(self.data_outputs) == 0:
            self.push_data_outputs(self.res)
        else:
            self.set_data_outputs(type=0, obj=self.res)


class SelectionSort(SortAlgNodeBase):
    title = "Seletion Sort"

    def sort(self):
        arr = self.get_data_inputs(0)
        for i in range(0, len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr


export_nodes = [
    SelectionSort,

]