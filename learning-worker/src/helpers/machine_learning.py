from typing import List
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


from src.contract.machine_learning_contract import MachineLearningContract
from src.core.entity.transaction import Transaction
from src.adapter.transaction_to_dict_row_adapter import transaction_to_dict_row_adapter

class MachineLearning(MachineLearningContract):

    def __init__(self) -> None:
        self.pd = pd
        self.pickle = pickle
        self.scaler = StandardScaler
        self.train_split = train_test_split
        self.classifier = RandomForestClassifier


    def preprocessing(self, transactions: List[Transaction]) -> None:
        base = self.pd.read_csv('./src/storage/transactions.csv')

        for transaction in transactions:
            base = base.append(transaction_to_dict_row_adapter(transaction), ignore_index=True)

        print(base)

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

        print(x_training)

        ml = self.classifier(n_estimators=100, criterion='entropy', random_state=0)
        ml.fit(x_training, y_training)

        return self.pickle.dumps(ml)

    def test(self, transactions):
        base = self.pd.read_csv('./src/storage/transactions.csv')
        print(base.shape)

        data = {
            'transaction_id': 222222,
            'merchant_id': 2222,
            'user_id': 97051,
            'card_number': '434505******9116',
            'transaction_date': '2019-12-01T23:16:32.812632',
            'transaction_amount': 44.56,
            'device_id': 285475,
            'has_cbk': False
        }
        
        base = base.append(data, ignore_index=True)