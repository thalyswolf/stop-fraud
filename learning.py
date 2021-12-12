
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier

import pickle

with open('base.pkl', 'rb') as f:
  x_training, y_training, x_testing, y_testing = pickle.load(f)

print(x_training)
# naive_risco_credito = GaussianNB()
# naive_risco_credito.fit(x_training, y_training)

# ml = SVC(kernel='poly', random_state=1, C=4.0)
# ml.fit(x_training, y_training)

# ml = MLPClassifier(max_iter=1000, verbose=True, tol=0.0000010, hidden_layer_sizes=(3, 3))
# ml.fit(x_training, y_training)

# ml = KNeighborsClassifier(n_neighbors=10, metric='minkowski', p=2)
# ml.fit(x_training, y_training)

ml = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=0)
ml.fit(x_training, y_training)

predictors = ml.predict(x_testing)
# print(naive_risco_credito.predict([[48982, 69588, 1590, 30.05, 766158.0]]))

print(accuracy_score(y_testing, predictors))


with open('./api/src/services/common/machine_learning/model.pkl','wb') as f:
    pickle.dump(ml,f)
