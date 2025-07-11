from Data_Ingestor import DataIngestorFactory
import os
import shutil

# Define the file path
file_path = "Data/archive2.zip"

# Extract the file extension
file_extension = ".zip"

# Get the appropriate ingestor using the factory
ingestor = DataIngestorFactory.get_data_ingestor(file_extension)

# Use the ingestor to read the data
try:
    df = ingestor.ingest(file_path)
    print("Data successfully ingested!")
    print(df.head())  # Print the first 5 rows of the DataFrame
except Exception as e:
    print(f"Error during ingestion: {e}")






