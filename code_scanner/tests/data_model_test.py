import pytest

from code_scanner.file_info import FileInfo


@pytest.fixture
def file_info():
    """
    Returns a test python file info
    """
    test_file_info = FileInfo('python')
    test_file_info.name = 'test.py'
    test_file_info.folder = '/tmp/'
    return test_file_info


@pytest.fixture
def another_file_info():
    """
    Returns another test python file info
    """
    test_file_info = FileInfo('python')
    test_file_info.name = 'test.py'
    test_file_info.folder = '/tmp/'
    return test_file_info


def test_file_info_funcs(file_info, another_file_info):
    assert file_info.name == 'test.py'
    assert str(file_info) == '/tmp/test.py'

    assert file_info == another_file_info
    assert hash(file_info) == hash(another_file_info)
    assert file_info is file_info   # 'is' test only identical objects
    assert repr(file_info) == repr(another_file_info)

    file_infos = [another_file_info]
    assert file_info in file_infos

    with pytest.raises(AssertionError):
        assert id(file_info) == id(another_file_info)


@pytest.mark.parametrize("updated_name,expected_full_name", [
    ('new.py', '/tmp/new.py'),
    ('tests.py', '/tmp/tests.py')
])
def test_update_file_name(file_info, updated_name, expected_full_name):
    file_info.name = updated_name
    assert str(file_info) == expected_full_name
