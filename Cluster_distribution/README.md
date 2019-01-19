
# Cluster distribution

**Command-line manual**

## About
Visualizing the sequence distribution into clones inferred by Mixclus.


# Input 

The main input file of Cluster_distribution.py are : 


Predicted_clusters_File which contains the output of Mixclus tool. This file has the following format :

``` diff
Cluster_number  seq_ID nucleotide_seq

```

Fasta_file which contains the sequences.

# Output

## Main output files

The outputs of Cluster_distribution.py are :

1- A png file containing different plots for visualizing the distribution of sequences into the clones.

2- A text file with the following format :
``` diff
Cluster_number  size of the cluster

Example :

Cluster number 1  0.50
```


## Usage

``` bash
$ python Cluster_distribution.py -f 30000.fa -c 30000_id_90.0.txt
   ```
