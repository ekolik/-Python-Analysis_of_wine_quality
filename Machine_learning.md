There are the [code](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/machine_learning.py) and its [output](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/machine_learning_output.txt) that cover all the steps described in this section.

### Decision Trees

I perform decision tree analysis to test nonlinear relationships among a set of explanatory variables (amount of residual sugar and alcohol in wine) and a binary, categorical response variable (`0` - if the quality of a wine sample is 3, 4, or 5, `1` - if 6, 7, 8, or 9). All possible cut points (for explanatory variables) are tested. For the present analysis, the entropy “goodness of split” criterion was used to grow the tree and a cost complexity algorithm was used for pruning the full tree into a final subtree. A classification tree was build for each of the wine sets (red and white) separately. In each set, 60% of the samples were used for the training, and 40% - for testing. 

The accuracy of the resulted tree for the red wine is `0.65`. The confusion matrix is:
 
 `[198  105]`

 `[120  217]`

The accuracy of the resulted tree for the white wine is `0.72`. The confusion matrix is:
 
 `[404  262]`

 `[290  1004]`
 
 The resulted trees are too big to be examined and visualized. It might indicate that the selected variables are not suitable for proper tree formation, or that the tree analysis is not suitable for these data. The work on this problem is continued in the next paragraph.
