from typing import List
import csv

from src.contract.csv_contract import CSVContract
from src.core.entity.transaction import Transaction
from src.adapter.transaction_to_dict_row_adapter import transaction_to_dict_row_adapter

class CSV(CSVContract):

    def read_csv(self):
        pass

    def generate_new_file(self, transactions: List[Transaction]):
        
        with open('./src/storage/transactions.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for transaction in transactions:
                spamwriter.writerow(transaction_to_dict_row_adapter(transaction))

