import os

MU_APPLICATION_GRAPH = os.environ.get(
    "MU_APPLICATION_GRAPH"
) or "http://mu.semte.ch/application"
MU_APPLICATION_FILE_STORAGE_PATH = os.environ.get(
    "MU_APPLICATION_FILE_STORAGE_PATH"
) or "";
STORAGE_PATH = os.path.join(
    "/share",
    MU_APPLICATION_FILE_STORAGE_PATH,
    "",  # Extra empty string for trailing slash
)
FILE_RESOURCE_BASE_URI = os.environ.get(
    "FILE_RESOURCE_BASE_URI"
) or "http://themis.vlaanderen.be/id/bestand/"
