import tempfile
import unittest
from pathlib import Path

from dwg_sheet_renamer.scanner import scan_folder


class ScanFolderTests(unittest.TestCase):
    def test_returns_only_dwg_files_from_selected_folder(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            selected_folder = Path(temp_dir)
            dwg_file = selected_folder / "E1.0.dwg"
            uppercase_dwg_file = selected_folder / "M1.0.DWG"
            text_file = selected_folder / "notes.txt"

            dwg_file.write_text("")
            uppercase_dwg_file.write_text("")
            text_file.write_text("")

            self.assertEqual(
                scan_folder(selected_folder),
                [dwg_file, uppercase_dwg_file],
            )

    def test_ignores_dwg_files_in_subfolders(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            selected_folder = Path(temp_dir)
            subfolder = selected_folder / "nested"
            subfolder.mkdir()
            nested_dwg_file = subfolder / "E2.0.dwg"
            nested_dwg_file.write_text("")

            self.assertEqual(scan_folder(selected_folder), [])

    def test_rejects_non_folder_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            selected_folder = Path(temp_dir)
            file_path = selected_folder / "E1.0.dwg"
            file_path.write_text("")

            with self.assertRaises(NotADirectoryError):
                scan_folder(file_path)


if __name__ == "__main__":
    unittest.main()
