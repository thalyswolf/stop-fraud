from typing import List
import csv

from src.contract.csv_contract import CSVContract
from src.core.entity.transaction import Transaction
from src.adapter.transaction_to_dict_row_adapter import transaction_to_dict_row_adapter
from src.helpers.get_env import get_env

class CSV(CSVContract):

    def read_csv(self):
        pass

    def generate_new_file(self, transactions: List[Transaction]):
        
        with open('{}transactions.csv'.format(get_env('STORAGE_DIR')), 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for transaction in transactions:
                spamwriter.writerow(transaction_to_dict_row_adapter(transaction))
