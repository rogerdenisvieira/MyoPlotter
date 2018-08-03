import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt, mean, square
import pandas as pd
import os

############################################################
#                                                          #
#                        PARAMETERS                        #
#                                                          #
############################################################

person_name = 'vini'

root_path = 'datasets/{}/'.format(person_name)
output_path = '{}_graphs'.format(person_name)

show_graphs = False
save_graphs = True

dpi = 100



############################################################
#                                                          #
#                     INTERNAL FUNCTIONS                   #
#                                                          #
############################################################

# setting figure up
figure = plt.gcf() # get current figure
figure.set_size_inches(16, 9)

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


os.makedirs(output_path)

############################################################
#                                                          #
#                     LOADING RAW DATA                     #
#                                                          #
############################################################

# loading cvm datasets
cvm1 = import_emg_data(root_path, 'cvm1.txt')
cvm2 = import_emg_data(root_path, 'cvm2.txt')
cvm3 = import_emg_data(root_path, 'cvm3.txt')

# loading repetitions datasets
rep1 = import_emg_data(root_path, '{}1.txt'.format(person_name))
rep2 = import_emg_data(root_path, '{}2.txt'.format(person_name))
rep3 = import_emg_data(root_path, '{}3.txt'.format(person_name))

############################################################
#                                                          #
#                       CALCULATING RMS                    #
#                                                          #
############################################################

cvm1_rms = calc_rms(cvm1)
cvm2_rms = calc_rms(cvm2)
cvm3_rms = calc_rms(cvm3)

rep1_rms = calc_rms(rep1)
rep2_rms = calc_rms(rep2)
rep3_rms = calc_rms(rep3)


############################################################
#                                                          #
#                       CVM PROCESSING                     #
#                                                          #
############################################################

plt.suptitle('Sinais por Canal em Cada CVM')

############################ CVM1 ##########################
for i in range(1,5):
    print('CVM1 Iteration {}'.format(i))
    plt.subplot(3,4,i)
    plt.plot(cvm1[0], cvm1[i], color = 'black')
    plt.title('CH{}'.format(i+3))


############################ CVM2 ##########################

for i in range(1,5):
    print('CVM2 Iteration {}'.format(i))
    plt.subplot(3,4,4+i)
    plt.plot(cvm2[0], cvm2[i], color = 'black')
    plt.title('CH{}'.format(i+3))

############################ CVM3 ##########################

for i in range(1,5):
    print('CVM3 Iteration {}'.format(i))
    plt.subplot(3,4,8+i)
    plt.plot(cvm3[0], cvm3[i], color = 'black')
    plt.title('CH{}'.format(i+3))

plt.tight_layout()

if save_graphs:
    plt.savefig('{}/lines_cvm_{}'.format(output_path ,person_name), dpi = dpi)
    plt.clf()

if show_graphs:
    plt.show()

############################################################
#                                                          #
#                  REPETITIONS PROCESSING                  #
#                                                          #
############################################################

plt.suptitle('Sinais por Canal em Cada Repetição')

############################ REP1 ##########################
for i in range(1,6):
    print('REP1 Iteration {}'.format(i))
    plt.subplot(3,5,i)
    plt.plot(rep1[0], rep1[i], color = 'black')
    plt.title('CH{}'.format(i+3))


############################ REP2 ##########################
for i in range(1,6):
    print('REP2 Iteration {}'.format(i))
    plt.subplot(3,5,5+i)
    plt.plot(rep2[0], rep2[i], color = 'black')
    plt.title('CH{}'.format(i+3))



############################ REP3 ##########################
for i in range(1,6):
    print('REP3 Iteration {}'.format(i))
    plt.subplot(3,5,10+i)
    plt.plot(rep3[0], rep3[i], color = 'black')
    plt.title('CH{}'.format(i+3))

plt.tight_layout()

if save_graphs:
    plt.savefig('{}/lines_rep_{}'.format(output_path ,person_name), dpi = dpi)
    plt.clf()

if show_graphs:
    plt.show()

############################################################
#                                                          #
#                  COMPARISONS USING RMS                   #
#                                                          #
############################################################



# comparison by channel in each CVM
print('Creating graph for comparisons by channel in each CVM')

