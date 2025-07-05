import pandas as pd

url = "https://en.wikipedia.org/wiki/Dayahang_Rai"
tables = pd.read_html(url)

for i, table in enumerate(tables, start=1):
    table.to_csv(f"table_{i}.csv")
