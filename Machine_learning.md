There are the [code](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/machine_learning.py) and its [output](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/machine_learning_output.txt) that cover all the steps described in this section.

### Decision Trees

I perform decision tree analysis to test nonlinear relationships among a set of explanatory variables (amount of residual sugar and alcohol in wine) and a binary, categorical response variable (`0` - if the quality of a wine sample is 3, 4, or 5, `1` - if 6, 7, 8, or 9). All possible cut points (for explanatory variables) are tested. For the present analysis, the entropy “goodness of split” criterion was used to grow the tree and a cost complexity algorithm was used for pruning the full tree into a final subtree. A classification tree was build for each of the wine sets (red and white) separately. In each set, 60% of the samples were used for the training, and 40% - for testing. 

The accuracy of the resulted tree for the **red** wine is `0.65`. The confusion matrix is:
 
 `[198  105]`

 `[120  217]`

The accuracy of the resulted tree for the **white** wine is `0.72`. The confusion matrix is:
 
 `[404  262]`

 `[290  1004]`
 
 The resulted trees are too big to be examined and visualized. It might indicate that the selected variables are not suitable for proper tree formation, or that the tree analysis is not suitable for these data. The work on this problem is continued in the next paragraph.
 
 
### Random Forests

Here I perform random forest analysis to evaluate the importance of all the explanatory variables in predicting the quality of wine (binary target variable: `0` - if the quality of a wine sample is 3, 4, or 5, `1` - if 6, 7, 8, or 9). Analysis was performed for each wine set (red and white) separately. In each set, 60% of the sample were used for the training, and 40% - for testing. 

The analysis consists of two steps. Firstly, I create the random forest model with `25` trees and examine its results. Secondly, I train random forests with different numbers of trees (1-100) to see the effect of the number on the accuracy of the prediction.

The [results](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/machine_learning_output.txt) of the random forest model with `25` trees for the **red** wine show that the accuracy of the prediction is `0.778` and the most important predictor is `alcohol`, followed by `volatile acidity`, `sulphates`, and `total sulfur dioxide`. It is interesting to note that the results of the *multivariate regression* for the **red** wine mark different set of variables (`chlorides`, `volatile acidity`, `sulphates`, and `pH`) as the most influential variables in describing the quality of wine.

The [results](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/machine_learning_output.txt) of the random forest model with `25` trees for the **white** wine show that the accuracy of the prediction is `0.816` and the most important predictor is `alcohol`, followed by `volatile acidity`, and `density`. It is interesting to notice that the results of the *multivariate regression* for the **white** wine mark the same set of variables (`alcohol`, `volatile acidity`, and `density`) as the most influential variables in describing the quality of wine.

Training random forests with different numbers of trees (1-100) shows that, after approximately 20 trees, the subsequent growing of number of trees adds little to the overall accuracy of the forest. It is true for both sets of wine: red and white.

**Red** wine:
![](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/red_random_forests.png)

**White** wine:
![](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/white_random_forests.png)


### Lasso Regression

A lasso regression analysis was conducted to identify a subset of wine characteristics (predictor variables) that are best in predicting wine quality (quantitative response variable). All wine characteristics were included as the predictor variables; they are quantitative and were standardized to have a mean of zero and a standard deviation of one.

Data were randomly split into a training set (70% of the observations) and a test set (30%). The least angle regression algorithm with k=10 fold cross validation was used to estimate the lasso regression model in the training set, and the model was validated using the test set. The change in the cross validation mean squared error at each step was used to identify the best subset of predictor variables.

**Red** wine:
![](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/red_lasso_coef-vs-alph.png)
![](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/red_lasso_mse-vs-alph.png)

**White** wine:
![](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/white_lasso_coef-vs-alph.png)
![](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/white_lasso_mse-vs-alph.png)

