import matplotlib.pyplot as plt
import numpy as np
from numpy import mean
from comparator.base_comparator import BaseComparator

DPI = 100


class RMSFinalComparator(BaseComparator):
    def __init__(self):
        BaseComparator.__init__(self)
        pass

    def compare(self, rep_rms_list, cvm_rms_list, output_path, person_name, show_charts, save_charts):
        print('Calculating mean cvm signal by channel')
        ch4_mean_cvm = mean([cvm_rms_list[0][1], cvm_rms_list[1][1], cvm_rms_list[2][1]])
        ch5_mean_cvm = mean([cvm_rms_list[0][2], cvm_rms_list[1][2], cvm_rms_list[2][2]])
        ch6_mean_cvm = mean([cvm_rms_list[0][3], cvm_rms_list[1][3], cvm_rms_list[2][3]])
        ch7_mean_cvm = mean([cvm_rms_list[0][4], cvm_rms_list[1][4], cvm_rms_list[2][4]])

        print('Calculating mean repetition signal by channel')
        ch4_mean_rep = mean([rep_rms_list[0][2], rep_rms_list[1][2], rep_rms_list[2][2]])
        ch5_mean_rep = mean([rep_rms_list[0][3], rep_rms_list[1][3], rep_rms_list[2][3]])
        ch6_mean_rep = mean([rep_rms_list[0][4], rep_rms_list[1][4], rep_rms_list[2][4]])
        ch7_mean_rep = mean([rep_rms_list[0][5], rep_rms_list[1][5], rep_rms_list[2][5]])

        n = 4
        ind = np.arange(n)
        width = 0.15

        plt.bar(
            ind,
            (ch4_mean_cvm, ch5_mean_cvm, ch6_mean_cvm, ch7_mean_cvm),
            width,
            label='CVM'
        )

        plt.bar(ind + width,
                (ch4_mean_rep, ch5_mean_rep, ch6_mean_rep, ch7_mean_rep),
                width,
                label='Repetição')

        plt.xticks(ind + width, ('CH4', 'CH5', 'CH6', 'CH7'))
        plt.legend(loc='best')
        plt.title('Médias RMS CVM e Repetição')
        plt.xlabel('Canais')
        plt.ylabel('RMS')
        plt.grid()

        if save_charts:
            plt.savefig('{}/[BAR]_Final_{}'.format(output_path, person_name), dpi=DPI)
            plt.clf()

        if show_charts:
            plt.show()
