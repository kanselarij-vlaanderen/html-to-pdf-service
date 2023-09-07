import os

from datetime import datetime
from pathlib import Path
from typing import Optional

from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration

from helpers import generate_uuid

from config import STORAGE_PATH
from lib.types import PhysicalFileResource


font_config = FontConfiguration()  # Needed by WeasyPrint to allow setting fonts in CSS

def generate_pdf(html_string: str) -> bytes:
    html = HTML(string=html_string, encoding="utf-8")
    return html.write_pdf(font_config=font_config)


def write_pdf(pdf_bytes: bytes, file_name: Optional[str] = None) -> PhysicalFileResource:
    uuid: str = generate_uuid()
    if file_name is None:
        file_name = uuid
    file_path = str(Path(STORAGE_PATH).joinpath(file_name).with_suffix(".pdf"))
    now = datetime.now()

    with open(file_path, 'wb') as _file:
        _file.write(pdf_bytes)

    file_size = os.path.getsize(file_path)

    physical_file: PhysicalFileResource = {
        "uuid": uuid,
        "uri": file_path.replace("/share/", "share://"),
        "name": file_name,
        "mime_type": "application/pdf",
        "created": now,
        "size": file_size,
        "extension": "pdf",
        "data_source": "",
    }
    return physical_file
