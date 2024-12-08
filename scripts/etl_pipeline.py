# etl_pipeline.py
from data_collection import collect_data
from data_processing import process_data

def run_etl(api_url, raw_data_path, processed_data_path):
    """
    Runs the ETL pipeline:
    1. Extracts data from an API.
    2. Transforms the data.
    3. Loads the processed data into a CSV file.
    """
    # Extract: Collect data from the API
    print("Extracting data...")
    data = collect_data(api_url)
    if data is not None:
        data.to_csv(raw_data_path, index=False)  # Save raw data to CSV
    
    # Transform: Process the raw data
    print("Transforming data...")
    processed_data = process_data(raw_data_path)
    
    # Load: Save the processed data to a CSV file
    processed_data.to_csv(processed_data_path, index=False)
    print(f"ETL process completed. Processed data saved to {processed_data_path}")

# Example usage: running the ETL pipeline
if __name__ == "__main__":
    api_url = "https://example.com/api/sales_data"  # Replace with your actual API URL
    raw_data_path = "../data/sales_data.csv"  # Path to save raw data
    processed_data_path = "../data/processed_sales_data.csv"  # Path to save processed data
    
    run_etl(api_url, raw_data_path, processed_data_path)
