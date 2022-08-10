import sys

from main import main



if __name__ == "__main__":

    if sys.argv[1] == "dev":
        try:
            main()
        except Exception as e:
            print(e)

        