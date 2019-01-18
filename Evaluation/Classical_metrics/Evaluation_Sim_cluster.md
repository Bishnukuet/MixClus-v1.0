# Evaluation of clustering tool on simulated data 
**Command-line manual**

## Data

We have simulated 619 clones via IG simulator: two significant clones (46% and 39%), 
four minor clones (between 0.1 and 0.5%) and 613 clones forming
polyclonal backgrounds. The simulated dataset contains 464 928 sequences.




# Input 

The main input files of Evaluate_Sim_cluster.py are: 

Predicted_clusters_File which contains the output of clustring tool. This file should have the folowing format :

``` diff
Cluster_number	seq1 seq2 seq3,...

Example :

1	S483-12 S483-9 S483-3 
```

True_clusters_file which contains the real cluster to which each sequence belongs. This file should have the folowing format :

``` diff
Real cluster of seq1
Real cluster of seq2

Example :

S10-1
S10-2
S10-3
```
for S10-1, S10 is the cluster Id and 1 is the sequence ID.



# Output

## Main output files

The  output of Evaluate_Sim_cluster.py are the values of precision, recall, F-score and Specificity:

``` diff
Pre = 0.99  , Rec = 0.87 , specificity = 0.99 ,F-score = 0.92 , NumCluster = 622  , NumSeqs = 466153 
```

## Usage

``` bash
$ python Evaluate_Sim_cluster.py -p 400000_simu_changeO_predict.txt  -tc 400000_TrueSeq.txt

   ```

