from helpers.config import get_settings, Settings
import os
import random
import string

class BaseController:
    
    def __init__(self):

        self.app_settings = get_settings()
        
        self.base_dir = os.path.dirname( os.path.dirname(__file__) )
        self.files_dir = os.path.join(
            self.base_dir,
            "assets/files"
        )
        
    def generate_random_string(self, length: int=12):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
# import os
# import random
# import string
# from pathlib import Path
# from helpers.config import get_settings


# class BaseController:
#     def __init__(self):
#         self.app_settings = get_settings()
#         self.base_dir = Path(__file__).resolve().parent.parent  # src/
#         self.files_dir = Path(self.app_settings.FILES_DIR.strip()).resolve()
#         os.makedirs(self.files_dir, exist_ok=True)

#     def generate_random_string(self, length: int = 12):
#         return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

