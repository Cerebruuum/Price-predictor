from abc import ABC, abstractmethod
import pandas as pd

# Define a common interface for data inspection strategies.
class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        """Perform a specific type of data inspection."""
        pass

# Inspect data types and non-null counts.
class DataTypeInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        print("\nData types and non-null counts:")
        print(df.info())

# Provide summary statistics for numerical and categorical features.
class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        print("\nSummary Statistics (Numerical features)")
        print(df.describe())
        print("\nSummary Statistics (Categorical features)")
        print(df.describe(include=["O"]))

# Manage and execute inspection strategies.
class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: DataInspectionStrategy):
        self._strategy = strategy

    def execute_inspection(self, df: pd.DataFrame):
        self._strategy.inspect(df)

# Example usage:
# if __name__ == "__main__":
#     df = pd.read_csv("/Users/omphiletladi/Price-predictor/extracted_data/archive2/AmesHousing.csv")
#     inspector = DataInspector(DataTypeInspectionStrategy())
#     inspector.execute_inspection(df)
#     inspector.set_strategy(SummaryStatisticsInspectionStrategy())
#     inspector.execute_inspection(df)