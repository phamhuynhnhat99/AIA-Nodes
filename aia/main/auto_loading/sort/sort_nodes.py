from aia.NENV import *
import numpy as np

class SortAlgNodeBase(Node):

    def __init__(self):
        super().__init__()
        self.res = list()

    def set_prev(self, node):
        if len(self.prev_nodes) == 0:
            self.push_prev_nodes(node)
        else:
            self.set_prev_nodes(type=0, obj=node)

        data = node.get_data_outputs(type = 0).copy()
        if len(self.data_inputs) == 0:
            self.push_data_inputs(data)
        else:
            self.set_data_inputs(type=0, obj=data)

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
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr


class MergeSort(SortAlgNodeBase):
    title = "Merge Sort"

    def sort(self):
        
        def merge_sort(a, l, r):
            if l >= r:
                return
            m = (l + r) // 2
            merge_sort(a, l, m)
            merge_sort(a, m+1, r)
            b = a[l:r+1].copy()
            il = l
            ir = m+1
            for i in range(r-l+1):
                if il <= m:
                    if ir > r or b[il-l] < b[ir-l]:
                        a[l+i] = b[il-l]
                        il += 1
                    else:
                        a[l+i] = b[ir-l]
                        ir += 1
                else:
                    a[l+i] = b[ir-l]
                    ir += 1

        arr = self.get_data_inputs(0)
        merge_sort(arr, 0, len(arr)-1)
        return arr


export_nodes = [
    SelectionSort,
    MergeSort,
]