#!/usr/bin/env python
import scikitplot as skplt
import numpy as np
import matplotlib.pyplot as plt
from Regression_package.LogisticRegressor import LogisticRegression
"""
runs the classifier class with data from the data package
"""
xls_file = "default_credit_card_data.xls"
clf = LogisticRegression()
X, y = clf.read_credit_card_file(xls_file)
X_train, X_test, y_train, y_test = clf.train_test_split(X, y, test_size=0.3, random_state=4)

coef, loss_arr = clf.fit_data(X_train, y_train, learning_rate=0.1, n_iter=400)
pred = clf.predict(X_test)
accuracy = clf.accuracy(pred, y_test.flatten())
print(f"accuracy_score: {accuracy}")

plt.style.use("seaborn-talk")
plt.plot(loss_arr)
plt.xlabel("Number of iterations", size=15)
plt.ylabel("Cost function", size=15)
plt.legend([r"Cost function $C(\beta)$"])
plt.show()

def bestCurve(y):
	defaults = sum(y == 1)
	total = len(y)
	x = np.linspace(0, 1, total)
	y1 = np.linspace(0, 1, defaults)
	y2 = np.ones(total-defaults)
	y3 = np.concatenate([y1,y2])
	return x, y3

plot_cumulative_gain



skplt.metrics.plot_roc(y_test, pred)
plt.show()