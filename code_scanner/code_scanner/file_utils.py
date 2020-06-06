from functools import reduce
from pathlib import Path
from code_scanner.enums import FileType
from code_scanner.file_info import FileInfo
from code_scanner.filter_utils import IFileFilter


def retrieve_folders(root: Path, folder_filters: [IFileFilter], include_root: bool = True) -> [FileInfo]:
    filtered = reduce(lambda prev, f: f.filter(prev), folder_filters, list(root.glob("*")))
    filtered = list(map(convert, filtered))

    if include_root:
        filtered.append(convert(root))
        return filtered

    return filtered


def convert(path: Path) -> FileInfo:
    if path.is_file():
        return FileInfo(path, FileType.SOURCE_CODE)
    elif path.is_dir():
        return FileInfo(path, FileType.DIR_SOURCE)
    return FileInfo(path)





