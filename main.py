from ml_project import logger
from ml_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ml_project.pipeline.stage_02_data_validation import DataValidationTrainingPipeline


STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(">>>>> %s Started <<<<<", STAGE_NAME)
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(">>>>> %s Completed <<<<<", STAGE_NAME)
except Exception as e:
    logger.exception(e)


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(">>>>> %s Started <<<<<", STAGE_NAME)
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(">>>>> %s Completed <<<<<", STAGE_NAME)
except Exception as e:
    logger.exception(e)
    raise e