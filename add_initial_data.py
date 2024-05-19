import os
import sqlite3

import pandas as pd

# Define the path to the data folder and the database
data_folder = "data"
database_path = "database/gestao_imobiliaria.sqlite"

# List of file names
file_names = [
    "contrato",
]

for file_name in file_names:
    # Construct the full path to the xlsx file
    file_path = os.path.join(data_folder, f"{file_name}.xlsx")

    # Read the data from the xlsx file into a DataFrame
    df = pd.read_excel(file_path)

    # Establish a connection to the SQLite database
    with sqlite3.connect(database_path) as conn:
        # Write the DataFrame to a table in the SQLite database
        df.to_sql(file_name, conn, if_exists="append", index=False)
