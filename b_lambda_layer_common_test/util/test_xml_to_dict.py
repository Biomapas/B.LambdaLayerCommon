from xml.etree import ElementTree

from b_lambda_layer_common.source.python.util.xml_to_dict import XmlToDict


def test_string_xml_to_dict() -> None:
    """
    Checks whether string representing xml can be converted to a dict successfully.

    :return: No return.
    """
    dictionary = XmlToDict('<element></element>').convert()

    assert dictionary == {'element': None}


def test_xml_object_to_dict() -> None:
    """
    Checks whether xml element can be converted to a dict successfully.

    :return: No return.
    """
    xml_element = ElementTree.fromstring(
        '<element>'
        '<list-element>E1</list-element>'
        '<list-element>E2</list-element>'
        '<list-element>E3</list-element>'
        '</element>'
    )

    dictionary = XmlToDict(xml_element).convert()

    assert dictionary == {'element': {'list-element': ['E1', 'E2', 'E3']}}
