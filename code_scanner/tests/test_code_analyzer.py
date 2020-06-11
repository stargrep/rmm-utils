from pathlib import Path

import pytest

from code_scanner.code_analyzer import python_code_counter
from code_scanner.file_info import FileInfo


@pytest.fixture
def root_path() -> Path:
    return Path(__file__).parent.joinpath("sample")


@pytest.fixture
def sample_file_infos(root_path: Path) -> [FileInfo]:
    paths = list(root_path.glob("*.py"))
    return list(map(lambda p: FileInfo(p), list(paths)))


def test_python_code_counter(root_path: Path, sample_file_infos: [FileInfo]):
    result = python_code_counter(root_path, sample_file_infos)
    # print(result.files[0].filtered)
    assert result.total_filtered_count == 49
    assert result.total_count == 118
