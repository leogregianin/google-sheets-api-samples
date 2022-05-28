from spreadsheets import MySheets

SPREADSHEET_ID = ''


def main():
    sheet_access = MySheets(SPREADSHEET_ID)
    sheet_data = sheet_access.read_data_sheet(data_range='page1!A1:B6')
    print(sheet_data)

if __name__ == '__main__':
    main()
