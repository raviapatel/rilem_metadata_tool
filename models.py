"""
models.py
---------
Pydantic data models, the Datatype enum, and a custom JSON encoder.
"""

import datetime
import json
from enum import Enum
from typing import Set

from pydantic import BaseModel, EmailStr, Field


# --------------------------------------------------------------------------- #
#  Custom JSON encoder                                                         #
# --------------------------------------------------------------------------- #
class SetEncoder(json.JSONEncoder):
    """Serialises sets, Enums, and dates that the default encoder cannot handle."""

    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        if isinstance(obj, Enum):
            return obj.value
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        return super().default(obj)


# --------------------------------------------------------------------------- #
#  Fixed enums                                                                 #
# --------------------------------------------------------------------------- #
class Datatype(str, Enum):
    text = "text"
    table = "table"
    image = "image"
    audio = "audio"
    video = "video"


# --------------------------------------------------------------------------- #
#  Pydantic models                                                             #
# --------------------------------------------------------------------------- #
class AuthorData(BaseModel):
    title: str = Field(description="Title of the dataset")
    keywords_comma_sperated: str = Field(description="Keywords (comma-separated)")
    description: str = Field(description="Description of the dataset")
    uploaded_by: str = Field(description="Uploader – First Name, Last Name")
    email: EmailStr = Field(description="Uploader email")
    date: datetime.date = Field(description="Date of data creation")
    identifier: str = Field(description="Unique identifier for the dataset")
    contributors: str = Field(
        default="",
        description="Contributors – First Name 1, Last Name 1; First Name 2, Last Name 2 …",
    )


class DataSetInfo(BaseModel):
    pick_dataset_type: Datatype
    extension_of_the_file: str
    time_series: bool
    number_of_files: int
    description: str
    Materials: str          # stored as "Category → Material" strings
    Experiments: Set[str]   # stored as "Category → Sub" strings
