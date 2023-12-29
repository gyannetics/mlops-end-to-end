from ml_project.config.configuration import ConfigurationManager
from ml_project.components.model_trainer import ModelTrainer
from ml_project import logger
from ml_project.pipeline.stage_01_data_ingestion import STAGE_NAME

STAGE_NAME = "Model Training Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
        
        
if __name__ == "__main__":
    try:
        logger.info("%s started", STAGE_NAME)
        model_trainer_obj = ModelTrainerPipeline()
        model_trainer_obj.main()
        logger.info("%s completed", STAGE_NAME)
    except Exception as e:
        logger.exception(e)
        raise e