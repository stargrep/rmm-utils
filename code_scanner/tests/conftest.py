from aifc import Error
from pathlib import Path
import pytest


@pytest.fixture
def root_test_folder() -> Path:
    return Path(__file__).resolve().parent


@pytest.fixture
def tmp_test_folder(root_test_folder) -> Path:
    return root_test_folder.joinpath("tmp")


@pytest.fixture
def sample_test_folder(root_test_folder) -> Path:
    return root_test_folder.joinpath("sample")