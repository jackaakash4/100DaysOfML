#Hyperparameter optimization with GridSearchCV
"""
Every ML model has settings called hyperparameters

we use grid search to value of hyperparameter

"""

from sklearn.model_selection import GridSearchCV

params = {
        "model_C": [0.01, 0.1, 1, 10]
        }

#GridSearch

grid = GridSearch(
        pipeline,
        params,
        cv=5,
        scoring = "accuracy"
        )

grid.fit(X_train, y_train)

#Best result
print(grid.best_params_)
print(grid.best_score_)


