import sys
import matplotlib.pyplot as plt
from process.base_processor import BaseProcessor

ROW_OFFSET = 4
COLUMN_OFFSET = 3
DPI = 100


class CvmProcess(BaseProcessor):

    def __init__(self):
        BaseProcessor.__init__(self)
        pass

    def process(self, cvm_rms_list, output_path, person_name, show_charts, save_charts):

        figure = plt.gcf()
        figure.set_size_inches(16, 9)

        plt.suptitle('Sinais por Canal em Cada CVM')

        for row in range(0,3):
            BaseProcessor.show_progress()
            for column in range(1,5):
                plt.subplot(3, 4, column + (row * ROW_OFFSET))
                plt.plot(cvm_rms_list[row][0], cvm_rms_list[row][column], color='black')
                plt.title('CH{}'.format(column + COLUMN_OFFSET))
                BaseProcessor.show_progress()

        plt.tight_layout()

        if save_charts:
            plt.savefig('{}/[LINES]_CVM_{}'.format(output_path, person_name), dpi=100)
            plt.clf()

        if show_charts:
            plt.show()