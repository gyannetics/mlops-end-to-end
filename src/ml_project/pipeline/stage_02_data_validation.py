# from main import STAGE_NAME
from ml_project.config.configuration import ConfigurationManager
from ml_project.components.data_validation import DataValidation
from ml_project import logger


STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        validation_result = data_validation.validate_all_columns()
        data_validation._write_status(status=validation_result)
        

if __name__ == "__main__":
    try:
        logger.info(">>>>> %s Started <<<<<", STAGE_NAME)
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(">>>>> %s Completed <<<<<", STAGE_NAME)
    except Exception as e:
        logger.exception(e)
        raise e
