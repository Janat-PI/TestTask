from sheets.classes import Sheet

def main():

    table = "1Exi0hjXSMUuote-pBy7JprtGfKhgUgWrSbCRthdbjDo"
    range = "A1:D"

    sheet = Sheet()
    sheet.read_values(table=table, range=range)
    # sheet.read_patch_get(table=table)
    # sheet.get(table)


if __name__ == "__main__":
    main()

