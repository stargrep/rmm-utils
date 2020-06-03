import enum


class FileType(enum.Enum):
    SOURCE_CODE = "SOURCE_CODE"
    TEST = "TEST"
    RESOURCE = "RESOURCE"
    TEXT = "TEXT"
    CONFIG = "CONFIG"
    MISC = "MISC"
    DIR_ENV = "DIR_ENV"
    DIR_CACHE = "DIR_CACHE"
    DIR_SOURCE = "DIR_SOURCE"
    IGNORE = "IGNORE"

