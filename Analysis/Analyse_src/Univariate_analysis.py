from abc import ABC, abstractmethod
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class UnivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyse(self, df: pd.DataFrame, feature: str):
        """Perform univariate analysis on a specific feature of the dataframe."""
        pass

class NumericalUnivariateAnalysis(UnivariateAnalysisStrategy):
    def analyse(self, df: pd.DataFrame, feature: str):
        """Plots the distribution of a numerical feature using a histogram and KDE."""
        plt.figure(figsize=(10, 6))
        sns.histplot(df[feature], kde = True, bins = 30)
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Frequency")
        plt.show()

class CategoricalUnivariateAnalysis(UnivariateAnalysisStrategy):
    def analyse(self, df: pd.DataFrame, feature: str):
        """Plots the distribution of a categorical feature using a bar plot."""
        plt.figure(figsize=(10, 6))
        sns.countplot(x=feature, data=df, palette="muted")
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.show()

class UnivariateAnalyser:
    def __init__(self, strategy: UnivariateAnalysisStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: UnivariateAnalysisStrategy):
        self._strategy = strategy

    def execute_analysis(self, df: pd.DataFrame, feature: str):
        self._strategy.analyse(df, feature)

# # Example usage
# if __name__ == "__main__":
#     # Example usage of the UnivariateAnalyzer with different strategies.

#     # Load the data
#     df = pd.read_csv('/Users/omphiletladi/Price-predictor/extracted_data/archive2/AmesHousing.csv')

#     # Analyzing a numerical feature
#     analyzer = UnivariateAnalyser(NumericalUnivariateAnalysis())
#     analyzer.execute_analysis(df, 'SalePrice')

#     # Analyzing a categorical feature
#     analyzer.set_strategy(CategoricalUnivariateAnalysis())
#     analyzer.execute_analysis(df, 'Neighborhood')
#     pass