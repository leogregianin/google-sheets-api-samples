from spreadsheets import MySheets

SPREADSHEET_ID = ''


def main():
    data = []
    sheet_access = MySheets(SPREADSHEET_ID)

    data_update_column1 = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6']
    data_update_column2 = ['E1', 'E2', 'E3', 'E4', 'E5', 'E6']

    for index, item in enumerate(data_update_column1, 0):
        data.append([data_update_column1[index], data_update_column2[index]])

    sheet_data = sheet_access.write_data_sheet(
        data_range='page1!D1:E6',
        data_update=data
    )
    print(sheet_data)

if __name__ == '__main__':
    main()
