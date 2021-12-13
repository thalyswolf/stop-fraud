from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier

import pickle

with open('base.pkl', 'rb') as f:
  x_training, y_training, x_testing, y_testing = pickle.load(f)

ml = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=0)
ml.fit(x_training, y_training)

predictors = ml.predict(x_testing)

print(accuracy_score(y_testing, predictors))

with open('./api/src/services/common/machine_learning/model.pkl','wb') as f:
    pickle.dump(ml,f)
