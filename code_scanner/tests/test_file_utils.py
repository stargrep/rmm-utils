from pathlib import Path
import pytest

from code_scanner.file_utils import retrieve_all_folders, retrieve_files
from code_scanner.filter_utils import PythonFolderFilter, GeneralFileFilter, PythonSourceFileFilter


@pytest.fixture
def current_folder() -> Path:
    return Path(__file__).parent.parent


def test_retrieve_folders(current_folder):
    folders = retrieve_all_folders(current_folder, [PythonFolderFilter()])
    print(current_folder)
    print(folders)
    assert len(folders) == 3
    assert folders[0].full_name.name == 'code_scanner'

    folders = retrieve_all_folders(current_folder, [PythonFolderFilter()], include_root=False)
    assert len(folders) == 2


def test_retrieve_files(current_folder):
    folders = retrieve_all_folders(current_folder, [PythonFolderFilter()])
    files = retrieve_files(folders, [PythonSourceFileFilter()])
    print("Python files--", files, folders)
    assert len(files) == 12

    files = retrieve_files(folders, [GeneralFileFilter()])
    print("Files ---", files)
    assert len(files) == 17
