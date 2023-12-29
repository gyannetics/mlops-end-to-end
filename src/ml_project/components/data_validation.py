# import os
from ml_project import logger
from ml_project.entity.config_entity import DataValidationConfig
import pandas as pd


class DataValidation:
    """
    A class for validating the columns and data types of a dataset against a predefined schema.

    Attributes:
        config (DataValidationConfig): Configuration object containing settings for data validation.
    """

    def __init__(self, config: DataValidationConfig):
        """
        Initializes the DataValidation object with the given configuration.

        Parameters:
            config (DataValidationConfig): The configuration for data validation.
        """
        self.config = config

    def validate_all_columns(self) -> bool:
        """
        Validates if all columns in the dataset match the predefined schema and data types.

        Returns:
            bool: True if all columns and their data types match the schema, False otherwise.
        """
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = set(data.columns)
            schema_cols = set(self.config.all_schema.keys())

            # Check for missing columns in the data
            missing_cols = schema_cols.difference(all_cols)
            if missing_cols:
                for col in missing_cols:
                    logger.error(f"Missing column in dataset: {col}")
                return False

            # Check for extra columns in the data not present in the schema
            extra_cols = all_cols.difference(schema_cols)
            if extra_cols:
                for col in extra_cols:
                    logger.error(f"Extra column in dataset: {col}")
                return False

            # Validate data types
            for col, expected_type in self.config.all_schema.items():
                if col in data and not pd.api.types.is_dtype_equal(data[col].dtype, expected_type):
                    logger.error(f"Data type mismatch for column: {col}. Expected: {expected_type}, Found: {data[col].dtype}")
                    return False

            logger.info("All columns and data types are valid.")
            return True

        except Exception as e:
            logger.exception("Error during data validation")
            raise e

    def _write_status(self, status: bool):
        """
        Writes the validation status to the status file.

        Parameters:
            status (bool): The validation status to be written to the file.
        """
        with open(self.config.STATUS_FILE, 'w') as f:
            f.write(f"Validation status: {status}")
