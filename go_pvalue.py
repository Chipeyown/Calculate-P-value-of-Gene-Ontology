import pandas as pd
from scipy import stats
import numpy as np

df=pd.read_csv('ATH_GO_BP.txt',sep='\t',header=None)#1,Select biological process; 2,Remove genes that not in ath10.gtf annotation file; 3,remove lines that GO is 0008150.
tmp=df.drop_duplicates(0)
N_genes=[e for e in tmp[0]]
N=tmp.shape[0]#Number of genes related to overall biological process in the genome

df=df[[0,5]]
df=df.drop_duplicates()
lib={}#genes related to a specific biological process in the genome. key: GO term, value: gene id list
for i in range(df.shape[0]):
    key=df.iloc[i,1]
    try:
        lib[key].append(df.iloc[i,0])
    except:
        lib[key]=[df.iloc[i,0]]

M_lib={}#The number of genes related to a specific biological process in the genome
for key,value in lib.items():
    M_lib[key]=len(value)

df2=pd.read_csv('upregulated_gene.data',sep='\t')
df2=df2.drop_duplicates('gene_id')
genes=[e for e in df2['gene_id'] if e in N_genes]
n=len(genes)#Number of upregulated genes related to overall biological process in the genome

k_genes={}#Upregulated genes related to a specific biological process in the genome. key: GO term, value: gene id list
k_lib={}#The number of upregulated genes related to a specific biological process in the genome
for key,value in lib.items():
    s=[e for e in genes if e in value]
    k_genes[key]=s
    k_lib[key]=len(s)

fa=open('pvalue.txt','w')
fa.write('GO\t-log10(pvalue)\tgenes\n')
for key,value in k_lib.items():
    if value==0:
        continue
    p=stats.hypergeom.pmf(value, N, M_lib[key], n)
    fa.write(key+'\t'+str(-np.log10(p))+'\t'+','.join(k_genes[key])+'\n')
fa.close()

df=pd.read_csv('pvalue.txt',sep='\t')
df=df.sort_values('-log10(pvalue)',ascending=False)
df.to_csv('pvalue.txt',sep='\t',index=None)
