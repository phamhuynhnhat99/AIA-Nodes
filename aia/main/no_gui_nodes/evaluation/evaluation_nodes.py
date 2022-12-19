from aia.NENV import *

widgets = import_widgets(__file__) # optional

import numpy as np

class EvaluationNodeBase(Node):
    path = "evaluation/evaluation_nodes" # compulsory

    def __init__(self, num_inp=2, num_out=1, title=''):
        super().__init__(num_inp, num_out, title)
    

    def get_output(self):
        return self.get_eval()

    
    def update_event(self):
        self.output = self.get_output()
        self.nodevalueoutput_[0] = self.output


class DiceCoefficient(EvaluationNodeBase):
    title = "Dice Coefficient"

    def __init__(self, num_inp=2, num_out=1, title=''):
        super().__init__(num_inp, num_out, title)
        self.default_eval = -1
        self.eval = self.default_eval

    def get_eval(self):
        self.update_nodevalueinputs()
        input = self.get_nodevalueinputs(ind=-1)
        if input:
            if 0 in input.keys() and 1 in input.keys():
                                
                try:
                    y_true_ = np.array(input[0][0])
                    y_pred_ = np.array(input[1][0])
                    y_true = y_true_[:, :, 3] # 4th channel
                    y_pred = y_pred_[:, :, 3] # 4th channel
                    y_true_shape = y_true.shape
                    y_pred_shape = y_pred.shape
                    if y_true_shape == y_pred_shape:
                        count_similarity = 0
                        for row in range(y_true_shape[0]):
                            for col in range(y_true_shape[1]):
                                count_similarity += 1 if y_true[row][col] == y_pred[row][col] else 0
                        
                        num_pixels = y_true_shape[0] * y_true_shape[1]
                        self.eval = (1 + 2*count_similarity) / (1 + num_pixels)

                    else:
                        self.eval = self.default_eval
                except Exception:
                    print(Exception)
                    self.eval = self.default_eval
            else:
                self.eval = self.default_eval
        else:
            self.eval = self.default_eval
        print(self.eval)
        return self.eval


# compulsory
export_nodes = [
    DiceCoefficient,
]