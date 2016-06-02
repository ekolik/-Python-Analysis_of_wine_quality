There are the [code](https://github.com/ekolik/-Python-Ahalysis_of_wine_quality/blob/master/data_analysis.py) and its [output](https://github.com/ekolik/-Python-Ahalysis_of_wine_quality/blob/master/data_analysis_output.txt) that cover all the steps described in this section.

### Hypothesis Testing and ANOVA

I decided to examine the correlation between the total sulfur dioxide and the quality of wine. Firstly, I created a new column containing a quality mark of wine: *high* if `quality` rank is greater than or equal to `8`, *medium* if `quality` rank is equal to `6`or `7`, and *low* if `quality` rank is less than or equal to `5`. Then, an Analysis of Variance (ANOVA) was performed on both wine sets (red and white) separately.

The analysis of the red wine revealed that the total sulfur dioxide and the quality of wine are significantly associated, `F(2, 1596) = 45.71, p = 4.97e-20`. Post hoc comparisons of mean total sulfur dioxide of the wine by pairs of its quality marks revealed that the *low* quality wine has significantly different (higher) amount of total sulfur dioxide than has the wine in the other groups. On the other hand, the *high* quality wine has the smallest mean amount of total sulfur dioxide compared to other groups, but not significanly different from the one in the *medium* group. 

Similarly, the analysis of the white wine revealed that the total sulfur dioxide and the quality of wine are significantly associated, `F(2, 4895) = 76.66, p = 1.65e-33`. Post hoc comparisons of mean total sulfur dioxide of the wine by pairs of its quality marks revealed that all three groups have significantly different amount of total sulfur dioxide. In particular, the *low* quality wine has the highers amount of total sulfur dioxide, and the *high* quality wine - the lowest.

### Pearson Correlation

Here I examine the association between the density of wine and the amount of residual sugar the wine contains. For that, I calculate a Pearson correlation coefficient for these variables (`density` is the quantitative explanatory variable and `residual sugar` is quantitative response variable) on each wine set separately. The coefficient for the red wine: `r = 0.355, p-value = 9.0e-49`. The coefficient for the white wine: `r = 0.839, p-value = 0.0`. In other words, the coefficients show that there is a positive linear relationship between these variables for both wine sets; however, for the white wine this relationship is stronger. In addition, it can be assumed that the percent of the variability in the amount of residual sugar in wine is described by variation in the wine's density for the red wine is equal to 12.6% and for the white - 70.4% (using `RSquared or Coefficient of Determination: 0.355² = 0.126` and `0.839² = 0.704` respectively). For the white wine, this number is quite impressive. In other words, it means that the amount of sugar is strongly connected to the wine density.

In addition, I make scatter-plots of these variables to check the linearity of the relationship. 

**Red wine**:
![](https://github.com/ekolik/-Python-Ahalysis_of_wine_quality/blob/master/red_sugar_vs_density.png)

**White wine**:
![](https://github.com/ekolik/-Python-Ahalysis_of_wine_quality/blob/master/white_sugar_vs_density.png)

Both plots show somewhat positive but not linear correlation. In fact, the red wine set has too many "outliers" from the linear pattern, and the samples in the white wine set form a "blob", not a line.
