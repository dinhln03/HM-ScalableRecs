import os
from dataclasses import dataclass

from dotenv import load_dotenv
from loguru import logger

# Load environment variables from .env file if it exists
load_dotenv(override=True)


@dataclass
class DatasetConfig:
    HF_DATASET_PATH: str = "dinhlnd1610/HM-Personalized-Fashion-Recommendations"
    HF_TOKEN: str = os.getenv("HF_TOKEN")

    def __post_init__(self):
        if not self.HF_TOKEN:
            raise ValueError("HF_TOKEN is not set in the environment variables.")


dataset_config = DatasetConfig()
logger.info(f"Dataset Path: {dataset_config.HF_DATASET_PATH}")
