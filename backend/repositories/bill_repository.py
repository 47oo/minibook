# bill_repository.py

from sqlalchemy.orm import Session
from models.bill_model import Bill
from datetime import datetime

class BillRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_bill(self, transaction_time: datetime, transaction_type: str, counterparty: str,
                    description: str, transaction_amount: float, transaction_category: str,
                    funding_source: str, user_id: int):
        new_bill = Bill(transaction_time=transaction_time, transaction_type=transaction_type,
                        counterparty=counterparty, description=description,
                        transaction_amount=transaction_amount, transaction_category=transaction_category,
                        funding_source=funding_source, user_id=user_id)
        self.db.add(new_bill)
        self.db.commit()
        self.db.refresh(new_bill)
        return new_bill

    def get_bill_by_id(self, bill_id: int):
        return self.db.query(Bill).filter(Bill.id == bill_id).first()

    def get_user_bills(self, user_id: int):
        return self.db.query(Bill).filter(Bill.user_id == user_id).all()

    def update_bill_description(self, bill_id: int, new_description: str):
        bill = self.get_bill_by_id(bill_id)
        if bill:
            bill.description = new_description
            self.db.commit()
            self.db.refresh(bill)
            return bill

    def delete_bill(self, bill_id: int):
        bill = self.get_bill_by_id(bill_id)
        if bill:
            self.db.delete(bill)
            self.db.commit()
           
