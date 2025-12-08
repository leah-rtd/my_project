def preproc(X):

    return OneHotEncoder().fit_transform(X)

def preproc_num(X):
    return RobustScaler().fit_transform(X)

def concat(X1,X2):
    pass