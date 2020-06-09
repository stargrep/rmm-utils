from pathlib import Path
import os

from code_scanner.file_utils import retrieve_all_folders, retrieve_files

from code_scanner.code_analyzer import python_code_counter
from code_scanner.filter_utils import PythonSourceFileFilter, PythonFolderFilter, GeneralFolderFilter

folders = retrieve_all_folders(Path(os.getcwd()), [GeneralFolderFilter()])
path_info_list = retrieve_files(folders, [PythonSourceFileFilter()])
print(os.getcwd())
print(folders)
print(path_info_list)
result = python_code_counter(path_info_list)

print(result)
