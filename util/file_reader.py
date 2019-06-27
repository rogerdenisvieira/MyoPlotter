import pandas as pd


class FileReader(object):
    def __init__(self, person_name=None):
        self.person_name = person_name
        self.root_path = 'datasets/{}/'.format(person_name)

    ############################################################
    #                                                          #
    #                     LOADING RAW DATA                     #
    #                                                          #
    ############################################################

    def get_cvms(self):
        # loading cvm datasets
        cvm1 = import_emg_data(self.root_path, 'cvm1.txt')
        cvm2 = import_emg_data(self.root_path, 'cvm2.txt')
        cvm3 = import_emg_data(self.root_path, 'cvm3.txt')

        cvm_list = [cvm1, cvm2, cvm3]

        return cvm_list

    def get_rms(self):
        # loading repetitions datasets
        rep1 = import_emg_data(self.root_path, '{}1.txt'.format(self.person_name))
        rep2 = import_emg_data(self.root_path, '{}2.txt'.format(self.person_name))
        rep3 = import_emg_data(self.root_path, '{}3.txt'.format(self.person_name))

        rep_list = [rep1, rep2, rep3]

        return rep_list


def import_emg_data(root_path, filename):
    print('Importing data from {}'.format(root_path + filename))

    return pd.read_csv(root_path + filename, header=None, sep='\t', decimal=',')
