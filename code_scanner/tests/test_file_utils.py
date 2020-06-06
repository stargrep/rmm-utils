from pathlib import Path
import pytest

from code_scanner.file_utils import retrieve_folders
from code_scanner.filter_utils import PythonFolderFilter


@pytest.fixture
def current_folder() -> Path:
    return Path(__file__).parent.parent


def test_retrieve_folders(current_folder):
    folders = retrieve_folders(current_folder, [PythonFolderFilter()])
    print(current_folder)
    print(folders)
    assert len(folders) == 2
    assert folders[0].full_name.name == 'code_scanner'
    assert folders[1].full_name.name == 'code_scanner'

    folders = retrieve_folders(current_folder, [PythonFolderFilter()], include_root=False)
    assert len(folders) == 1

