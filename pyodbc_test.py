"""
to troubleshoot connection error:
https://stackoverflow.com/questions/4657919/sql-server-does-not-exist-or-access-denied
"""

import pyodbc  # pip install pyodbc
import time

SERVER = "QS-IL-LT-NATTIK"
DATABASE = "QualiInsight_New"


def does_table_exist(cursor, schema):
    try:
        cursor.execute("SELECT * from [{schema}].[ResourceAttributesValuesSummary]".format(schema=schema))
    except Exception as e:
        return False, cursor
    else:
        return True, cursor


def alter_schema(cursor):
    print("altering NT authority schema to dbo")
    cursor.execute("ALTER SCHEMA [dbo] TRANSFER [NT AUTHORITY\SYSTEM].[ResourceAttributesValuesSummary]")
    print("wait ten seconds for changes to reflect...")
    time.sleep(10)
    print("==========")
    return cursor


def drop_table(cursor, schema):
    print("dropping dbo table")
    cursor.execute("DROP TABLE [{schema}].[ResourceAttributesValuesSummary];".format(schema=schema))
    print("wait ten seconds for changes to reflect...")
    time.sleep(10)
    print("==========")
    return cursor


def validate_insight_table():
    conn = pyodbc.connect('DRIVER={{SQL Server}};SERVER={};DATABASE={};'.format(SERVER, DATABASE))
    with conn:
        cursor = conn.cursor()
        nt_authority_check, cursor = does_table_exist(cursor, r'NT AUTHORITY\SYSTEM')
        dbo_check, cursor = does_table_exist(cursor, 'dbo')
        print("NT Authority: {}, DBO: {}".format(str(nt_authority_check), str(dbo_check)))

        # If NT Authority is present and no dbo then alter schema
        if nt_authority_check and not dbo_check:
            cursor = alter_schema(cursor)
            nt_authority_check, cursor = does_table_exist(cursor, r'NT AUTHORITY\SYSTEM')
            dbo_check, cursor = does_table_exist(cursor, 'dbo')
            print("NT Authority: {}, DBO: {}".format(str(nt_authority_check), str(dbo_check)))

            # validate and return success state
            if dbo_check and not nt_authority_check:
                return True
            else:
                return False

        # if both tables exist, delete dbo and rename NT authority schema
        elif nt_authority_check and dbo_check:
            cursor = drop_table(cursor, 'dbo')
            cursor = alter_schema(cursor)
            nt_authority_check, cursor = does_table_exist(cursor, r'NT AUTHORITY\SYSTEM')
            dbo_check, cursor = does_table_exist(cursor, 'dbo')
            print("NT Authority: {}, DBO: {}".format(str(nt_authority_check), str(dbo_check)))

            # validate and return success state
            if dbo_check and not nt_authority_check:
                return True
            else:
                return False

        elif dbo_check and not nt_authority_check:
            print("No SQL actions needed")
            return True


res = validate_insight_table()
print(str(res))
