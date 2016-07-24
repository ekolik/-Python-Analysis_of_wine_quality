from sklearn.cross_validation import train_test_split
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import sklearn
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
import matplotlib.pyplot as plt
import operator
from sklearn import preprocessing
from sklearn.linear_model import LassoLarsCV
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from sklearn.decomposition import PCA
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi

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


# __________________________Decision Trees__________________________________________
def decis_tree(wine_set):
    # to remember the if the wine_set red or white
    w = wine_set

    # subset data for better tree visibility
    # wine_set = wine_set[:100]

    # recode quality (response variable) into 2 groups: 0:{3,4,5}, 1:{6,7,8,9}
    recode = {3: 0, 4: 0, 5: 0, 6: 1, 7: 1, 8: 1, 9: 1}
    wine_set['quality_c'] = wine_set['quality'].map(recode)

    # round explanatory data for easier tree
    # wine_set["residual_sugar"] = wine_set["residual_sugar"].round()
    # wine_set["alcohol"] = wine_set["alcohol"].round()

    # split into training and testing sets
    predictors = wine_set[["residual_sugar", 'alcohol']]
    targets = wine_set.quality_c

    pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, targets, test_size=.4)

    # build model on training data
    classifier = DecisionTreeClassifier()
    classifier = classifier.fit(pred_train, tar_train)

    predictions = classifier.predict(pred_test)

    # print the confusion matrix and accuracy of the model
    print(sklearn.metrics.confusion_matrix(tar_test, predictions))
    print(sklearn.metrics.accuracy_score(tar_test, predictions))

    # export the tree for viewing
    if w.equals(red):
        export_graphviz(classifier, out_file="red_decision_tree.dot")
    else:
        export_graphviz(classifier, out_file="white_decision_tree.dot")
    # to view the decision tree create a .pdf file from the created .dot file
    # by typing in the terminal from this directory: dot -Tpdf decision_tree.dot -o decision_tree.pdf
# print('----------------Decision Tree------------------------')
# call(decis_tree)


# ____________________________________Random Forests________________
def random_forests(wine_set):
    # recode quality (response variable) into 2 groups: 0:{3,4,5}, 1:{6,7,8,9}
    recode = {3: 0, 4: 0, 5: 0, 6: 1, 7: 1, 8: 1, 9: 1}
    wine_set['quality_c'] = wine_set['quality'].map(recode)

    # split into training and testing sets
    predictors = wine_set[["density", 'alcohol', 'sulphates', 'pH', 'volatile_acidity', 'chlorides', 'fixed_acidity',
                           'citric_acid', 'residual_sugar', 'free_sulfur_dioxide', 'total_sulfur_dioxide']]

    targets = wine_set.quality_c

    pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, targets, test_size=.4)

    # build model on training data#
    classifier = RandomForestClassifier(n_estimators=25)
    classifier = classifier.fit(pred_train, tar_train)

    predictions = classifier.predict(pred_test)
    # print the confusion matrix and accuracy of the model
    print('confusion matrix:\n', sklearn.metrics.confusion_matrix(tar_test, predictions))
    print('\naccuracy:', sklearn.metrics.accuracy_score(tar_test, predictions))

    # to display the relative importance of each predictive variable
    model = ExtraTreesClassifier()
    model.fit(pred_train, tar_train)

    print('importance of predictors:')
    dct = dict()
    for c in range(len(predictors.columns)):
        dct[predictors.columns[c]] = model.feature_importances_[c]
    print(sorted(dct.items(), key=operator.itemgetter(1), reverse=True))

    # run different numbers of trees to see the effect of the number on the accuracy of the prediction
    n = 100
    accuracy = [0]*n

    for i in range(n):
        classifier = RandomForestClassifier(n_estimators=i+1)
        classifier = classifier.fit(pred_train, tar_train)
        predictions = classifier.predict(pred_test)
        accuracy[i] = sklearn.metrics.accuracy_score(tar_test, predictions)

    plt.plot(range(1, n+1), accuracy)
    plt.xlabel("Number of trees")
    plt.ylabel("Accuracy of prediction")
    plt.title("Effect of the number of trees on the prediction accuracy")
    plt.show()

    print(accuracy)

