from decimal import Decimal

from sheets.classes import Sheet, get_course_price
from DB.engine import main as session
from sheets.helper import SheetData
from DB.shemas import Test


def parse_data(values: list[SheetData], usd: Decimal, *args, **kwargs) -> list[Test]:
    """
    function yield object(DBTestShema)
    """
    test_data = []
    for val in values:
        price_on_rub = val.price_on_usd * usd

        test_data.append(Test(
            id_obj=val.id,
            order_id=val.order_id,
            price_on_usd=val.price_on_usd,
            price_on_rub=price_on_rub,
            date_delivery=val.date_delivery
        ))

    return test_data


def main():

    spreadsheetId = "1Exi0hjXSMUuote-pBy7JprtGfKhgUgWrSbCRthdbjDo"
    range = "A1:D"

    sheet = Sheet()
    values = sheet.read_values(spreadsheetId=spreadsheetId, range=range)
    USD = get_course_price()

    all_data = parse_data(values=values, usd=USD)
    conn = session(True)
    
    conn.add_all(all_data)
    conn.commit()
    
    # for data in all_data:
        # print(data)
        # print(data)
        # conn.add(test)
    

    # data = parse_data(values=values, usd=USD)

    

if __name__ == "__main__":
    main()

