#Scikit learn estimator api

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

#.fit()
#learns from data
scaler.fit(X_train)
#scaler computes: mean, std, etc and stores these values internally


#.transform()
#uses what was learned during .fit()

X_train_scaled = scaler.transform(X_train)
#not every feature is standardized







