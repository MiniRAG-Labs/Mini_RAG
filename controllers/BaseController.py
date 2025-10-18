from helpers.config import get_settings, Settings
from pathlib import Path
import random
import string

class BaseController:
    def __init__(self):
        self.app_settings = get_settings()

        # Get the base directory of the project
        self.base_dir = Path(__file__).resolve().parents[1]

        # Create a fixed path to the 'assets/files' folder
        self.files_dir = self.base_dir / "assets" / "files"
        self.files_dir.mkdir(parents=True, exist_ok=True)  # Ensure the folder exists

    def generate_random_string(self, length: int = 12):
        # Generate a random lowercase alphanumeric string
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
