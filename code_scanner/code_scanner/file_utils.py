from functools import reduce
from pathlib import Path
from code_scanner.enums import FileType
from code_scanner.file_info import FileInfo
from code_scanner.filter_utils import IFileFilter


def retrieve_all_folders(root: Path,
                         filters: [IFileFilter],
                         include_root: bool = True,
                         recursive: bool = True) -> [FileInfo]:
    filtered = list_folders(root, filters)
    if recursive:
        to_visit = [i for i in filtered]
        while len(to_visit) > 0:
            collected = list_folders(to_visit.pop(), filters)
            to_visit += collected
            filtered += collected

    filtered = list(map(convert, filtered))

    if include_root:
        filtered.append(convert(root))
        return filtered

    return filtered


def list_folders(root: Path, filters: [IFileFilter]) -> [Path]:
    return list(reduce(lambda prev, f: f.filter(prev), filters, list(root.glob("*"))))


def retrieve_files(folders: [FileInfo], filters: [IFileFilter]) -> [FileInfo]:
    all_files = reduce(lambda prev, folder: prev + list(folder.full_name.glob("*")), folders, [])
    filtered = reduce(lambda prev, f: f.filter(prev), filters, all_files)
    return list(map(convert, filtered))


def convert(path: Path) -> FileInfo:
    if path.is_file():
        return FileInfo(path, FileType.SOURCE_CODE)
    elif path.is_dir():
        return FileInfo(path, FileType.DIR_SOURCE)
    return FileInfo(path)
