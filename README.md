# Mutual Funds Time Series Analysis and Clustering


### Instructions 
1. Run `sax_open_prices.py` to get a file `sax_words_ri_norot_w=$_a=#.txt`
2. Execute `show_CM.py` to obtain a file `CM_w=$_a=#_lsh_limit=@.txt`.
3. Execute Hcluster_my_idea.py to obtain the clusters in `./CLusters/nested_clusters_15_average_w=$_a=#_lsh_limit=@.txt`. A dendrogram will also be obtained.
4. From `nested_clusters_15_average_w=$_a=#_lsh_limit=@.txt` obtain the indices to plot and create a new file in the working directory named as `to_plot_15_average_w=$_a=#_lsh_limit=@`. These indices will be obtained by copying the contents of the cluster file into the excel sheet (column A) and then copying the resukts in column B.
5. Finally generate a comparison plot by running gen_subplots.py.

## Plotting and getting analysis

### Generate comparative subplots for algorithm results
TO generate a subplot comparing the results obtained from the algorithm, use the `gen_subplot.py` script.
A UI based tool has also
### For Specific Stocks
To view trends for specific stock tickers (by viewing their time-series) use the `csv_price_plot.py` script.

## Results and Example Plots

![Clusters obtained with `w=8` and `k=3` named as a,b,c,...m from left to right, top to bottom](https://github.com/atishayjain708/TS_MF_cluster_analysis/blob/results/Plots/diff_znorm_comparison_nested_15_average_w%3D8_a%3D20_lsh_limit%3D3.png)Clusters obtained with `w=8` and `k=3` named as a,b,c,...m from left to right, top to bottom
![Clusters obtained with `w=4` and `k=3` named as a,b,c,...m from left to right, top to bottom](https://github.com/atishayjain708/TS_MF_cluster_analysis/blob/results/Plots/diff_znorm_comparison_nested_15_average_w%3D4_a%3D20_lsh_limit%3D3.png)Clusters obtained with `w=4` and `k=3` named as a,b,c,...m from left to right, top to bottom
![Clusters obtained with `w=4` and `k=6` named as a,b,c,...m from left to right, top to bottom](https://github.com/atishayjain708/TS_MF_cluster_analysis/blob/results/Plots/diff_znorm_comparison_nested_15_average_w%3D4_a%3D20_lsh_limit%3D6.png)Clusters obtained with `w=4` and `k=6` named as a,b,c,...m from left to right, top to bottom
![Clusters obtained with `w=8` and `k=6` named as a,b,c,...m from left to right, top to bottom](https://github.com/atishayjain708/TS_MF_cluster_analysis/blob/results/Plots/diff_znorm_comparison_nested_15_average_w%3D8_a%3D20_lsh_limit%3D6.png)Clusters obtained with `w=8` and `k=6` named as a,b,c,...m from left to right, top to bottom

<!-- | w | a | lsh_limit | Resulting plot
| ------------------------- | ------------------------- | ------------------------- |
| ArrowHead_TRAIN | ![](https://github.com/atishayjain708/TS_MF_cluster_analysis/blob/results/Plots/diff_znorm_comparison_nested_15_average_w%3D8_a%3D20_lsh_limit%3D3.png) |
| Butterfly_A | ![](https://github.com/atishayjain708/shape-discord-identification/blob/results/Plots/Butterfly_A_all.png) | ![](https://github.com/atishayjain708/shape-discord-identification/blob/results/Plots/Butterfly_A_31.png) |
 -->
**NOTE: The various parameters (w,k,lsh_limit) can be varied by changing the respective values in the code files. $,# and @ have been used as placeholder in this guide for w,k and lsh_limit respectively.**

diff_znorm_comparison_nested_15_average_w_8_a_20_lsh_limit_6.png