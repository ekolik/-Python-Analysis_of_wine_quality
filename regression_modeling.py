import pandas as pd
import seaborn
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm

red = pd.read_csv('winequality-red.csv', low_memory=False, sep=';')
white = pd.read_csv('winequality-white.csv', low_memory=False, sep=';')


def call(functionToCall):
    print('Red')
    functionToCall(red)
    print('\n')

    print('White')
    functionToCall(white)
    print('\n')


# ----- to remove all spaces from column names ---------
def remove_col_spaces(wine_set):
    wine_set.columns = [x.strip().replace(' ', '_') for x in wine_set.columns]
    return wine_set

call(remove_col_spaces)


# # ______________________________ Basics of Linear Regression_____________________________________
#
def basic_linear(wine_set):
    scat0 = seaborn.regplot(x="volatile_acidity", y="quality", fit_reg=True, data=wine_set)
    plt.xlabel("Amount of volatile acidity in wine")
    plt.ylabel("Quality level of wine (0-10 scale)")
    plt.title("Association between the amount of volatile acidity in wine and the quality of wine")
    plt.show()

    # ----------- centering the explanatory variable by subrtacting the mean
    f_acidity_mean = wine_set["volatile_acidity"].mean()
    print("mean of the volatile acidity variable = ", f_acidity_mean)
    wine_set["volatile_acidity"] = wine_set["volatile_acidity"] - f_acidity_mean
    print("mean of the volatile acidity variable after normalization = ", wine_set["volatile_acidity"].mean())

    print ("\nOLS regression model for the association between the amount of volatile acidity in wine and the quality of wine:")
    model1 = smf.ols(formula="quality ~ volatile_acidity", data=wine_set)
    results1 = model1.fit()
    print(results1.summary())


# call(basic_linear)


# #___________________________________ Multiple Regression___________________________________________

def mult_regression(wine_set):
    # center quantitative IVs for regression analysis
    w = wine_set['quality']
    wine_set = wine_set - wine_set.mean()
    wine_set['quality'] = w

    print ("OLS multivariate regression model")
    # first i have run with all columns; than chose the most significant for each wine set and rerun:

    if len(wine_set) < 2000:
        # for red
        model1 = smf.ols(
            formula="quality ~ volatile_acidity + chlorides + pH + sulphates + alcohol",
            data=wine_set)
    else:
        # for white
        model1 = smf.ols(
            formula="quality ~ volatile_acidity + density + pH + sulphates + alcohol",
            data=wine_set)

    results1 = model1.fit()
    print(results1.summary())

    # q-q plot for normality
    qq = sm.qqplot(results1.resid, line = 'r')
    plt.show()

    # plot of residuals
    stdres = pd.DataFrame(results1.resid_pearson)
    plt.plot(stdres, 'o', ls = 'None')
    l = plt.axhline(y=0, color = 'r')
    plt.ylabel('Standardized redisual')
    plt.xlabel('Observation number')
    plt.show()

    # # diagnostic plots
    # figure1 = plt.figure(figsize=(12, 8))
    # figure1 = sm.graphics.plot_regress_exog(results1, "alcohol", fig = figure1)
    # plt.show()
    #
    # figure1 = plt.figure(figsize=(12, 8))
    # figure1 = sm.graphics.plot_regress_exog(results1, "sulphates", fig = figure1)
    # plt.show()

    # leverage plot
    figure1 = sm.graphics.influence_plot(results1, size=8)
    plt.show()

call(mult_regression)