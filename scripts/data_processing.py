# data_processing.py
import pandas as pd

def process_data(file_path):
    """
    Processes the sales data by cleaning and transforming it.
    This includes handling missing values, converting columns, etc.
    """
    data = pd.read_csv(file_path)  # Load the data from CSV into a DataFrame

    # Example Processing:
    # 1. Drop rows with missing values
    data.dropna(inplace=True)

    # 2. Convert 'sales_date' column to datetime format
    data['sales_date'] = pd.to_datetime(data['sales_date'])

    # 3. Create a new column 'total_sales' by multiplying quantity and price
    if 'quantity' in data.columns and 'price' in data.columns:
        data['total_sales'] = data['quantity'] * data['price']

    return data

# Example usage: processing the collected data
if __name__ == "__main__":
    file_path = "../data/sales_data.csv"  # Replace with the path to your collected data
    processed_data = process_data(file_path)
    processed_data.to_csv("../data/processed_sales_data.csv", index=False)  # Save cleaned data
    print("Data processed and saved to 'data/processed_sales_data.csv'")
