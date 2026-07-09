"""preview row building for dwg sheet renamer."""

from pathlib import Path

from dwg_sheet_renamer.config import IGNORE_KEYWORDS


def find_ignore_keyword(filename: str | Path) -> str | None:
    """return the configured ignore keyword found in a filename."""
    lowercase_filename = Path(filename).name.casefold()

    for keyword in IGNORE_KEYWORDS:
        if keyword.casefold() in lowercase_filename:
            return keyword

    return None


def is_ignored_filename(filename: str | Path) -> bool:
    """return whether a filename matches a configured ignore keyword."""
    return find_ignore_keyword(filename) is not None


def get_ignore_reason(filename: str | Path) -> str | None:
    """return the ignore reason for a filename when one applies."""
    ignore_keyword = find_ignore_keyword(filename)

    if ignore_keyword is None:
        return None

    return f"ignored because filename contains {ignore_keyword}"
