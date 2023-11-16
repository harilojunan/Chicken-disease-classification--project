from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAE_NAME} started <<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAE_NAME} completed <<<<\n\nx==========x")
except Exception as e:
    logger.error(f">>>>>> stage {STAE_NAME} failed <<<<<<<<<")
    logger.error(e)
    raise e