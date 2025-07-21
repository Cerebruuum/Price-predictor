from steps.data_ingestion_step import data_ingestion_step
from steps.handling_missing_values_step import handle_missing_values_step
from steps.feature_engineering_step import feature_engineering_step
from zenml import Model, pipeline, step

@pipeline(
    model=Model(
        name="prices_predictor"
    ),
)

def ml_pipline():
    raw_data = data_ingestion_step(file_path = "/Users/omphiletladi/Price-predictor/Data/archive2.zip")

    filled_data = handle_missing_values_step(raw_data)

    engineered_data = feature_engineering_step(filled_data, strategy="log", features=["Gr Liv Area", "SalePrice"])