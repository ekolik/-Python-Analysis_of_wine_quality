import pandas as pd
import seaborn
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
import numpy

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

# call(mult_regression)


# ____________________________ Logistic Regression _____________________

def log_regression(wine_set):
    # # examining the data before recoding
    # print(wine_set["sulphates"].describe())
    # wine_set["sulphates_c"] = pd.qcut(wine_set["sulphates"], 4)
    # print(wine_set.groupby("sulphates_c").size())
    # print()
    # #
    # print(wine_set["alcohol"].describe())
    # wine_set["alcohol_c"] = pd.qcut(wine_set["alcohol"], 4)
    # print(wine_set.groupby("alcohol_c").size())
    # print()
    #
    # print(wine_set["quality"].describe())
    # wine_set["quality_c"] = pd.qcut(wine_set["quality"], 3)
    # print(wine_set.groupby("quality_c").size())
    # print()


    # recode quality into 2 groups: 0:{3,4,5,6}, 1:{7,8,9}
    recode = {3: 0, 4: 0, 5:0, 6:0, 7:1, 8:1, 9:1}
    wine_set['quality_c'] = wine_set['quality'].map(recode)

    # recode sulphates into 2 groups: 0: <= mean, 1: > mean
    def sulphates_to_cat(x):
       if x['sulphates'] <= wine_set['sulphates'].mean():
          return 0
       else:
          return 1
    wine_set['sulphates_c'] = wine_set.apply(lambda x: sulphates_to_cat(x), axis=1)

    # recode alcohol into 2 groups: 0: <= mean , 1: > mean
    def alcohol_to_cat(x):
       if x['alcohol'] <= wine_set['alcohol'].mean():
          return 0
       else:
          return 1
    wine_set['alcohol_c'] = wine_set.apply(lambda x: alcohol_to_cat(x), axis=1)
    # print(wine_set.head(10))

    # logistic regression for sulphates+alcohol -> quality
    print ("Logistic regression model for the association between wine's quality and sulphates&alcohol")
    model1 = smf.logit(formula="quality_c ~ sulphates_c + alcohol_c", data=wine_set)
    results1 = model1.fit()
    print(results1.summary())

    # odds ratios with 95% confidence intervals
    print("\nConfidence intervals")
    conf = results1.conf_int()
    conf['Odds ratio'] = results1.params
    conf.columns = ['Lower conf.int.', 'Upper conf.int.', 'Odds ratio']
    print(numpy.exp(conf))

call(log_regression)
