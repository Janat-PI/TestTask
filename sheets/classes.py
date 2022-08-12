import os.path
from typing import Any
from datetime import datetime
from decimal import Decimal

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import requests
import xmltodict

from sheets.helper import try_error


from sheets.abstractclasses import AbstractSheet


class CredentialsGoogle():

    SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets.readonly', 
    ]

    def __init__(self):

        self.__creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
             self.__creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not  self.__creds or not  self.__creds.valid:
            if  self.__creds and  self.__creds.expired and  self.__creds.refresh_token:
                 self.__creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                self.__creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write( self.__creds.to_json())

    def get_credentials(self):
        return self.__creds
        
    def __call__(self, *args, **kwds) -> Any:
        return self.get_credentials()


class Sheet(AbstractSheet):

    def __init__(self):
        self.cred = CredentialsGoogle()
        self.cred = self.cred.get_credentials()

    def build_service(self):
        try:
            service = build('sheets', 'v4', credentials=self.cred)
        except HttpError as e:
            print(e)
        return service
    
    @try_error
    def read_values(self, table, range=None) -> list:
        service = self.build_service()
        sheet = service.spreadsheets()
        result = sheet.values().get(
            spreadsheetId=table, 
            range=range
            ).execute()
        values = result.get('values', [])

        return values

    def get(self, spreadsheetId):
        service = self.build_service()
        sheets = service.spreadsheets()
        result = sheets.get(
            spreadsheetId,
            includeGridData=True
        )
        print(result)

    @try_error
    def read_patch_get(self, table, range=None):
        service = self.build_service()
        sheet = service.spreadsheets()
        result = sheet.values().batchGet(
            spreadsheetId=table, ranges=range
        ).execute()
        print(result)

        data = result.get("valueRanges", [])

    def write(self):
        print("work")

    def show(self, data):
        for i in data:
            print(i)

    def read(self):
        pass


def get_to_day_date() -> str:
    to_day_date = datetime.now().strftime("%d/%m/%Y")
    return to_day_date


def get_response(url: str) -> dict:
    response = requests.get(url).content
    data = xmltodict.parse(response)
    return data


def get_course_price(course: str = "USD") -> Decimal:
    
    date = get_to_day_date()
    URL = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={date}"

    data = get_response(URL)
    new_data: list[dict[str, str]] = data.get("ValCurs").get("Valute")
    USD: str = new_data[10].get("Value").replace(",", ".")

    return Decimal(USD)
