import unittest

from dwg_sheet_renamer.config import IGNORE_KEYWORDS
from dwg_sheet_renamer.preview import (
    find_ignore_keyword,
    get_ignore_reason,
    is_ignored_filename,
)


class IgnoreRuleTests(unittest.TestCase):
    def test_ignore_keywords_live_in_config(self) -> None:
        self.assertIn("titleblock", IGNORE_KEYWORDS)
        self.assertIn("xref", IGNORE_KEYWORDS)

    def test_detects_ignored_filename_case_insensitively(self) -> None:
        self.assertTrue(is_ignored_filename("TITLEBLOCK.dwg"))
        self.assertTrue(is_ignored_filename("xref-background.dwg"))

    def test_returns_useful_ignore_reason(self) -> None:
        self.assertEqual(
            get_ignore_reason("xref-background.dwg"),
            "ignored because filename contains xref",
        )

    def test_returns_no_ignore_reason_for_regular_sheet_name(self) -> None:
        self.assertFalse(is_ignored_filename("E1.0.dwg"))
        self.assertIsNone(find_ignore_keyword("E1.0.dwg"))
        self.assertIsNone(get_ignore_reason("E1.0.dwg"))


if __name__ == "__main__":
    unittest.main()
