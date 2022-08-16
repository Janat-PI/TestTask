import sys

from main import main
from DB.engine import main as init



if __name__ == "__main__":

    if sys.argv[1] == "dev":
        start = main
    elif sys.argv[1] == "migrate":
        start = init

    # try:
    #     start()
    # except Exception as e:
    #     print(e)

    start()