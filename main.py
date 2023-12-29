from ml_project import logger
from ml_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ml_project.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from ml_project.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

def run_pipeline_stage(stage_name, pipeline_class):
    """
    Run a pipeline stage and handle logging and exceptions.

    Args:
        stage_name (str): The name of the stage.
        pipeline_class: The pipeline class to instantiate and run.
    """
    try:
        logger.info(">>>>> %s Started <<<<<", stage_name)
        pipeline_obj = pipeline_class()
        pipeline_obj.main()
        logger.info(">>>>> %s Completed <<<<<", stage_name)
    except Exception as e:
        logger.exception(e)
        raise e

# Run each pipeline stage
run_pipeline_stage('Data Ingestion Stage', DataIngestionTrainingPipeline)
run_pipeline_stage('Data Validation Stage', DataValidationTrainingPipeline)
run_pipeline_stage('Data Transformation Stage', DataTransformationTrainingPipeline)
