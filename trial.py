# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 12:15:01 2019

@author: nzubair
"""

from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data, iris.target
features = iris.feature_names