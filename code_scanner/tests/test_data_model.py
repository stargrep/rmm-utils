from pathlib import Path

import pytest

from code_scanner.enums import FileType
from code_scanner.file_info import FileInfo


@pytest.fixture
def file_info():
    """
    Returns a test python file info
    """
    return FileInfo(Path('/tmp/test.py'), FileType.SOURCE_CODE)


@pytest.fixture
def another_file_info():
    """
    Returns another test python file info
    """
    return FileInfo(Path('/tmp/test.py'), FileType.SOURCE_CODE)


def test_file_info_funcs(file_info, another_file_info):
    assert file_info.full_name == Path('/tmp/test.py')
    assert str(file_info) == 'SOURCE_CODE-/tmp/test.py'

    assert file_info == another_file_info
    assert hash(file_info) == hash(another_file_info)
    assert file_info is file_info   # 'is' test only identical objects
    assert repr(file_info) == repr(another_file_info)

    file_infos = [another_file_info]
    assert file_info in file_infos

    with pytest.raises(AssertionError):
        assert id(file_info) == id(another_file_info)


@pytest.mark.parametrize("updated_name,expected_full_name", [
    ('/tmp/new.py', 'SOURCE_CODE-/tmp/new.py'),
    ('/tmp/tests.py', 'SOURCE_CODE-/tmp/tests.py')
])
def test_update_file_name(file_info, updated_name, expected_full_name):
    file_info.full_name = updated_name
    assert str(file_info) == expected_full_name
