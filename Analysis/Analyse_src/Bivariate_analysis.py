from abc import ABC, abstractmethod
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class BivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyse(self, df: pd.DataFrame, feature1: str, feature2: str):
        pass

class NumericalVsNumericalAnalysis(BivariateAnalysisStrategy):
    def analyse(self, df: pd.DataFrame, feature1: str, feature2: str):
        """Plots the relationship between two numerical features using a scatter plot."""

        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=feature1, y=feature2, data=df)
        plt.title(f"{feature1} vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.show()

class CategoricalVsNumericalAnalysis(BivariateAnalysisStrategy):
    def analyse(self, df: pd.DataFrame, feature1: str, feature2: str):
        """Plots the relationship between a categorical feature and a numerical feature using a box plot."""

        plt.figure(figsize=(10, 6))
        sns.boxplot(x=feature1, y=feature2, data=df)
        plt.title(f"{feature1} vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.xticks(rotation = 45)
        plt.show()

class BivariateAnalyser:
    def __init__(self, strategy: BivariateAnalysisStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: BivariateAnalysisStrategy):
        self._strategy = strategy
    
    def execute_analysis(self, df: pd.DataFrame, feature1: str, feature2: str):
        self._strategy.analyse(df, feature1, feature2)

# if __name__ == "__main__":
#     # Example usage of the BivariateAnalyzer with different strategies.

#     # Load the data
#     df = pd.read_csv('/Users/omphiletladi/Price-predictor/extracted_data/archive2/AmesHousing.csv')

#     # Analyzing relationship between two numerical features
#     analyzer = BivariateAnalyser(NumericalVsNumericalAnalysis())
#     analyzer.execute_analysis(df, 'Gr Liv Area', 'SalePrice')

#     # Analyzing relationship between a categorical and a numerical feature
#     analyzer.set_strategy(CategoricalVsNumericalAnalysis())
#     analyzer.execute_analysis(df, 'Overall Qual', 'SalePrice')
#     pass