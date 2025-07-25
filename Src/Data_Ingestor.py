import os
import zipfile
from abc import ABC, abstractmethod
import pandas as pd

# Defining an abstract class for data ingestion
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Abstract method to ingest data from a given file"""
        pass

# Implement a concrete class for ZIP Ingestion
class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Extracts a .zip file and returns the content as a pandas DataFrame"""

        # Ensure the file is a .zip
        if not file_path.endswith('.zip'):
            raise ValueError("The provided file is not a .zip file")
        
        # Extract the zip file
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall("extracted_data")
        
        # Find the extracted CSV file (assuming there is one CSV file inside the zip)
        csv_files = []
        for root, dirs, files in os.walk("extracted_data"):
            if "__MACOSX" in root:
                continue

            for f in files:
                if f.endswith(".csv"):
                    csv_files.append(os.path.join(root, f))

        if len(csv_files) == 0:
            raise FileNotFoundError("No CSV file found in the extracted data.")
        if len(csv_files) > 1:
            raise ValueError("Multiple CSV files found. Please specify which one to use.")
        
        # Read the CSV into a DataFrame
        csv_file_path = os.path.join(csv_files[0])
        df = pd.read_csv(csv_file_path)

        return df

#Implement a Factory to create DataIngestors
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension: str) -> DataIngestor:
        """Returns the appropriate DataIngestor based on file extension."""
        if file_extension == ".zip":
            return ZipDataIngestor()
        else:
            raise ValueError(f"No ingestor available for file extension: {file_extension}")