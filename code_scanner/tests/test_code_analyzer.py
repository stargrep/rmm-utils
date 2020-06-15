import pytest

from code_scanner.code_analyzer import python_code_counter
from code_scanner.file_info import FileInfo


@pytest.fixture
def sample_file_infos(sample_test_folder) -> [FileInfo]:
    paths = list(sample_test_folder.glob("*.py"))
    return list(map(lambda p: FileInfo(p), list(paths)))


def test_python_code_counter(sample_test_folder, sample_file_infos: [FileInfo]):
    result = python_code_counter(sample_test_folder, sample_file_infos)
    assert result.total_filtered_count == 49
    assert result.total_count == 118
