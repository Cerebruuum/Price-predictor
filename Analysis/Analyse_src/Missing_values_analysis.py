from abc import ABC, abstractmethod

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Abstract base class for missing values

class MissingValuesAnalysisTemplate(ABC):
    def analyse(self, df: pd.DataFrame):
        """Performs a complete missing values analysis by identifying and visualizing missing values."""
        self.identify_missing_values(df)
        self.visualise_missing_values(df)

    @abstractmethod
    def identify_missing_values(self, df: pd.DataFrame):
        """Identifies missing values in the dataframe."""
        pass

    @abstractmethod
    def visualise_missing_values(self, df: pd.DataFrame):
        """Visualizes missing values in the dataframe."""
        pass

class SimpleMissingValuesAnalysis(MissingValuesAnalysisTemplate):
    def identify_missing_values(self, df: pd.DataFrame):

        print("\nMissing Values count by column")
        missing_values = df.isnull().sum()
        print(missing_values[missing_values > 0])

    def visualise_missing_values(self, df: pd.DataFrame):
        print("\n Visualise missing values...")
        plt.figure(figsize=(12, 8))
        sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
        plt.title("Missing Values Heatmap")
        plt.show()
