from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
import os

class ProjectController(BaseController):
    
    def __init__(self):
        super().__init__()

    def get_project_path(self, project_id: str):
        project_dir = os.path.join(
            self.files_dir,
            project_id
        )

        if not os.path.exists(project_dir):
            os.makedirs(project_dir)

        return project_dir

# from .BaseController import BaseController
# from fastapi import UploadFile
# from models import ResponseSignal
# from pathlib import Path

# class ProjectController(BaseController):
#     def __init__(self):
#         super().__init__()

#     def get_project_path(self, project_id: str) -> str:
#         safe_id = project_id.strip().replace("\\", "_").replace("/", "_")
#         project_dir = Path(self.files_dir) / safe_id
#         project_dir.mkdir(parents=True, exist_ok=True)
#         return str(project_dir)

