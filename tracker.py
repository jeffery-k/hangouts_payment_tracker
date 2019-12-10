import json
import argparse
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials

CONFIG_FILE_NAME = "config.json"
CONFIG = json.load(open(CONFIG_FILE_NAME))


# Wrapper class for gspread.models.Spreadsheet
class SheetData:
    def __init__(self, data):
        self.data = data

    # Ensures most recent dates are in sheet
    def updateDates(self):
        cur_time = time.time()

    # Returns a map of date ranges to arrays of users with vacant payments
    def getVacancies(self):
        pass

    # Returns a map of date ranges to arrays of users with unverified payments
    def getUnverified(self):
        pass

    # Set the user status for the current period as unverified
    def submitPayment(self):
        pass

    #TODO
    # Verifies a payment via payment code
    def verifyPayment(self, code):
        pass

    # Returns row with provided time bounded by the row start and end date
    def findRow(self, time):
        pass

    # Returns a list of rows in data
    def getRows(self):
        pass

    # Returns value of entry in data given key (column name) and row index
    def getEntry(self, row_index, key):
        pass

    # Sets the value of entry in data given key (column name) and row index
    def setEntry(self, row_index, key, value):
        pass


# Starts payment tracking service
def start(sheet_data):
    pass


# Submits a payment for the calling user for the current period
def pay(sheet_data):
    pass


# Registers the calling user into the dataset
def register(sheet_data):
    pass


# Gets data from payment sheet
def getData():
    credentials_file_name = CONFIG["credentialsFileName"]

    scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file_name, scope)
    client = gspread.authorize(creds)

    sheet = client.open("Payments").sheet1
    return SheetData(sheet)


# Gets a string representation of a date
def toString(date):
    pass


# Gets a date from a string representation
def toDate(string):
    pass

# Returns calling user
def getCaller():
    pass

# Main method
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", action="store_true",
                        help="Starts payment tracking service")
    parser.add_argument("--pay", action="store_true",
                        help="Submits a payment for the calling user for the current period")
    parser.add_argument("--register", action="store_true",
                        help="Registers the calling user into the dataset")

    sheet_data = getData()
    args = parser.parse_args()

    if args.start:
        start(sheet_data)
    elif args.pay:
        pay(sheet_data)
    elif args.register:
        register(sheet_data)
    else:
        parser.print_help()



if __name__ == "__main__":
    main()
