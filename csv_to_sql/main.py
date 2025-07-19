# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from multiprocessing import current_process
import pandas as pd
import sqlite3
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pathlib import Path


def csv_to_db(csv_filedir):
    if not Path(csv_filedir).is_file():  # if needed ask for user input of CVS file
        current_path = os.getcwd()
        Tk().withdraw()
        csv_filedir = askopenfilename(initialdir=current_path)

    try:
        data = pd.read_csv(csv_filedir)  # load CSV file
    except FileNotFoundError as e:
        print(f"Something went wrong when opening to the file {e.strerror}")
        print(csv_filedir)

    csv_df = pd.DataFrame(data)
    csv_df = csv_df.fillna('NULL')  # make NaN = to 'NULL' for SQL format

    [path, filename] = os.path.split(csv_filedir)  # define path and filename
    [filename, _] = os.path.splitext(filename)
    database_filedir = os.path.join(path, filename + '.db')

    conn = sqlite3.connect(database_filedir)  # connect to SQL server

    [fields_sql, header_sql_string] = create_sql_fields(csv_df)

    # CREATE EMPTY DATABASE
    create_sql = ''.join(['CREATE TABLE IF NOT EXISTS ' + filename + ' (' + fields_sql + ')'])
    cursor = conn.cursor()
    cursor.execute(create_sql)

    # INSERT EACH ROW IN THE SQL DATABASE
    for irow in csv_df.itertuples():
        insert_values_string = ''.join(['INSERT INTO ', filename, header_sql_string, ' VALUES ('])
        insert_sql = f"{insert_values_string} {irow[1]}, '{irow[2]}','{irow[3]}', {irow[4]}, '{irow[5]}' )"
        print(insert_sql)
        cursor.execute(insert_sql)

    # COMMIT CHANGES TO DATABASE AND CLOSE CONNECTION
    conn.commit()
    conn.close()

    print('\n' + csv_filedir + ' \n converted to \n' + database_filedir)

    return database_filedir


def create_sql_fields(df):  # gather the headers of the CSV and create two strings
    fields_sql = []  # str1 = var1 TYPE, va2, TYPE ...
    header_names = []  # str2 = var1, var2, var3, var4
    for col in range(0, len(df.columns)):
        fields_sql.append(df.columns[col])
        fields_sql.append(str(df.dtypes[col]))

        header_names.append(df.columns[col])
        if col != len(df.columns) - 1:
            fields_sql.append(',')
            header_names.append(',')

    fields_sql = ' '.join(fields_sql)
    fields_sql = fields_sql.replace('int64', 'integer')
    fields_sql = fields_sql.replace('float64', 'integer')
    fields_sql = fields_sql.replace('object', 'text')

    header_sql_string = '(' + ''.join(header_names) + ')'

    return fields_sql, header_sql_string


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    csv_to_db('')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
