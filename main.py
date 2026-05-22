from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 
from textSummarizer.pipeline.stage_02_data_validation import DatavalidationTrainingPipeline
from textSummarizer.logging import logger


STAGE_NAME = "Data validation Stage"
try:
    logger.info(f"------------- stage {STAGE_NAME} started -----------------------")
    data_validation = DatavalidationTrainingPipeline()
    data_validation.main()
    logger.info(f"------------- stage {STAGE_NAME} completed ---------------------")

except Exception as e:
    logger.exception(e)
    raise e
from src.textSummarizer.logging import logger


logger.info("welcome to our custom logging")


