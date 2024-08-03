from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:

    valid_loan_types = {
            "StudentLoan": StudentLoan,
            "MortgageLoan": MortgageLoan
    }

    valid_client_types = {
            "Student": Student,
            "Adult": Adult
    }

    client_type_of_loan_mapper = {
        "Student": "StudentLoan",
        "Adult": "MortgageLoan"
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.valid_loan_types:
            raise Exception("Invalid loan type!")

        new_loan = self.valid_loan_types[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.valid_client_types:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        new_client = self.valid_client_types[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = [cl for cl in self.clients if cl.client_id == client_id][0]

        if self.client_type_of_loan_mapper[client.__class__.__name__] != loan_type:
            raise Exception("Inappropriate loan type!")

        loan = next(filter(lambda l: l.__class__.__name__ == loan_type, self.loans))
        client.loans.append(loan)
        self.loans.remove(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id):
        try:
            client = [cl for cl in self.clients if cl.client_id == client_id][0]
        except IndexError:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        changed_loans = len([loan.increase_interest_rate() for loan in self.loans if loan.__class__.__name__ == loan_type])
        return f"Successfully changed {changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_rates = len([client.increase_clients_interest() for client in self.clients if client.interest < min_rate])
        return f"Number of clients affected: {changed_rates}."

    def get_statistics(self):
        total_clients_count = len(self.clients)
        total_clients_income = sum([client.income for client in self.clients])
        loans_count_granted_to_clients = sum([len(client.loans) for client in self.clients])
        granted_sum = sum([2000*len(client.loans) if client.__class__.__name__ == "Student" else 50000*len(client.loans)
                           for client in self.clients])
        loans_count_not_granted = len(self.loans)
        not_granted_sum = sum([loan.amount for loan in self.loans])
        try:
            avg_client_interest_rate = sum([client.interest for client in self.clients]) / len(self.clients)
        except ZeroDivisionError:
            avg_client_interest_rate = 0

        return f"Active Clients: {total_clients_count}\n"\
               f"Total Income: {total_clients_income:.2f}\n"\
               f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n"\
               f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}\n"\
               f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
