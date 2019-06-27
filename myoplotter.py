import os
import sys

import matplotlib.pyplot as plt

from mathematics.calculator import rms
from comparator.rms_rep_comparator import RMSREPComparator
from comparator.rms_cvm_comparator import RMSCVMComparator
from comparator.rms_final_comparator import RMSFinalComparator

from process import cvm_processor, repetitions_processor
from util import file_reader

############################################################
#                                                          #
#                        PARAMETERS                        #
#                                                          #
############################################################


try:
    person_name = sys.argv[1]
    show_charts = True
    save_charts = True
except IndexError:
    print("Please provide a valid input.")
    sys.exit()

output_path = '{}_graphs'.format(person_name)

############################################################
#                                                          #
#                     INTERNAL FUNCTIONS                   #
#                                                          #
############################################################

# setting figure up
figure = plt.gcf()  # get current figure
figure.set_size_inches(16, 9)

read_filesVar = file_reader.FileReader(person_name)

cvmList = read_filesVar.get_cvms()
repList = read_filesVar.get_rms()


print("Creating output directory")
print("Processing data")
os.makedirs(output_path, exist_ok=True)

# ############################################################
# #                                                          #
# #                       CALCULATING RMS                    #
# #                                                          #
# ############################################################

cvm1_rms = rms(cvmList[0])
cvm2_rms = rms(cvmList[1])
cvm3_rms = rms(cvmList[2])

rep1_rms = rms(repList[0])
rep2_rms = rms(repList[1])
rep3_rms = rms(repList[2])

cvmRmsList = [cvm1_rms, cvm2_rms, cvm3_rms]
repRmsList = [rep1_rms, rep2_rms, rep2_rms]

############################################################
#                                                          #
#                       CVM LINES                          #
#                                                          #
############################################################

cvm_process_var = cvm_processor.CvmProcess()
cvm_process_var.process(cvmList, output_path, person_name, show_charts, save_charts)

############################################################
#                                                          #
#                  REPETITIONS LINES                       #
#                                                          #
############################################################

repetitions_process_var = repetitions_processor.RepetitionsProcess()
repetitions_process_var.process(repList, output_path, person_name, show_charts, save_charts)

############################################################
#                                                          #
#                  RMS CVM COMPARISON                      #
#                                                          #
############################################################

compare_rms_cvm_var = RMSCVMComparator()
compare_rms_cvm_var.compare(cvmRmsList, output_path, person_name, show_charts, save_charts)

############################################################
#                                                          #
#                  RMS REP COMPARISON                      #
#                                                          #
############################################################

compare_rms_rep_var = RMSREPComparator()
compare_rms_rep_var.compare(repRmsList, output_path, person_name, show_charts, save_charts)

############################################################
#                                                          #
#                COMPARISONS REP X CVMS                    #
#                                                          #
############################################################
compare_final_var = RMSFinalComparator()
compare_final_var.compare(repRmsList, cvmRmsList, output_path, person_name, show_charts, save_charts)


print("Done")
