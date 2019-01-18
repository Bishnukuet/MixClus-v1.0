
import sys
#===================================================================================
#Global variables
Input_file = ""


#Usage
usage = "python format_output_realdata.py -i Input_file  \n"

#===================================================================================
#Read parameters
def readParameters(args):
	global Input_file


	for i in range(1,len(args)):
		if (args[i] == "-i"):
			Input_file = args[i+1]
		elif (args[i] == "-h"):
			print usage
#===================================================================================
### Check parameters
def checkParameters():
	if (Input_file == ""):
		print "ERROR::Parameter -i Input_file is required\n"
		sys.exit(1);

#===================================================================================
def read_output_file(filename):
	f=open(filename,"r")
	lines=f.readlines()
	f.close()
	return lines

#===================================================================================
def dico_format(lines):
	Dico={}
	for l in range(0,len(lines)):
		V,J="_","_"
		split=lines[l].split("\t")
		if len(split)>5:
			if split[3] != "":
				V=split[3].split(" ")[1]
			if split[10] != "":
				J=split[9].split(" ")[1]
		Dico[split[1]]=[V,J]
	return Dico
#===================================================================================

#===================================================================================				
def write_file(dico):
	outputname=Input_file.split(".")[0]+"_VDJ.txt"
	f=open(outputname,"w")
	for key in dico.keys():
		line=key+"\t"+dico[key][0]+"\t"+dico[key][1]+"\n"
		f.write(line)
	f.close()
	return 0

#===================================================================================
#			    		Main
#===================================================================================
readParameters(sys.argv)
checkParameters()
lines=read_output_file(Input_file)
Dico= dico_format(lines)
write_file(Dico)