from googleapiclient.errors import HttpError

def try_error(func):
    """
    try except on HttpErrror
    """

    def wrapper(self, table, range):
        try:
            func(self, table, range)
        except HttpError as e:
            print(e)
    
    return wrapper