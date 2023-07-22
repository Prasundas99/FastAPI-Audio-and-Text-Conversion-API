from typing import Annotated
from fastapi.params import Form
from pydantic import BaseModel
from fastapi import UploadFile, File


class FileUploadRequestSchema(BaseModel):
    file: Annotated[bytes, File()]

class FileUploadResponseSchema(BaseModel):
    url: str
