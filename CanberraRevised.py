#! /usr/bin/python
#Canberra Distance metric for ranked lists-Revised Edition v1.0
#Stephen Talley
#Date started: January 17, 2015
import csv
import getopt, sys, itertools
try:
    import numpy as np
except ImportError:
    print "Cannot import numpy. Please install numpy and try again.\n"
try:
    import mlpy
except ImportError:
    print "Cannot import mlpy. Please install mlpy and try again.\n"
    
def Doc():#Function to display the help menu as needed
    print "Canberra Distance help menu:\n\n"
    print "Use -v or -verbose to trigger verbose mode.\n"
    print "Use -h or -help to access this menu.\n"
    print "Use -f or -inFile to specify the name of the input file (i.e. the file with the ranked lists).\n"
    print "Use -s or -inSep to set the delimiter on the input file.\n"
    print "Use -o or -outFile to set the desired name for your output file (e.g. My_Results).\n"
    print "Use -S or -outSep to set the desired delimiter on your outputfile.\n"
    
def GetArgs():#Collects the arguments for the program
    try:
        ops, args = getopt.getopt(sys.argv[1:],shortopts="vhf:s:o:S:", longopts=["verbose","help","inFile","inSep","outFile","outSep"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit()
    #Establish default values for arguments
    verbose=False
    inputsep="comma"
    outputsep="comma"
    outFile="Canberra_Results"
    #Loop through command line arguments to get file names and specifications
    for o, a in ops:
        if o in ("-v","verbose"):
            verbose=True
        elif o in ("-h","help"):
            if verbose:
                print "Loading help menu..."
            Doc()
        elif o in ("-f","-inFile"):
            inFile=str(a)
            if verbose:
                print "Input file to be analyzed is named", inFile
        elif o in ("-s","-inSep"):
            inputsep=str(a)
            if verbose:
                print "Input delimiter is set to", inputsep
        elif o in ("-o","-outFile"):
            outFile=str(a)
            if verbose:
                print "Output file name is specified as", outFile
        elif o in ("-S","-outSep"):
            outputsep=str(a)
            if verbose:
                print "Output delimiter is set to", outputsep
#Verify that the main required variable is actually defined
    try:
        inFile
    except NameError:
        print "No input file found! Input file required for analysis."
        Doc()
    return inFile, inputsep, outputsep, outFile, verbose
        
def GetData(inFile, inputsep): #Reads data from csv file and translates it into a multi-dimensional list
    List1=[]
    with open(inFile,mode='rb') as data:
        reader=csv.reader(data, delimiter=inputsep)
        for row in reader:
            seq=map(int, row) #Map, in this case, applies the 'int' operator to every element in the row
            List1.append(seq)
    reader=None
    return np.array(List1)
    
def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip(a, b)
    
def ChangeDelim(inputsep, outputsep): #Change the written names for delimiters/separators into actual delimiters
    if inputsep or outputsep not in ("comma", "whitespace", "tab"):
        print "Delimiter not an acceptable option."
    else:
        if inputsep=="comma":
            inputsep=','
        elif inputsep=="whitespace":
            inputsep=' '
        elif inputsep=='tab':
            inputsep='\t'
        if outputsep=="comma":
            outputsep=','
        elif outputsep=="whitespace":
            outputsep=' '
        elif inputsep=='tab':
            outputsep='\t'
    return inputsep, outputsep
    
def main(): 
    inName,inSep,outSep,outName,verbose=GetArgs()
    data = GetData(inName, inSep)
    inSep, outSep = ChangeDelim(inSep, outSep)
    with open(outName, outSep) as csvfile:
        out=csv.writer(csvfile)
        out.writerow("First List", "Second List","Distance")
        for x, y in pairwise(data):
            results=mlpy.canberra(x,y)
            out.writerow([data.index(x),data.index(y),results])
            if verbose:
                print "Writing to file...\n"
    print "\nCompleted. Check "+outName+" for results."     
        
if __name__=="__main__":
    main()
            
    
        
        
        
    
