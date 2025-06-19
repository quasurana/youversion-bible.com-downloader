import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bible.data.generate_xml import generate_xml_from_data


def test_generate_xml_basic():
    sample_json = [
        {
            "Genesis": {
                "1": {
                    "1": "In the beginning",
                    "2": "The earth was without form"
                },
                "2": {
                    "1": "Thus the heavens and the earth were finished"
                }
            }
        }
    ]

    xml_output = generate_xml_from_data(sample_json, bible_name="TEST")

    assert "<XMLBIBLE biblename=\"TEST\">" in xml_output
    assert "<BIBLEBOOK bnumber=\"1\" bname=\"Genesis\">" in xml_output
    assert "<CHAPTER cnumber=\"1\">" in xml_output
    assert "<VERS vnumber=\"1\">In the beginning</VERS>" in xml_output
