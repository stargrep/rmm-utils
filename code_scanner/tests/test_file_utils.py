from pathlib import Path

import pytest

from code_scanner.filter_utils import GeneralFileFilter, GeneralFolderFilter, IFileFilter, PythonFolderFilter


@pytest.fixture
def general_file_filter() -> GeneralFileFilter:
    return GeneralFileFilter()


@pytest.fixture
def general_folder_filter() -> GeneralFolderFilter:
    return GeneralFolderFilter()


@pytest.fixture
def python_folder_filter() -> PythonFolderFilter:
    return PythonFolderFilter()


@pytest.fixture
def current_folder() -> Path:
    return Path(__file__).parent.parent


def test_sub_class(general_file_filter: GeneralFileFilter,
                   python_folder_filter: GeneralFolderFilter) -> None:
    assert not isinstance(GeneralFileFilter, IFileFilter)
    assert isinstance(general_file_filter, GeneralFileFilter)
    assert issubclass(GeneralFileFilter, IFileFilter)
    assert issubclass(general_file_filter.__class__, IFileFilter)
    assert type(general_file_filter) is GeneralFileFilter
    assert type(general_file_filter) is not IFileFilter

    assert len(GeneralFileFilter.__mro__) == 3
    # ((<class 'code_scanner.filter_utils.GeneralFileFilter'>, <class 'code_scanner.filter_utils.IFileFilter'>,
    # <class 'object'>
    assert len(python_folder_filter.__class__.__mro__) == 4
    assert tuple(list(PythonFolderFilter.__mro__)[1:]) == GeneralFolderFilter.__mro__


def test_python_folder(current_folder: Path,
                       general_folder_filter: GeneralFolderFilter,
                       python_folder_filter: PythonFolderFilter) -> None:
    assert general_folder_filter.valid(current_folder)
    assert not general_folder_filter.valid(current_folder.joinpath("env"))
    assert len(python_folder_filter.filter([current_folder])) == 1
