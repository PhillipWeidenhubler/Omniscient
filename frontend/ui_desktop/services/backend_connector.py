import requests
from config.app_config import BACKEND_URL
from utils.logger import initialize_logger

class BackendConnector:
    def __init__(self):
        self.url = BACKEND_URL
        self.logger = initialize_logger()

    def test_connection(self):
        """
        Attempts to connect to the backend.
        Returns True if the connection is successful (HTTP 200 response),
        otherwise logs the error and returns False.
        """
        try:
            response = requests.get(self.url, timeout=5)
            if response.status_code == 200:
                self.logger.info("Backend connection successful.")
                return True
            else:
                self.logger.error("Backend connection failed with status code: %s", response.status_code)
                return False
        except Exception as e:
            self.logger.error("Error connecting to backend: %s", e)
            return False