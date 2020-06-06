import enum


class FileType(enum.Enum):
    SOURCE_CODE = "SOURCE_CODE"
    TEST = "TEST"
    RESOURCE = "RESOURCE"
    CONFIG = "CONFIG"
    DIR_ENV = "DIR_ENV"
    DIR_CACHE = "DIR_CACHE"
    DIR_SOURCE = "DIR_SOURCE"
    UNKNOWN = "UNKNOWN"

