from typing import NamedTuple
from decimal import Decimal
from datetime import date
from dataclasses import dataclass

from googleapiclient.errors import HttpError


def try_error(func):
    """
    try except on HttpErrror
    """

    def wrapper(self, spreadsheetId, range):
        try:
            return func(self, spreadsheetId, range)
        except HttpError as e:
            print(e)
    
    return wrapper


# @dataclass(frozen=True)
# class DBTestShema:
#     id: int
#     order_id: int
#     price_on_usd: Decimal
#     price_on_rub: Decimal
#     date_delivery: date


@dataclass(frozen=True)
class SheetData:
    id: int
    order_id: int
    price_on_usd: Decimal
    date_delivery: date