N = 4
ind = np.arange(N) 
width = 0.15       

plt.bar(
    ind, 
    (cvm1_rms[1],cvm1_rms[2],cvm1_rms[3],cvm1_rms[4]), 
    width, 
    label='CVM 1'
    )

plt.bar(ind+width, 
    (cvm2_rms[1],cvm2_rms[2],cvm2_rms[3],cvm2_rms[4]), 
    width,
    label='CVM 2')

plt.bar(ind+width*2,
    (cvm3_rms[1],cvm3_rms[2],cvm3_rms[3],cvm3_rms[4]), 
    width,
    label='CVM 3')

plt.xticks(ind+width, ('CH4', 'CH5', 'CH6', 'CH7'))
plt.legend(loc='best')
plt.title('RMS por Canal em Cada CVM')
plt.xlabel('Canais')
plt.ylabel('RMS')
plt.grid()

if save_graphs:
    plt.savefig('{}/barchart_rms_cvm_{}'.format(output_path ,person_name), dpi = dpi)
    plt.clf()

if show_graphs:
    plt.show()


# comparison by channel in each repetition
print('Creating graph for comparisons by channel in each repetition')

N = 4
ind = np.arange(N) 
width = 0.15       

plt.bar(
    ind, 
    (rep1_rms[2],rep1_rms[3],rep1_rms[4],rep1_rms[5]), 
    width, 
    label='Repetição 01'
    )

plt.bar(ind+width, 
    (rep2_rms[2],rep2_rms[3],rep2_rms[4],rep2_rms[5]), 
    width,
    label='Repetição 02')

plt.bar(ind+width*2,
    (rep3_rms[2],rep3_rms[3],rep3_rms[4],rep3_rms[5]), 
    width,
    label='Repetição 03')

plt.xticks(ind+width, ('CH4', 'CH5', 'CH6', 'CH7'))
plt.legend(loc='best')
plt.title('RMS por Canal em Cada Repetição')
plt.xlabel('Canais')
plt.ylabel('RMS')
plt.grid()

if save_graphs:
    plt.savefig('{}/barchart_rms_rep_{}'.format(output_path ,person_name), dpi = dpi)
    plt.clf()

if show_graphs:
    plt.show()


############################################################
#                                                          #
#                COMPARISONS REP X CVMS                    #
#                                                          #
############################################################

print('Calculating mean cvm signal by channel')
ch4_mean_cvm = mean([cvm1_rms[1], cvm2_rms[1], cvm3_rms[1]])
ch5_mean_cvm = mean([cvm1_rms[2], cvm2_rms[2], cvm3_rms[2]])
ch6_mean_cvm = mean([cvm1_rms[3], cvm2_rms[3], cvm3_rms[3]])
ch7_mean_cvm = mean([cvm1_rms[4], cvm2_rms[4], cvm3_rms[4]])

print('Calculating mean repetition signal by channel')
ch4_mean_rep = mean([rep1_rms[2], rep2_rms[2], rep3_rms[2]])
ch5_mean_rep = mean([rep1_rms[3], rep2_rms[3], rep3_rms[4]])
ch6_mean_rep = mean([rep1_rms[4], rep2_rms[4], rep3_rms[4]])
ch7_mean_rep = mean([rep1_rms[5], rep2_rms[5], rep3_rms[5]])


N = 4
ind = np.arange(N) 
width = 0.15       

plt.bar(
    ind, 
    (ch4_mean_cvm, ch5_mean_cvm, ch6_mean_cvm, ch7_mean_cvm), 
    width, 
    label='CVM'
    )

plt.bar(ind+width, 
    (ch4_mean_rep, ch5_mean_rep, ch6_mean_rep, ch7_mean_rep), 
    width,
    label='Repetição')

plt.xticks(ind+width, ('CH4', 'CH5', 'CH6', 'CH7'))
plt.legend(loc='best')
plt.title('Médias RMS CVM e Repetição')
plt.xlabel('Canais')
plt.ylabel('RMS')
plt.grid()

if save_graphs:
    plt.savefig('{}/barchar_final_{}'.format(output_path ,person_name), dpi = dpi)
    plt.clf()

if show_graphs:
    plt.show()
