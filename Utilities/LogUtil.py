import os
import logging
from datetime import datetime

class Logger:
    def __init__(self, logger_name, log_level=logging.INFO):
        log_directory = "Logs"  # Define the log folder
        os.makedirs(log_directory, exist_ok=True)  # Ensure directory exists

        log_filename = f"log{datetime.now().strftime('%Y-%m-%d')}.txt"
        self.LogFileName = os.path.join(log_directory, log_filename)

        # Set up logging
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(log_level)

        fh = logging.FileHandler(self.LogFileName, mode="a")
        fh.setLevel(log_level)

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)
