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
    sys.exit()
try:
    import mlpy
except ImportError:
    print "Cannot import mlpy. Please install mlpy and try again.\n"
    sys.exit()
    
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
    for o in ops:
        if o[0] in ("-v","verbose"):
            verbose=True
    for o in ops:
        if o[0] in ("-h","help"):
            if verbose:
                print "Loading help menu..."
            Doc()
            sys.exit()
    for o in ops:
        if o[0] in ("-f","-inFile"):
            inFile=str(o[1])
            if verbose:
                print "Input file to be analyzed is named", inFile
        if o[0] in ("-s","-inSep"):
            inputsep=str(o[1])
            if verbose:
                print "Input delimiter is set to", inputsep
        if o[0] in ("-o","-outFile"):
            outFile=str(o[1])
            if verbose:
                print "Output file name is specified as", outFile
        if o[0] in ("-S","-outSep"):
            outputsep=str(o[1])
            if verbose:
                print "Output delimiter is set to", outputsep
#Verify that the main required variable is actually defined
    try:
        inFile
    except NameError:
        print "No input file found! Input file required for analysis."
        Doc()
        sys.exit()
    return inFile, inputsep, outputsep, outFile, verbose
        
def GetData(inFile, inputsep): #Reads data from csv file and translates it into a multi-dimensional list
    List1=[]
    with open(inFile,mode='rb') as data:
        if inputsep=='comma':
            reader=csv.reader(data, delimiter=',')
        else:
            reader=csv.reader(data, delimiter=' ')
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
    with open(outName, 'wb') as csvfile:
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
            
    
        
        
        
    
