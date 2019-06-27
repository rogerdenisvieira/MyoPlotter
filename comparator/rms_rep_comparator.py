import matplotlib.pyplot as plt
import numpy as np
from comparator.base_comparator import BaseComparator

DPI = 100


class RMSREPComparator(BaseComparator):
    def __init__(self):
        BaseComparator.__init__(self)
        pass

    def compare(self, rep_rms_list, output_path, person_name, show_charts, save_charts):

        print('Creating chart for comparisons by channel in each repetition')

        elements = 4
        ind = np.arange(elements)
        width = 0.15

        for i in range(0, 3):
            plt.bar(
                ind + (width * i),
                (rep_rms_list[i][1], rep_rms_list[i][2], rep_rms_list[i][3], rep_rms_list[i][4]),
                width,
                label="Repetição {}".format(i + 1)
            )

        plt.xticks(ind + width, ('CH4', 'CH5', 'CH6', 'CH7'))
        plt.legend(loc='best')
        plt.title('RMS por Canal em Cada Repetição')
        plt.xlabel('Canais')
        plt.ylabel('RMS')
        plt.grid()

        if save_charts:
            plt.savefig('{}/[BAR]_RMS_REP_{}'.format(output_path, person_name), dpi=DPI)
            plt.clf()

        if show_charts:
            plt.show()