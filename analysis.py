import matplotlib.pyplot as plt
from numpy import sqrt, mean, square
import pandas as pd

root_path = 'datasets/'

############################################################
#                                                          #
#                     INTERNAL FUNCTIONS                   #
#                                                          #
############################################################

def import_emg_data(root_path, filename):
    print('Importing data from {}'.format(root_path + filename))

    return pd.read_csv(
        root_path + filename,
        header = None,
        sep = '\t',
        decimal = ','
        )


# creating a RMS function
def calc_rms(serie):
    return round(sqrt(mean(square(serie))),4)

# useful to show RMS per channel 
def process_four_channels(dataset):
    print('CH4 {0} \tCH5 {1} \tCH6 {2} \tCH7 {3}'
    .format(calc_rms(
        dataset[1]),
        calc_rms(dataset[2]),
        calc_rms(dataset[3]),
        calc_rms(dataset[4])
        )
    )

############################################################
#                                                          #
#                     LOADING RAW DATA                     #
#                                                          #
############################################################

# loading cvm datasets
cvm1 = import_emg_data(root_path, 'cvm1.txt')
cvm2 = import_emg_data(root_path, 'cvm2.txt')
cvm3 = import_emg_data(root_path, 'cvm3.txt')

# loading series datasets
rep1 = import_emg_data(root_path, 'roger1.txt')
rep2 = import_emg_data(root_path, 'roger2.txt')
rep3 = import_emg_data(root_path, 'roger3.txt')

# loading real cvm datasets
cvm_real1 = import_emg_data(root_path, 'cvmreal1.txt')
cvm_real2 = import_emg_data(root_path, 'cvmreal2.txt')
cvm_real3 = import_emg_data(root_path, 'cvmreal3.txt')

############################################################
#                                                          #
#                       CVM PROCESSING                     #
#                                                          #
############################################################

plt.suptitle('Sinais por CVM')

############################ CVM1 ##########################
for i in range(1,5):
    print('Iteration {}'.format(i))
    plt.subplot(3,4,i)
    plt.plot(cvm1[0], cvm1[i], color = 'black')
    plt.title('CH{}'.format(i+3))


############################ CVM2 ##########################

for i in range(1,5):
    plt.subplot(3,4,4+i)
    plt.plot(cvm2[0], cvm2[i], color = 'black')
    plt.title('CH{}'.format(i+3))

############################ CVM3 ##########################

for i in range(1,5):
    plt.subplot(3,4,8+i)
    plt.plot(cvm3[0], cvm3[i], color = 'black')
    plt.title('CH{}'.format(i+3))

plt.show()

############################################################
#                                                          #
#                  REPETITIONS PROCESSING                  #
#                                                          #
############################################################

plt.suptitle('Sinais por Repetição')

############################ REP1 ##########################
for i in range(1,6):
    print('Iteration {}'.format(i))
    plt.subplot(3,5,i)
    plt.plot(rep1[0], rep1[i], color = 'black')
    plt.title('CH{}'.format(i+3))



############################ REP2 ##########################
for i in range(1,6):
    print('Iteration {}'.format(i))
    plt.subplot(3,5,5+i)
    plt.plot(rep2[0], rep2[i], color = 'black')
    plt.title('CH{}'.format(i+3))



############################ REP3 ##########################
for i in range(1,6):
    print('Iteration {}'.format(i))
    plt.subplot(3,5,10+i)
    plt.plot(rep3[0], rep3[i], color = 'black')
    plt.title('CH{}'.format(i+3))

plt.show()

############################################################
#                                                          #
#                 PROCESSING LAST CVM SERIES               #
#                                                          #
############################################################

plt.suptitle('Sinais por CVM Colchonete')

############################ CVM1 ##########################
for i in range(2,6):
    print('Iteration {}'.format(i))
    plt.subplot(3,4,i-1)
    plt.plot(cvm_real1[0], cvm_real1[i], color = 'black')
    plt.title('CH{}'.format(i+3))



############################ CVM2 ##########################
for i in range(2,6):
    print('Iteration {}'.format(i))
    plt.subplot(3,4,3+i)
    plt.plot(cvm_real2[0], cvm_real2[i], color = 'black')
    plt.title('CH{}'.format(i+3))



############################ CVM3 ##########################
for i in range(2,6):
    print('Iteration {}'.format(i))
    plt.subplot(3,4,7+i)
    plt.plot(cvm_real3[0], cvm_real3[i], color = 'black')
    plt.title('CH{}'.format(i+3))

plt.show()

############################################################
#                                                          #
#                  COMPARISONS USING RMS                   #
#                                                          #
############################################################