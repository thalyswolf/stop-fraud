from typing import List
import csv

from src.contract.csv_contract import CSVContract
from src.core.entity.transaction import Transaction
from src.adapter.transaction_to_list_row_adapter import transaction_to_list_row_adapter

class CSV(CSVContract):

    def read_csv(self):
        pass

    def write_row(self, transactions: List[Transaction]):
        with open('./src/storage/transactions.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for transaction in transactions:
                spamwriter.writerow(transaction_to_list_row_adapter(transaction))

        
            
#[21320398, 29744, 97051, '434505******9116', '2019-12-01T23:16:32.812632', 44.56, 285475.0, False]
# 21320398        29744     97051  434505******9116  2019-12-01T23:16:32.812632              374.56  285475.0    False