from xml.etree import ElementTree

from b_lambda_layer_common.util.xml_to_dict import XmlToDict


def test_FUNC_convert_WITH_dummy_xml_string_EXPECT_successful_conversion() -> None:
    """
    Checks whether string representing xml can be converted to a dict successfully.

    :return: No return.
    """
    dictionary = XmlToDict('<element></element>').convert()

    assert dictionary == {'element': None}


def test_FUNC_convert_WITH_dummy_xml_document_EXPECT_successful_conversion() -> None:
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
