# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:49:51 2019

@author: nzubair
"""

from __future__ import print_function

import os
import subprocess

import pandas as pd
import numpy as np
import graphviz


from sklearn.tree import DecisionTreeClassifier, export_graphviz

#Reference taken from
#http://chrisstrelioff.ws/sandbox/2015/06/08/decision_trees_in_python_with_scikit_learn_and_pandas.html

#Step 1
def get_iris_data():
    """Get the iris data, from local csv or pandas repo."""
    if os.path.exists("iris.csv"):
        print("-- iris.csv found locally")
        df = pd.read_csv("iris.csv", index_col=0)
    else:
        print("-- trying to download from github")
        fn = "https://raw.githubusercontent.com/pydata/pandas/" + \
             "master/pandas/tests/data/iris.csv"
        try:
            df = pd.read_csv(fn)
        except:
            exit("-- Unable to download iris.csv")

        with open("iris.csv", 'w') as f:
            print("-- writing to local iris.csv file")
            df.to_csv(f)

    return df


def get_swi_data():
    print("-- Open covered_swi_params.xls")
    #df = pd.read_csv("covered_swi_params.csv", index_col=0)
    df = pd.read_csv("covered_ise_swi_params_2.csv", index_col=0)
    return df

#Step 2
#df = get_iris_data()
df = get_swi_data()

#Strp 3
print("* df.head()", df.head(), sep="\n", end="\n\n")
print("* df.tail()", df.tail(), sep="\n", end="\n\n")

#Step 4
print("* iris types:", df["Name"].unique(), sep="\n")

#Step 5
def encode_target(df, target_column):
    """Add column to df with integers for the target.

    Args
    ----
    df -- pandas DataFrame.
    target_column -- column to map to int, producing
                     new Target column.

    Returns
    -------
    df_mod -- modified DataFrame.
    targets -- list of target names.
    """
    df_mod = df.copy()
    targets = df_mod[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets)}
    df_mod["Target"] = df_mod[target_column].replace(map_to_int)

    return (df_mod, targets)

#Step 6
df2, targets = encode_target(df, "Name")
print("* df2.head()", df2[["Target", "Name"]].head(),
      sep="\n", end="\n\n")
print("* df2.tail()", df2[["Target", "Name"]].tail(),
      sep="\n", end="\n\n")
print("* targets", targets, sep="\n", end="\n\n")

#Step 7
features = list(df2.columns[18:28])
print("* features:", features, sep="\n")

#Step 8
y = df2["Target"]
X = df2[features]
dt = DecisionTreeClassifier(min_samples_split=20, random_state=99,presort=1)
dt.fit(X, y)    

#Step 9
def visualize_tree(tree, feature_names):
    """Create tree png using graphviz.

    Args
    ----
    tree -- scikit-learn DecsisionTree.
    feature_names -- list of feature names.
    """
    with open("dt.dot", 'w') as f:
        print("Going to Show the tree...")
        export_graphviz(tree, out_file=f,
                        feature_names=feature_names,filled=True,leaves_parallel=True,impurity=False,node_ids=True,proportion=False,rounded=True)

    command = ["dot", "-Tpng", "dt.dot", "-o", "dt.png"]
    try:
        subprocess.check_call(command)
    except:
        exit("Could not run dot, ie graphviz, to "
             "produce visualization")
        
#step 10
visualize_tree(dt, features)
        