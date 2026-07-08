"""Folder scanning for DWG Sheet Renamer."""

from pathlib import Path


def scan_folder(folder_path: str | Path) -> list[Path]:
    """Return DWG files from one folder without scanning subfolders."""
    selected_folder = Path(folder_path)

    if not selected_folder.is_dir():
        raise NotADirectoryError(f"not a folder: {selected_folder}")

    return sorted(
        file_path
        for file_path in selected_folder.iterdir()
        if file_path.is_file() and file_path.suffix.lower() == ".dwg"
    )
