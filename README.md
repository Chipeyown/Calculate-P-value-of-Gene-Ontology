# Calculate-P-value-of-Gene-Ontology
Calculate P value of Gene Ontology
p value is calculated using hypergeometric distribution model (https://en.wikipedia.org/wiki/Hypergeometric_distribution)
The calculation is implemented by scipy.stats.hypergeom.pmf package.
pvalue = scipy.stats.hypergeom.pmf(k, N, M, n)


files:

ATH_GO_GOSLIM.txt from https://www.arabidopsis.org/download/file?path=GO_and_PO_Annotations/Gene_Ontology_Annotations/ATH_GO_GOSLIM.txt.gz
version: 2025-09-01

ATH_GO_BP.txt is generated from ATH_GO_GOSLIM.txt by using the follow screening:
1, Select biological process: Column 8 == P (P: Biological Process; F: Molecular Function; C: Cell Component);
2, Remove genes that not in ath.gtf annotation file;
3, Remove lines that GO annotation is 0008150.

upregulated_gene.txt； example data

ath.gtf: ath.gtf annotation file download from enzemle plant

pvalue.txt: result of example data

go_pvalue.py: script for calculate p value of selected genes.
