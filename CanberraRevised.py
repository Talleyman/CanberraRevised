#! /usr/bin/python
#Canberra Distance metric for ranked lists-Revised Edition v1.0
#Stephen Talley
#Date started: January 17, 2015
import csv
import getopt, sys
try:
    import numpy
except ImportError:
    print "Cannot import numpy. Please install numpy and try again.\n"
try:
    import mlpy
except ImportError:
    print "Cannot import mlpy. Please install mlpy and try again.\n"
    
def Doc():
    print "Canberra Distance help menu:\n\n"
    print "Use -v or -verbose to trigger verbose mode.\n"
    print "Use -h or -help to access this menu.\n"
    print "Use -f or -inFile to specify the name of the input file (i.e. the file with the ranked lists).\n"
    print "Use -s or -inSep to set the delimiter on the input file.\n"
    print "Use -o or -outFile to set the desired name for your output file (e.g. My_Results).\n"
    print "Use -S or -outSep to set the desired delimiter on your outputfile.\n"
    
def GetArgs():#Collects the arguments for the program
    try:
        ops, args = getopt.getopt(sys.argv[1:],shortops="vhf:s:o:S:", longops=["verbose","help","inFile","inSep","outFile","outSep"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit()
    #Establish default values for arguments
    verbose=False
    inputsep="comma"
    outputsep="comma"
    outFile="Canberra_Results"
    #Loop through command line arguments to get file names and specifications
    for o in ops:
        if o in ("-v","verbose"):
            verbose=True
        elif o in ("-h","help"):
            if verbose:
                print "Loading help menu..."
            Doc()
        elif o in ("-f","-inFile"):
            inFile=str(o)
            if verbose:
                print "Input file to be analyzed is named", inFile
        elif o in ("-s","-inSep"):
            inputsep=str(o)
            if verbose:
                print "Input delimiter is set to", inputsep
        elif o in ("-o","-outFile"):
            outFile=str(o)
            if verbose:
                print "Output file name is specified as", outFile
        elif o in ("-S","-outSep"):
            outputsep=str(o)
            if verbose:
                print "Output delimiter is set to", outputsep
    try:
        inFile
    except NameError:
        print "No input file found! Input file required for analysis."
    try:
        in
def GetData():
    
