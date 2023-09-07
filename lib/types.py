from typing import TypedDict
from datetime import datetime


class VirtualFileResource(TypedDict):
    uuid: str
    uri: str
    name: str
    mime_type: str
    created: datetime
    size: int
    extension: str


class PhysicalFileResource(VirtualFileResource):
    data_source: str