# print('----------------Random Forests------------------------')
# call(random_forests)


# ________________________________Lasso Regression__________________________________
def lasso_regr(wine_set):

    pred = wine_set[["density", 'alcohol', 'sulphates', 'pH', 'volatile_acidity', 'chlorides', 'fixed_acidity',
                    'citric_acid', 'residual_sugar', 'free_sulfur_dioxide', 'total_sulfur_dioxide']]
    predictors = pred.copy()
    targets = wine_set.quality

    # standardize predictors to have mean=0 and sd=1
    predictors = pd.DataFrame(preprocessing.scale(predictors))
    predictors.columns = pred.columns
    # print(predictors.head())

    # split into training and testing sets
    pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, targets, test_size=.3, random_state=123)

    # specify the lasso regression model
    model = LassoLarsCV(cv=10, precompute=False).fit(pred_train, tar_train)

    print('Predictors and their regression coefficients:')
    d = dict(zip(predictors.columns, model.coef_))
    for k in d:
        print(k, ':', d[k])

    # plot coefficient progression
    m_log_alphas = -np.log10(model.alphas_)
    # ax = plt.gca()
    plt.plot(m_log_alphas, model.coef_path_.T)
    print('\nAlpha:', model.alpha_)
    plt.axvline(-np.log10(model.alpha_), linestyle="dashed", color='k', label='alpha CV')
    plt.ylabel("Regression coefficients")
    plt.xlabel("-log(alpha)")
    plt.title('Regression coefficients progression for Lasso paths')
    plt.show()

    # plot mean squared error for each fold
    m_log_alphascv = -np.log10(model.cv_alphas_)
    plt.plot(m_log_alphascv, model.cv_mse_path_, ':')
    plt.plot(m_log_alphascv, model.cv_mse_path_.mean(axis=-1), 'k', label='Average across the folds', linewidth=2)
    plt.legend()
    plt.xlabel('-log(alpha)')
    plt.ylabel('Mean squared error')
    plt.title('Mean squared error on each fold')
    plt.show()

    # Mean squared error from training and test data
    train_error = mean_squared_error(tar_train, model.predict(pred_train))
    test_error = mean_squared_error(tar_test, model.predict(pred_test))
    print('\nMean squared error for training data:', train_error)
    print('Mean squared error for test data:', test_error)

    rsquared_train = model.score(pred_train, tar_train)
    rsquared_test = model.score(pred_test, tar_test)
    print('\nR-square for training data:', rsquared_train)
    print('R-square for test data:', rsquared_test)
#
# print('----------------Lasso Regression------------------------')
# call(lasso_regr)


# ______________________________K-Means Cluster Analysis_________________

