"""
Program for evaluate the clustring performance of different Rep-seq tools.
The calculated metrics are : Precision, recall, F-score and Specificity.
This evaluation if for simulated sequences for which we know the real clusters.
"""

import sys
# =============================================================================
#               evaluate Measures
# =============================================================================		
def evaluateMeasures(cluster, hashCluster, totalSeq):

	count = 0; tp = 0; sumTp = 0.0; sumFp = 0.0; sumFn = 0.0; sumTtC = 0; tn = 0; sumTn = 0.0;
	countSeq = 0

	for i in cluster:
		count +=1
		if (count % 5000 == 0): print "Processed ", count
		
		arraySeqIds = cluster[i]
		
		#find the majority label
		hashAux = {}; tp = 0;
		
		for j in arraySeqIds:
			IDmember = j.split("-")[0]

			countSeq += 1
			if IDmember.rstrip() in hashAux.keys():
				hashAux[IDmember.rstrip()] += 1
			else:
				hashAux[IDmember.rstrip()] = 1

		maxValue = 0; maxLabel = ""
		for d in hashAux:

			if hashAux[d.split("-")[0]] > maxValue:
				maxValue = hashAux[d.split("-")[0]]
				maxLabel = d.split("-")[0]

		for j in arraySeqIds:
			IDmember = j.split("-")[0]

			if IDmember !="" and IDmember == maxLabel:

				tp +=1

		totalCluster = hashCluster[maxLabel.rstrip()]

		sumTtC += totalCluster
		
		fn = totalCluster - tp
		if fn<0:
			print "erreur"
		fp = len(arraySeqIds) - tp
		tn = totalSeq -(tp+ fn +fp)
		sumTp += tp; sumFp += fp; sumFn += fn; sumTn += tn;
		#print (tp, fp, fn)
		
	print sumTp, sumFp, sumFn, sumTn
	
	pre = sumTp/(sumTp+ sumFp);
	rec = sumTp/(sumTp+ sumFn);
	spe = sumTn/(sumTn + sumFp)
	print ("Pre = ", pre, "Rec = ", rec , "specificity = ",spe,"F-score = ", 2*pre*rec/(pre + rec), "NumCluster = ", count, "NumSeqs = ", countSeq, " sumTtC = ", sumTtC)

	
# =============================================================================
#               Read cluster result formatted file
# =============================================================================	
def readResultFile(filename):
	cluster = {}; count = 0; totalSeq = 0;
	file = open(filename, "r")
	for line in file.readlines(): 
		count +=1
		if (count % 5000 == 0): print "Processed ", count
		IDcluster = line.split('\t')[0]
		members = line.split('\t')[1]
		if (members == "\n" or members == ""):
			print "Warnning:: Cluster ", IDcluster, " has no members"
		else: 
			arraySeqIds = members.split(" ")
			#print arraySeqIds
			if len(arraySeqIds[:-1]) != 0:
				cluster[IDcluster] = arraySeqIds[:-1]
				totalSeq += len(arraySeqIds)
	file.close()
	print "Cluster results\nTotal of clusters = ", count," Total sequences = " , totalSeq
	return  cluster,totalSeq
	
# =============================================================================
#               Read true cluster file
# =============================================================================	
def readTrueClusterFile(filename):
	hashCluster = {}; count = 0; countCluster = 0;
	file = open(filename, "r")
	for line in file.readlines(): 
		IDcluster = line.split('\n')[0].split("-")[0]
		if IDcluster in hashCluster.keys():
			hashCluster[IDcluster.rstrip()] +=1
		else:
			hashCluster[IDcluster.rstrip()] =1
	file.close()
	return  hashCluster


#=============================================================================#
def main():
    usage = "python  evaluateSimCluster.py -p <clustering output> -tc <true cluster file>\n "
    parser = OptionParser(usage)
    parser.add_option("-p", "--Predicted_clusters_File", dest="Predicted_clusters_File",
          help="read clusters from Predicted_File")
    parser.add_option("-tc", "--True_clusters_file", dest="True_clusters_file",
          help="read data from True clusters file")
    
    (options, args) = parser.parse_args()
    if len(sys.argv) != 5:
        parser.error("incorrect number of arguments")
    
    Predicted_File = options.Predicted_clusters_File
    True_file = options.True_clusters_file
    cluster,totalSeq = readResultFile(Predicted_File)
	hashCluster = readTrueClusterFile(True_file)
	evaluateMeasures(cluster, hashCluster, totalSeq)

#=============================================================================#
if __name__ == "__main__":
    main()