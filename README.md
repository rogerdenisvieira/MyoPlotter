# MyoPlotter
Plot and analysis of collected data in an EMG System electromyography device using matlibplot, pandas and numpy.

## Usage

In a command line interface, inside of root path, run following command:

```
> python myoplotter.py name show_charts save_charts

name            the subject's name identified in data files
show_charts     shows a window with plotted charts 
save_charts     exports the output files 
```

In order to execute MyoPlotter properly, processing files must have be placed into */datasets* folder, according by following naming pattern:

```bash
├───datasets
│   └───foobar
│           cvm1.txt
│           cvm2.txt
│           cvm3.txt
│           foobar1.txt
│           foobar2.txt
│           foobar3.txt
```

**Note**:  name *foobar* needs to be replaced by name of the subjects in your experiment

## Format Supporting

MyoPlotter supports TSV (Tab Separated Values) files format. The CVM files (e.g. cvm1.txt) follows the pattern:

```
[time]  [channel 4]             [channel 5]             [channel 6]             [channel 7]

0,0000  -39,2919813839931	11,2153810940718	10,1472495613031	14,2671854734111	
0,0005	-25,7114518959334	17,3189898527504	0,686655985351337	11,0627908751049	
0,001	-2,97550926985579	30,2891584649423	-3,12809948882276	15,3353170061798	

...

6,4985	35,0194552529182	-6,79026474402988	-33,0357824063476	-21,1337453269245	
16,499	38,8342107270923	-8,77393759060041	-25,5588616769664	-17,0138094148165	
16,4995	43,7170977340351	-8,46875715266648	-18,8448920424200       -14,1145952544441	
```

Also, Repetition files (e.g. foobar1.txt) takes the data structure:

```
[time]  [channel 4]             [channel 5]             [channel 6]             [channel 7]             [channel 8]

0	-27,6484172579538	-23,270008392462	-13,1990539406424	13,1990539406424	6,02731364919507
0,0005	-27,6484172579538	-24,9485008010986	-9,38429846646827	12,5886930647745	8,77393759060041
0,001	-27,6484172579538	-25,2536812390325	-4,34882124055846	12,4361028458075	9,99465934233612

...

16,6985	-27,6322396429389	-31,9676508735789	18,0819409475852	3,28068970778972	13,6568245975432
16,699	-27,616062027924	-10,9102006561379	28,9158464942396	-1,44960708018615	15,4879072251468
16,6995	-27,6322396429389	3,12809948882276	30,5943389028762	-5,56954299229417	12,4361028458075
```

## Output

As output, MyoPlotter generates a set of charts into folder */foobar_graphs*, as following:

```bash
├───foobar_graphs
│       [BAR]_Final_foobar.png
│       [BAR]_RMS_CVM_foobar.png
│       [BAR]_RMS_REP_foobar.png
│       [LINES]_CVM_foobar.png
│       [LINES]_REP_foobar.png
```
***