def k_means(wine_set):

    # standardize predictors to have mean=0 and sd=1
    pred = wine_set[["density", 'alcohol', 'sulphates', 'pH', 'volatile_acidity', 'chlorides', 'fixed_acidity',
                    'citric_acid', 'residual_sugar', 'free_sulfur_dioxide', 'total_sulfur_dioxide']]
    clustervar = pred.copy()

    clustervar = pd.DataFrame(preprocessing.scale(clustervar))
    clustervar.columns = pred.columns

    # split into training and testing sets
    clus_train, clus_test = train_test_split(clustervar, test_size=.3, random_state=123)
    # print(clus_train.shape)

    # _________________k-means cluster analysis for 1-9 clusters
    clusters = range(1, 10)
    meandist = []

    for k in clusters:
        # print(k)
        model = KMeans(n_clusters=k)
        model.fit(clus_train)
        # clusassign = model.predict(clus_train)
        meandist.append(sum(np.min(cdist(clus_train, model.cluster_centers_, 'euclidean'), axis=1))/clus_train.shape[0])

    print('Average distance from observations to the cluster centroids for 1-9 clusters:')
    print(meandist)

    # plot average distance from observations to the cluster centroid
    # to use the Elbow Method to identify number of clusters to choose
    plt.plot(clusters, meandist)
    plt.xlabel('Number of clusters')
    plt.ylabel('Average distance')
    plt.title('Selecting k with the Elbow Method')
    plt.show()

    ## _________Plot solution for each number of clusters (1-9) to choose the best
    # for k in clusters:
    #     modelk = KMeans(n_clusters=k)
    #     modelk.fit(clus_train)
    #     # clusassign = modelk.predict(clus_train)
    #
    #     # plot clusters
    #     pca_2 = PCA(2)
    #     plot_columns = pca_2.fit_transform(clus_train)
    #     plt.scatter(x=plot_columns[:, 0], y=plot_columns[:, 1], c=modelk.labels_)
    #     plt.xlabel('Canonical variable 1')
    #     plt.ylabel('Canonical variable 2')
    #     plt.title('Canonical variables for k clusters')
    #     plt.show()

    # ________ 2-cluster solution proven to be the best
    model2 = KMeans(n_clusters=2)
    model2.fit(clus_train)
    # plot clusters
    pca_2 = PCA(2)
    plot_columns = pca_2.fit_transform(clus_train)
    plt.scatter(x=plot_columns[:, 0], y=plot_columns[:, 1], c=model2.labels_)
    plt.xlabel('Canonical variable 1')
    plt.ylabel('Canonical variable 2')
    plt.title('Canonical variables for 2 clusters')
    plt.show()

    # __________merge cluster assignment with clustering variables to examine cluster variable means by cluster

    # create a unique identifier variable from the index for the cluster training data
    # to merge with the cluster assignment variable

    clus_train.reset_index(level=0, inplace=True)
    # create a list that has the new index variable
    cluslist = list(clus_train['index'])
    # print(cluslist)
    # create a list of cluster assignments
    labels = list(model2.labels_)
    # combine index variable list with cluster assignment list into a dictionary
    newlist = dict(zip(cluslist, labels))
    # convert newlist dictionary to a dataframe
    newclus = pd.DataFrame.from_dict(newlist, orient='index')
    # rename the cluster assignment column
    newclus.columns = ['cluster']
    # create a unique identifier variable from the index for the cluster assignment dataframe
    # to merge with cluster training data
    newclus.reset_index(level=0, inplace=True)
    # merge the cluster assignment dataframe with the cluster training variable dataframe by the index variable
    merged_train = pd.merge(clus_train, newclus, on='index')
    # print(merged_train.head(n=100))
    print('\nCounts of observations per each cluster:')
    print(merged_train.cluster.value_counts())

    # calculate clustering variable means by cluster
    clustergrp = merged_train.groupby('cluster').mean()
    print('\nClustering variable means by cluster:')
    print(clustergrp)

    # _________validate clusters in training data by examining cluster differences
    #               in wine quality (validation variable) using ANOVA_____________
    # merge wine quality with clustering variables and cluster assignment data
    qual = wine_set['quality']
    # split quality data into train and test sets
    qual_train, qual_test = train_test_split(qual, test_size=.3, random_state=123)
    qual_train1 = pd.DataFrame(qual_train)
    qual_train1.reset_index(level=0, inplace=True)
    merged_train_all = pd.merge(qual_train1, merged_train, on='index')
    sub1 = merged_train_all[['quality', 'cluster']]

    mod = smf.ols(formula='quality ~ C(cluster)', data=sub1).fit()
    print(mod.summary())

    print('\nMeans for wine quality by cluster:')
    print(sub1.groupby('cluster').mean())
    print('\nStandard deviations for wine quality by cluster:')
    print(sub1.groupby('cluster').std())

    # perform Post hoc test (using Tukey's Honestly Significant Difference Test)
    mc1 = multi.MultiComparison(sub1['quality'], sub1['cluster'])
    res1 = mc1.tukeyhsd()
    print(res1.summary())

print('----------------K-Means Cluster Analysis------------------------')
call(k_means)
