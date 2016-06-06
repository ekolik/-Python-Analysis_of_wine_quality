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

We can see that the formulas are very similar for both wine sets. That is, the relationship between the amount of volatile acidity in wine and the quality of wine is almost the same for the red and white wines, even though the mean of the amount of volatile acidity in the red wine is different (bigger) than the one in the white wine, 
