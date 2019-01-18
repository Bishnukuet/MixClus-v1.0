from collections import Counter
#===================================================================================
def read_output_file(filename):
	f=open(filename,"r")
	lines=f.readlines()
	f.close()
	return lines

#===================================================================================
def dico_format(lines):
	Dico_first={}
	for l in range(0,len(lines)):
		split=lines[l].split("\t")
		if split[0] in Dico_first.keys():
			Dico_first[split[0] ][0].append(split[1].split("|")[1])
			Dico_first[split[0] ][0].append(split[1].split("|")[3])
				
		else:
			Dico_first[split[0]]=[[split[1].split("|")[1]],[split[1].split("|")[3]]]
	return Dico_first
#===================================================================================
lines=read_output_file("30000_id_97.0.txt")
dico=dico_format(lines)
listloc=[]
for key in dico:

	if len(set(dico[key][0])) != 1:
		dico1=dict( Counter(dico[key][0]))
		maximum = max(dico1, key=dico1.get)
		final=(sum(dico1.values())-dico1[maximum])/float(sum(dico1.values()))
		listloc.append( final)
		dico2=dict( Counter(dico[key][1]))
		maximum = max(dico2, key=dico2.get)
		final2=(sum(dico2.values())-dico2[maximum])/float(sum(dico2.values()))
		listloc.append( final2)
	else:
		listloc.append(1)
		listloc.append(1)
#===================================================================================
print 1-(sum(listloc) / float(len(listloc)))
