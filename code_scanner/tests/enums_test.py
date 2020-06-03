import pytest

from code_scanner.enums import FileType


def test_enums_funcs():
    assert FileType.IGNORE is FileType.IGNORE
    assert FileType.SOURCE_CODE is FileType.SOURCE_CODE
    assert FileType.DIR_SOURCE is not FileType.SOURCE_CODE
    assert FileType.SOURCE_CODE is not "SOURCE_CODE"
    assert FileType.SOURCE_CODE.name == "SOURCE_CODE"
    assert FileType["SOURCE_CODE"].name == "SOURCE_CODE"

    with pytest.raises(AssertionError):
        assert id(FileType.IGNORE) != id(FileType.IGNORE)
