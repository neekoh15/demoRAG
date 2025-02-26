# data_types.py:

from pydantic import BaseModel
from typing import Dict

class VectorDocument(BaseModel):
    document: str
    metadata: Dict[str, str]
    uuid: str
