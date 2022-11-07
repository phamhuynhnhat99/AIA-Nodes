from aia.NENV import *

class SortAlgNodeBase(Node):

    def __init__(self):
        super().__init__()
        self.res = list()

    def update_event(self):
        self.res = self.sort()
        self.set_data_output(key="array", obj=self.res)


class SelectionSort(SortAlgNodeBase):
    title = "Seletion Sort"

    def sort(self):

        def selection_sort(a, l, r):
            for i in range(l, r):
                for j in range(i+1, r+1):
                    if a[i] < a[j]:
                        a[i], a[j] = a[j], a[i]

        arr = list()
        input = self.get_data_inputs(0)
        if input:
            if "array" in input.keys():
                arr = input["array"].copy()
                selection_sort(arr, 0, len(arr)-1)
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
        
        arr = list()
        input = self.get_data_inputs(0)
        if input:
            if "array" in input.keys():
                arr = input["array"].copy()
                merge_sort(arr, 0, len(arr)-1)
        return arr


export_nodes = [
    SelectionSort,
    MergeSort,
]