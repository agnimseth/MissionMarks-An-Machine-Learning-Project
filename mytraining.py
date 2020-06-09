import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression


def data_split(data, ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data)*ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices] 


if __name__ == "__main__":
    
    data = pd.read_csv('C:\\Users\\Agnim S\\Desktop\\FINALSTUDENTDATA.csv')
    train,test = data_split(data, 0.2)

    x_train = train[['MS-I','MS-II','INTERNAL','EXTERNAL']].to_numpy()
    x_test = test[['MS-I','MS-II','INTERNAL','EXTERNAL',]].to_numpy()

    y_train = train[['ENDSEM']].to_numpy().reshape(332,)
    y_test = test[['ENDSEM']].to_numpy().reshape(83,)    

    
    clf = LinearRegression()
    clf.fit(x_train, y_train)

    
     

    # open a file, where you ant to store the data
    file = open('model.pkl', 'wb')

    # dump information to that file
    pickle.dump(clf, file)
    file.close()



