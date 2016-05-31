### Hypothesis Testing and ANOVA

I decided to examine the correlation between the total sulfur dioxide and the quality of wine. Firstly, I created a new column containing a quality mark of wine: *high* if `quality` rank is greater than or equal to `8`, *medium* if `quality` rank is equal to `6`or `7`, and *low* if `quality` rank is less than or equal to `5`. Then, an Analysis of Variance (ANOVA) was performed on both wine sets (red and white) separately.

The analysis of the red wine revealed that the total sulfur dioxide and the quality of wine are significantly associated, `F(2, 1596) = 45.71, p = 4.97e-20`. Post hoc comparisons of mean total sulfur dioxide of the wine by pairs of its quality marks revealed that the *low* quality wine has significantly different (higher) amount of total sulfur dioxide than has the wine in the other groups. On the other hand, the *high* quality wine has the smallest mean amount of total sulfur dioxide compared to other groups, but not significanly different from the one in the *medium* group. 

Similarly, the analysis of the white wine revealed that the total sulfur dioxide and the quality of wine are significantly associated, `F(2, 4895) = 76.66, p = 1.65e-33`. Post hoc comparisons of mean total sulfur dioxide of the wine by pairs of its quality marks revealed that all three groups have significantly different amount of total sulfur dioxide. In particular, the *low* quality wine has the highers amount of total sulfur dioxide, and the *high* quality wine - the lowest.

There are the [code](https://github.com/ekolik/-Python-Ahalysis_of_wine_quality/blob/master/data_analysis.py) and its [output](https://github.com/ekolik/-Python-Ahalysis_of_wine_quality/blob/master/data_analysis_output.txt) that are created at this point.
