import requests
import pandas as pd

def collect_data(api_url):
    response = requests.get(api_url)
    data = response.json()
    df = pd.DataFrame(data)
    return df

# Example usage
api_url = "https://example.com/api/sales_data"
data = collect_data(api_url)
data.to_csv("../data/sales_data.csv", index=False)
