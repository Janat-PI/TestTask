from sqlalchemy.orm import declarative_base

from sqlalchemy import (
    Table, Column, 
    Integer, String, DECIMAL,
    Date, Sequence
)

Base = declarative_base()


class Test(Base):
    __tablename__ = "test_table"

    id = Column(Integer, Sequence('test_id_seq'), primary_key=True)
    id_obj = Column(Integer)
    order_id = Column(Integer)
    price_on_usd = Column(DECIMAL)
    price_on_rub = Column(DECIMAL)
    date_delivery = Column(Date)

    def __repr__(self):
        return f"<User(id_obj={self.id} order_id={self.order_id} \
                usd={self.price_on_usd} rub={self.price_on_rub} \
                date={self.date_delivery})"

