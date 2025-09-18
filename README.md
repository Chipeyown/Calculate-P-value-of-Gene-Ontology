# Calculate-P-value-of-Gene-Ontology
Calculate P value of Gene Ontology

ATH_GO_GOSLIM.txt from https://www.arabidopsis.org/download/file?path=GO_and_PO_Annotations/Gene_Ontology_Annotations/ATH_GO_GOSLIM.txt.gz
version: 2025-09-01

ATH_GO_BP.txt is generated from ATH_GO_GOSLIM.txt by using the follow screening:
1, Select biological process: Column 8 == P (P: Biological Process; F: Molecular Function; C: Cell Component);
2, Remove genes that not in ath.gtf annotation file;
3, Remove lines that GO annotation is 0008150.