Not all predictor variables were retained in the selected models. For the red wine, `citric acid`, `fixed acidity`, and `free sulfur dioxide` variables received zero coefficients, and therefore do not participate in the prediction. The results of the training indicate the `alcohol`, `volatile acidity`, and `sulphates` variables as the most strongly associated with the quality of wine and, therefore, the most influential for the prediction. Interestingly, this results differ from the ones of [random forests analysis](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/Machine_learning.md#random-forests) and [multivariate regression](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/Regression_modeling.md#multiple-regression). Mean squared error and R-squared values prove the model being robust for testing on new examples. The predictors account for 33% of the variance in the target variable.

For the white wine, `citric acid` and `fixed acidity` variables received zero coefficients, and therefore do not participate in the prediction. The results of the training indicate the `alcohol`, `residual sugar`, `density`, and `volatile acidity` variables as the most strongly associated with the quality of wine and, therefore, the most influential for the prediction. Interestingly, this results similar to the ones of [random forests analysis](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/Machine_learning.md#random-forests) and [multivariate regression](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/Regression_modeling.md#multiple-regression). Mean squared error and R-squared values prove the model being robust for testing on new examples. The predictors account for 28% of the variance in the target variable.

We can see that for the white wine the predictive algorithms are more unanimous in the selection of most influential predictors than they are for red.

### K-Means Cluster Analysis

A K-means cluster analysis was conducted to identify underlying subgroups of wine samples based on their characteristics (quantitative clustering variables): density, alcohol, sulphates, pH, volatile acidity, chlorides, fixed acidity,
citric acid, residual sugar, free sulfur dioxide, and total sulfur dioxide (i.e., all available characteristics, expect the wine quality). Analysis was performed for each wine set (red and white) separately. All the variables were standardized to have a mean of 0 and a standard deviation of 1.

Data were randomly split into a training set (70%) and a test set (30% of the observations). A series of k-means cluster analyses were conducted on the training set specifying k=1-9 clusters, using Euclidean distance. The average distance from observations to the cluster centroids was plotted for each of the nine cluster solutions in an elbow curve to provide guidance for choosing the number of clusters to interpret.

**Red** wine:
![](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/red_kmeans_elbow.png)

**White** wine:
![](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/white_kmeans_elbow.png)

The elbow curves for both wine sets were inconclusive, suggesting that the 2, 3, 5, and 7-cluster solutions might be interpreted. To choose the best solution, canonical discriminant analyses were further performed for each solution.

Canonical discriminant analysis reduces the 11 clustering variables down to 2 canonical variables that account for most of the variance in the clustering variables. After plotting the canonical variables for each 1-9 cluster solution, the 2-cluster solution was chosen as the one that splits the data in the best way. For the white wine, the plot for 2-cluster solution indicates that the observations in the clusters are densely packed with relatively low within cluster variances, and the clusters don't overlap with each other. For the red wine, the observations in each of the 2 clusters have greater spread suggesting higher within cluster variance, but the clusters also don't overlap with each other.

**Red** wine:
![](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/red_2clusters.png)

**White** wine:
![](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/white_2clusters.png)

For the red wine, the means of the clustering variables show that, the samples in the first cluster, on average, have higher values of pH, volatile acidity, free sulfur dioxide, and total sulfur dioxide than the samples in the second cluster. Mean values of all other clustering variables in the first cluster are lower than in the second. 

For the white wine, the means of the clustering variables show that, the samples in the first cluster, on average, have higher values of alcohol and pH than the samples in the second cluster. Mean values of all other clustering variables in the first cluster are lower than in the second. 

In order to externally validate the clusters, an Analysis of Variance (ANOVA) was conducted to test for significant differences between the clusters on the quality of wine:
* For the red wine, results indicated significant differences between the clusters on the wine quality (`F(1, 1117) = 61.10, p = 1.25e-14`). The Tukey post hoc comparisons also showed significant differences between two clusters on the wine quality. Samples in the first cluster have lower quality (`mean = 5.502833, std = 0.746143`) than the samples in the second cluster (`mean = 5.886199, std = 0.864133`).
* For the white wine, results also indicated significant differences between the clusters on the wine quality (`F(1, 3426) = 219.8, p = 3.08e-48`). The Tukey post hoc comparisons also showed significant differences between two clusters on the wine quality. Samples in the first cluster have higher quality (`mean = 6.057617, std = 0.924930`) than the samples in the second cluster (`mean = 5.610145, std = 0.772186`).


