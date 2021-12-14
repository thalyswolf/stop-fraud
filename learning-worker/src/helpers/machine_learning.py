import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


from src.contract.machine_learning_contract import MachineLearningContract

class MachineLearning(MachineLearningContract):

    def __init__(self) -> None:
        self.pd = pd
        self.pickle = pickle
        self.scaler = StandardScaler
        self.train_split = train_test_split
        self.classifier = RandomForestClassifier


    def preprocessing(self) -> None:
        base = self.pd.read_csv('./src/storage/transactions.csv')
        base = base.drop('transaction_date', axis=1)
        base = base.drop('card_number', axis=1)
        base.loc[base['device_id'].isnull(), 'device_id'] = 0

        x, y = base.iloc[:, 1:5].values, base.iloc[:, 5].values

        scaler_base = self.scaler()
        x_base = scaler_base.fit_transform(x)

        x_training, x_testing, y_training, y_testing = self.train_split(x, y, test_size=0.15, random_state=0)

        with open('./src/storage/base.pkl', mode='wb') as f:
            self.pickle.dump([x_training, y_training, x_testing, y_testing], f)

    def learning(self) -> None:
        with open('./src/storage/base.pkl', 'rb') as f:
            x_training, y_training, x_testing, y_testing = pickle.load(f)

        ml = self.classifier(n_estimators=100, criterion='entropy', random_state=0)
        ml.fit(x_training, y_training)

        return self.pickle.dumps(ml)

    def test(self, model: bytes):
        ml = self.pickle.loads(model)
        print(ml)
