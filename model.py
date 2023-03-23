import numpy as np
from sklearn.neighbors import KNeighborsClassifier


def predict(temp, wind):
    data = np.loadtxt("sample_data.csv", delimiter=",", dtype=int)
    X = data[:, :2]
    y = data[:,2]
    knn = KNeighborsClassifier(n_neighbors=2, metric='euclidean')
    knn.fit(X, y)

    testval = np.array([[temp,wind]])
    value = knn.predict(testval)[0]
    
    if(value == 1):
        return "Pants and Long Sleeve 👖 👔"
    elif(value == 2):
        return "Shorts and Long Sleeve 🩳 👔"
    elif(value == 3):
        return "Shorts and Short Sleeve 🩳 🎽"
    elif(value == 4):
        return "Shorts and No Shirt! 🩳 "
    else:
        return str(value)

