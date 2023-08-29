import copy
from pathlib import Path

from helpers import generate_uuid, update

from config import FILE_RESOURCE_BASE_URI
from lib.types import PhysicalFileResource, VirtualFileResource
from queries.file import template_insert_file_query

def insert_file(physical_file: PhysicalFileResource):
    uuid: str = generate_uuid()

    virtual_file: VirtualFileResource = copy.deepcopy(physical_file)
    virtual_file["uuid"] = uuid
    virtual_file["uri"] = str(Path(FILE_RESOURCE_BASE_URI).joinpath(uuid))
    physical_file["data_source"] = virtual_file["uri"]

    query_string = template_insert_file_query(virtual_file, physical_file)
    update(query_string)
