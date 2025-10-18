from fastapi import APIRouter, Depends, UploadFile, File, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController
import aiofiles
from models import ResponseSignal
import logging

# Use Uvicorn's built-in logger for consistent error logging
logger = logging.getLogger('uvicorn.error')

# Define the router for data-related endpoints
data_router = APIRouter(prefix="/api/v1/data", tags=["api_v1", "data"])

@data_router.post("/upload/{project_id}")
async def upload_data(
    project_id: str,
    file: UploadFile = File(...),
    app_settings: Settings = Depends(get_settings)
):
    # Clean up the project_id to remove whitespace or newline characters
    project_id = (project_id or "").strip()

    # Initialize the DataController
    data_controller = DataController()

    # Validate the uploaded file before saving
    is_valid, result_signal = data_controller.validate_uploaded_file(file=file)
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal": result_signal}
        )

    # Get the target project directory path
    project_dir_path = ProjectController().get_project_path(project_id=project_id)

    # Generate a unique file name and path for the upload
    file_path, file_id = data_controller.generate_unique_filepath(
        orig_file_name=file.filename,
        project_id=project_id
    )

    # Save the file asynchronously in chunks
    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
        logger.error(f"Error while uploading file: {e}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal": ResponseSignal.FILE_UPLOAD_FAILED.value}
        )

    # Return success response with file ID
    return JSONResponse(
        content={
            "signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value,
            "file_id": file_id
        }
    )
