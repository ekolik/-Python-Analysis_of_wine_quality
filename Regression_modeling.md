There are the [code](https://github.com/ekolik/-Python-Ahalysis_of_wine_quality/blob/master/regression_modeling.py) and its [output](https://github.com/ekolik/-Python-Ahalysis_of_wine_quality/blob/master/regression_modeling_output.txt) that cover all the steps described in this section.

### Basics of Linear Regression

Here I test the association between the amount of volatile acidity in wine and the quality of wine by building a simple linear regression model with one explanatory variable (the amount of volatile acidity). I do it for both wine sets (red and white) separately.

The scatter-plots reveal negative association between the variables for both wine sets: with the increase in the amount of volatile acidity the quality of wine tends to decrease.

**Red wine**:
![](https://github.com/ekolik/-Python-Ahalysis_of_wine_quality/blob/master/red_vacid_vs_quality.png)

**White wine**:
![](https://github.com/ekolik/-Python-Ahalysis_of_wine_quality/blob/master/white_vacid_vs_quality.png)

Before testing a linear regression model, the explanatory variable (volatile acidity) was centered by subtracting its mean from each observed value. It is interesting to note, that the mean of the volatile acidity is different for each wine set: for the red wine it is `0.53` and for the white wine - `0.28`. 

The results of the regression modeling for the red wine tell us that the model was constructed using `1599` observations, the R-squared number is `0.153` (in other words, 2.3% of the variability in the quality of wine is described by variation in the amount of volatile acidity in it), F = `287.4` with p = `2.05e-59` (which mean that the variables are significantly associated). The regression coefficients of the model are: intercept = `5.6360` and slope = `-1.7614`, which means that we can relate our variables by the formula: <br /> `quality = 5.6360 - 1.7614*volatile acidity`.

The results of the regression modeling for the white wine tell us that the model was constructed using `4898` observations, the R-squared number is `0.038` (in other words, 0.1% of the variability in the quality of wine is described by variation in the amount of volatile acidity in it), F = `193.0` with p = `4.67e-43` (which mean that the variables are significantly associated). The regression coefficients of the model are: intercept = `5.8779` and slope = `-1.7109`, which means that we can relate our variables by the formula: <br /> `quality = 5.8779 - 1.7109*volatile acidity`.

We can see that the formulas are very similar for both wine sets. That is, the relationship between the amount of volatile acidity in wine and the quality of wine is almost the same for the red and white wines, even though the mean of the amount of volatile acidity in the red wine is different (bigger) than the one in the white wine.

### Multiple Regression

Here, using multivariate regression, I examine which characteristics of wine are the most influential on the wine's quality. After running the multivariate regression with all explanatory variables in a wine set, I've selected those variables that are significantly associated (p-value smaller than `0.05`) with the quality of wine (response variable) after controlling for other variables and also have the regression coefficient greater than `0.1`. Then, I reran the multivariate regression with these selected variables. I performed this procedure separately on both wine sets (red and white).

As usually, before testing any regression model I centered the explanatory variables by subtracting their means from each observed value. 

The results of the multivariate regression for the **red** wine showed that the most influential variables in describing the quality of wine are: volatile_acidity (coefficient = `-1.0687`), chlorides (`-1.9288`), pH (`-0.4173`), sulphates (`0.8474`), and alcohol (`0.3055`). All variables have p-values = `0`. The model was constructed using `1599` observations; the R-squared number is `0.346` (in other words, 12% of the variability in the quality of wine is described by variation in the selected variables), F = `170.3` with p = `2.66e-145` (which mean that the explanatory and response variables are significantly associated). The intercept of the model is `5.6360`. In other words, all characteristics equal, the quality of red wine would be around 5.6. Sulphates and alcohol are positively associated with the wine quality, while volatile acidity, chlorides, and pH - negatively. To check the quality of the model, I create the following diagnostic plots:

* The Q-Q plot shows that the residuals follow the fit line in the middle, but slightly deviate at the lower and higher quantiles. This indicated that the residuals do not follow normal distribution perfectly. For the improvement of the model, other explanatory variables might be considered.
![](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/red_multi_q_q_.png)

* The plot of residuals again shows that less than 5% of the observations have standardized residuals with an absolute value bigger than 2. Nonetheless, there are still quite a few observations with residuals out of these boundaries. Again, that means that the quality of the model might be improved. ![](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/red_multi_resud.png)

* The leverage plot shows that quite a few observations are outliers (they have residuals greater than 2 or less than -2), but almost all of them have small leverage values, and, therefore, they don't have an undue influence on the estimation of the regression model. Also, there are several cases with higher than average leverage; in particular, there are observation (marked `92` and `151`) that are both outliers and have high leverages, and they might be very dramatic in their undue influence on the estimation. 
![](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/red_multi_leverage.png)

The results of the multivariate regression for the **white** wine showed that the most influential variables in describing the quality of wine are: volatile_acidity (coefficient = `-2.0437`, p-value = `0`), density (`36.8919`, `0`), pH (`0.1822`, `0.014`), sulphates (`0.3162`, `0.001`), and alcohol (`0.3925`, `0`). The model was constructed using `4898` observations; the R-squared number is `0.250` (in other words, 6.25% of the variability in the quality of wine is described by variation in the selected variables), F = `325.9` with p = `4.08e-302` (which mean that the explanatory and response variables are significantly associated). The intercept of the model is `5.8779`. In other words, all characteristics equal, the quality of red wine would be around 5.9. Density, pH, sulphates, and alcohol are positively associated with the wine quality, while volatile acidity - negatively. To check the quality of the model, I create the following diagnostic plots:

* The Q-Q plot shows that the residuals follow the fit line in the middle, but highly deviate at the lower and higher quantiles. This indicated that the residuals do not follow normal distribution perfectly. For the improvement of the model, other explanatory variables might be considered.
![](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/white_multi_q_q_.png)

* The plot of residuals again shows that less than 5% of the observations have standardized residuals with an absolute value bigger than 2. Nonetheless, there are still quite a few observations with residuals out of these boundaries. Again, that means that the quality of the model might be improved. ![](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/white_multi_resud.png)

* The leverage plot shows that quite a few observations are outliers (they have residuals greater than 2 or less than -2), but all of them have small leverage values, and, therefore, they don't have an undue influence on the estimation of the regression model. There is only one sample with higher than average leverage (marked `2781`), but, not being an outlier, it influences the estimation correctly. 
![](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/white_multi_leverage.png)

To sum up the results of the multiple regression modeling, the following observations are made:
* The intercept of the white wine model is higher than the one of the red wine model, which means that if to equal all the explanatory variables, the white wine would have higher quality.
* Density is the most influential variable (has dramatically high coefficient) in describing the quality of the white wine, but not influential for the red wine.
* Sulphates and alcohol are positively associated with the quality of both red and white wines; however, the regression coefficients of these variables are less than `1`.
* pH is positively associated with the quality of the white wine, but negatively - of the red (absolute values of the coefficients for both wine sets are less than `1`).
* Volatile acidity is negatively associated with the quality of both wine sets, with the regression coefficients less than `-1`.
* Chlorides is the most influential variable (has the lowest negative coefficient) in negative association with the quality of the red wine, but not influential for the white wine.
* Fixed acidity, citric acid, residual sugar, free sulfur dioxide, and total sulfur dioxide are variables not significantly associated with the quality of both wines.

### Logistic Regression

Here I examine the association between the amount of sulphates and alcohol in wine (the explanatory variables), and the quality of wine (the response variable) from a perspective of logistic regression. For that, I recode the explanatory and response variables into binary categorical values. I perform the recoding using the following rules: 
* *categorical quality*: `0` - if the quality of a wine sample is 3, 4, 5, or 6, `1` - if 7, 8, or 9;
* *categorical sulphates*: `0` - if the amount of sulphates in a wine sample is lower that the mean amount of sulphates in all samples, `1` - if higher;
* *categorical alcohol*: `0` - if the amount of alcohol in a wine sample is lower that the mean amount of alcohol in all samples, `1` - if higher.

After recoding the variables I train the logistic regression model and calculate the confidence intervals for the explanatory variables. I perform this procedure separately on both wine sets (red and white).

The results of the logistic regression model for the **red** wine tell us that both of the explanatory variables are positively and significantly (both p-values = 0) associated with the response variable. None of these variables is a confounder. We can say that, after adjusting for the *sulphates* variable, wine samples with higher than the mean amount of alcohol are 9.26 times more likely to have high (>= 7) quality mark (`Odds ratio = 9.263534, 95% CI = [6.129303, 14.000459]`). Similarly, after adjusting for the *alcohol* variable, wine samples with higher than the mean amount of sulphates are 3.99 times more likely to have high (>= 7) quality mark (`Odds ratio = 3.992948, 95% CI = [2.843148, 5.607741]`).

The results of the logistic regression model for the **white** wine tell us that both of the explanatory variables are positively and significantly (sulphates p-value = 0.007, alcohol p-value = 0) associated with the response variable. None of these variables is a confounder. We can say that, after adjusting for the *sulphates* variable, wine samples with higher than the mean amount of alcohol are 6.00 times more likely to have high (>= 7) quality mark (`Odds ratio = 6.003765, 95% CI = [5.131542, 7.024243]`). Similarly, after adjusting for the *alcohol* variable, wine samples with higher than the mean amount of sulphates are 1.22 times more likely to have high (>= 7) quality mark (`Odds ratio = 1.220176, 95% CI = [1.054847, 1.411418]`).

Therefore, the results show that, for both wines, the sulphates and alcohol variables are positively associated with the quality variable. Moreover, for both wines, the alcohol variable is stronger associated with the quality variable since it has higher regression coefficient and odds ratio than the sulphates variable.

The work is continued in the [Machine Learning](https://github.com/ekolik/-Python-Analysis_of_wine_quality/blob/master/Machine_learning.md) section.
