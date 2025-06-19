"""Utility to convert scraped bible JSON data into XML."""

from __future__ import annotations

import json
import os
from typing import Any, List

import xmltodict


def generate_xml_from_data(data: List[Any], bible_name: str = "TPT") -> str:
    """Convert bible data loaded from JSON to an XML string."""
    modified_data = {"XMLBIBLE": {"@biblename": bible_name, "BIBLEBOOK": []}}

    book_index = 1
    for book_name, chapters in data[0].items():
        book_data = {"@bnumber": book_index, "@bname": book_name, "CHAPTER": []}

        for chapter_number, verses in chapters.items():
            chapter_data = {"@cnumber": chapter_number, "VERS": []}

            for verse_number, verse_text in verses.items():
                verse_data = {"@vnumber": verse_number, "#text": verse_text}
                chapter_data["VERS"].append(verse_data)

            book_data["CHAPTER"].append(chapter_data)

        modified_data["XMLBIBLE"]["BIBLEBOOK"].append(book_data)
        book_index += 1

    return xmltodict.unparse(modified_data, pretty=True)


def main() -> None:
    """Entry point used when running this module as a script."""
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "spider.bible_id.json")
    with open(json_path) as f:
        data = json.load(f)

    xml_data = generate_xml_from_data(data, bible_name="TPT")

    xml_path = os.path.join(base_dir, "spider.bible_id.xml")
    with open(xml_path, "w") as f:
        f.write(xml_data)


if __name__ == "__main__":
    main()
