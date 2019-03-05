SAX
1. Run sax_open_prices.py to get a file sax_words_ri_norot_w=$_a=#.txt
2. Execute show_CM.py to obtain a file CM_w=$_a=#_lsh_limit=@.txt.
3. Execute Hcluster_my_idea.py to obtain the clusters in ./CLusters/nested_clusters_15_average_w=$_a=#_lsh_limit=@.txt. A dendrogram will also be obtained.
4. From nested_clusters_15_average_w=$_a=#_lsh_limit=@.txt obtain the indices to plot and create a new file in the working directory named as 'to_plot_15_average_w=$_a=#_lsh_limit=@'. These indices will be obtained by copying the contents of the cluster file into the excel sheet (column A) and then copying the resukts in column B.
5. Finally generate a comparison plot by running gen_subplots.py.

NOTES: The various parameters (w,k,lsh_limit) can be varied by changing the respective values in the code files. $,# and @ have been used as placeholder in this guide for w,k and lsh_limit respectively.