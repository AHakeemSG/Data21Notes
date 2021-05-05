import pandas as pd
from sqlalchemy import create_engine

pd.options.display.max_columns = 50
pd.options.display.max_rows = 50


def create_mssql_connection(user, password, server, database, driver):
    """
    Return a connection object for a Microsoft Sql Server Database.
    """
    engine = create_engine(
        f"mssql+pyodbc://{user}:{password}@{server}/{database}?driver={driver}"
    )

    connection = engine.connect()

    return connection


def run_query(conn, query):
    """
    Return a dataframe of results given a query.
    """
    result = conn.engine.execute(query)
    fields = result._metadata.keys
    outputs = result.fetchall()
    df = pd.DataFrame(outputs, columns=fields)

    return df


server = 'localhost,1433'
port = 1433
database = 'Northwind'
user = 'SA'
password = 'Passw0rd2018'
# driver = 'SQL+Server' -- This is for Windows machines
driver = "/usr/local/lib/libtdsodbc.so"

if __name__ == '__main__':
    conn = create_mssql_connection(
        user=user, password=password, server=server, database=database, driver=driver
    )


    query_1 = "SELECT TOP 5 * from Products;"
    query_2 = "SELECT * from Products;"

    prods_df = run_query(conn=conn, query=query_1)
    print(prods_df.shape)

    prods_df2 = run_query(conn=conn, query=query_2)
    print(prods_df2.shape)
    print(prods_df2.head(5))

    category_df = run_query(conn=conn, query="SELECT * FROM Categories;")
    print(category_df.shape)
    print(category_df.head(5))