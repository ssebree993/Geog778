# Retest connection for Austin's data
# requests was throwing an error - reset env
# Clone up to Github repo

import requests
import pandas as pd

url = "https://data.austintexas.gov/resource/xwdj-i9he.json"

params = {
    "$select": "sr_type_desc, count(*)",
    "$group": "sr_type_desc",
    "$order": "count DESC",
    "$limit": 20
}

r = requests.get(url, params=params)
df = pd.DataFrame(r.json())
print(df)