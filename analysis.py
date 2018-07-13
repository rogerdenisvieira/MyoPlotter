import matplotlib.pyplot as plt
from numpy import sqrt, mean, square
import pandas as pd

root_path = 'datasets/'


# loading datasets
cvm1 = pd.read_csv(root_path + 'cvm1.txt', header = None, sep = '\t', decimal = ',')
cvm2 = pd.read_csv(root_path + 'cvm2.txt', header = None, sep = '\t', decimal = ',')
cvm3 = pd.read_csv(root_path + 'cvm3.txt', header = None, sep = '\t', decimal = ',')

rep1 = pd.read_csv(root_path + 'roger1.txt', header = None, sep = '\t', decimal = ',')
rep2 = pd.read_csv(root_path + 'roger2.txt', header = None, sep = '\t', decimal = ',')
rep3 = pd.read_csv(root_path + 'roger3.txt', header = None, sep = '\t', decimal = ',')

cvm_real1 = pd.read_csv(root_path + 'cvmreal1.txt', header = None, sep = '\t', decimal = ',')
cvm_real2 = pd.read_csv(root_path + 'cvmreal2.txt', header = None, sep = '\t', decimal = ',')
cvm_real3 = pd.read_csv(root_path + 'cvmreal3.txt', header = None, sep = '\t', decimal = ',')


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
#                   PROCESSANDO AS CVM                     #
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
#               PROCESSANDO AS REPETIÇÕES                  #
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
#               PROCESSANDO O CVM COLCHONETE               #
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
#                     COMPARAÇÕES RMS                      #
#                                                          #
############################################################