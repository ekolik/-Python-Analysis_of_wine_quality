from sklearn.cross_validation import train_test_split
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import sklearn

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


#__________________________Decision Trees__________________________________________
def decis_tree(wine_set):
    # to remember the if the wine_set red or white
    w = wine_set

    # subset data for better tree visibility
    wine_set = wine_set[:100]
    # recode quality (response variable) into 2 groups: 0:{3,4,5}, 1:{6,7,8,9}
    recode = {3: 0, 4: 0, 5:0, 6:1, 7:1, 8:1, 9:1}
    wine_set['quality_c'] = wine_set['quality'].map(recode)
    # round explanatory data for easier tree
    wine_set["residual_sugar"] = wine_set["residual_sugar"].round()
    wine_set["alcohol"] = wine_set["alcohol"].round()

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
print('----------------Decision Tree------------------------')
call(decis_tree)