from decimal import Decimal
from sheets.classes import Sheet, get_course_price

def main():

    table = "1Exi0hjXSMUuote-pBy7JprtGfKhgUgWrSbCRthdbjDo"
    range = "A1:D"

    sheet = Sheet()
    values = sheet.read_values(table=table, range=range)[1:]
    USD = get_course_price()

    for val in values:
        id, order, price, date = val
        view = "id:{id} order_id:{order} price:{price} date:{date}".format(
            id=id, order=order, 
            price = Decimal(price) * USD,
            date = date
        )
        print(view)

    

    

    



if __name__ == "__main__":
    main()

