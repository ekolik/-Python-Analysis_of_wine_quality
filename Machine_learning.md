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
