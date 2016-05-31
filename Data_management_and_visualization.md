### Data management and visualization

As the first step in the project, I download the data sets and examine the data. 

Firstly, I checked that there are no missing data in any variable in both sets. Secondly, I found it interesting to explore the frequency distribution of the wines' quality. For both wines, the majority of the samples have quality ranks `5`, `6`, and `7` (on the `0`-`10` scale). There are no samples ranked `0`, `1`, `2`, or `10`. However, the quality ranks of the white samples on average are higher the those of the reds. In addition, the following countplots were created to visualize the distribution of quality ranks for both wines. 

![](https://github.com/ekolik/-Python-Ahalysis_of_wine_quality/blob/master/red_quality_counts.png)
![](https://github.com/ekolik/-Python-Ahalysis_of_wine_quality/blob/master/white_quality_counts.png)

To examine the data a little further, I've created the factorplots that show the alcohol levels of wine samples in each quality rank. Here we can notice not very strong, but positive correlation of the alcohol level and quality rank for both wines: the higher the rank, the higher the alcohol level.

![](https://github.com/ekolik/-Python-Ahalysis_of_wine_quality/blob/master/red_alco_per_quality.png)
![](https://github.com/ekolik/-Python-Ahalysis_of_wine_quality/blob/master/white_alco_per_quality.png)


There are the [code](https://github.com/ekolik/-Python-Ahalysis_of_wine_quality/blob/master/data_manag%26visualization.py) and its [output](https://github.com/ekolik/-Python-Ahalysis_of_wine_quality/blob/master/data_manag_output.txt) for this step in the project. 

The work is continued in the [Data analysis](https://github.com/ekolik/-Python-Ahalysis_of_wine_quality/blob/master/Data_analysis.md) section.
