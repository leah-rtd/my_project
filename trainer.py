def preproc(X):
    return RobustScaler().fit_transform(X)