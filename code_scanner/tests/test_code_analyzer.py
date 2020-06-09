from pathlib import Path

import pytest

from code_scanner.code_analyzer import python_code_counter
from code_scanner.file_info import FileInfo


@pytest.fixture
def sample_file_infos() -> [FileInfo]:
    paths = Path(__file__).parent.joinpath("sample").glob("*.py")
    return list(map(lambda p: FileInfo(p), list(paths)))


def test_python_code_counter(sample_file_infos: [FileInfo]):
    result = python_code_counter(sample_file_infos)
    # print(result.files[0].filtered)
    assert result.total_count == 49

