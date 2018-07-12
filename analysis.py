import matplotlib.pyplot as plt
from numpy import sqrt, mean, square
import pandas as pd



# loading datasets
cvm1 = pd.read_csv('/home/roger.vieira/Downloads/laura/Roger/cvm1.txt', header = None, sep = '\t', decimal = ',')
cvm2 = pd.read_csv('/home/roger.vieira/Downloads/laura/Roger/cvm2.txt', header = None, sep = '\t', decimal = ',')
cvm3 = pd.read_csv('/home/roger.vieira/Downloads/laura/Roger/cvm3.txt', header = None, sep = '\t', decimal = ',')

#rep1 = pd.read_csv('/home/roger.vieira/Downloads/laura/Roger/roger1.txt', header = None, sep = '\t', decimal = ',')
#rep2 = pd.read_csv('/home/roger.vieira/Downloads/laura/Roger/roger2.txt', header = None, sep = '\t', decimal = ',')
#rep3 = pd.read_csv('/home/roger.vieira/Downloads/laura/Roger/roger3.txt', header = None, sep = '\t', decimal = ',')


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


fig = plt.figure()

ch4 = fig.add_subplot(411)
ch5 = fig.add_subplot(412)
ch6 = fig.add_subplot(413)
ch7 = fig.add_subplot(414)

ch4.plot(cvm1[0], cvm1[1], label = 'CH4')
ch5.plot(cvm1[0], cvm1[2])
ch6.plot(cvm1[0], cvm1[3])
ch7.plot(cvm1[0], cvm1[4])


'''

process_four_channels(cvm1)
process_four_channels(cvm2)
process_four_channels(cvm3) '''

plt.show()



