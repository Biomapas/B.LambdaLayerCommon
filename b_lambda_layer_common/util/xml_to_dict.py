from collections import defaultdict
from typing import Dict, Any, Union
from xml.etree import ElementTree
from xml.etree.ElementTree import Element


class XmlToDict:
    """
    Class that is responsible for converting xml to dict.
    """
    def __init__(self, xml_document: Union[str, Element]) -> None:
        """
        Constructor.

        :param xml_document: Xml document.
        """
        if isinstance(xml_document, str):
            self.__xml_document: Element = ElementTree.fromstring(xml_document)
        elif isinstance(xml_document, Element):
            self.__xml_document: Element = xml_document

    def convert(self) -> Dict[Any, Any]:
        """
        Initiates conversion from xml to dict.

        :return: Dictionary representation of an xml document.
        """
        return self.__etree_to_dict(self.__xml_document)

    @staticmethod
    def __etree_to_dict(xml_element: Element) -> Dict[Any, Any]:
        dictionary = {xml_element.tag: {} if xml_element.attrib else None}
        children = list(xml_element)
        if children:
            dd = defaultdict(list)
            for dc in map(XmlToDict.__etree_to_dict, children):
                for k, v in dc.items():
                    dd[k].append(v)
            dictionary = {xml_element.tag: {k: v[0] if len(v) == 1 else v for k, v in dd.items()}}
        if xml_element.attrib:
            dictionary[xml_element.tag].update(('@' + k, v) for k, v in xml_element.attrib.items())
        if xml_element.text:
            text = xml_element.text.strip()
            if children or xml_element.attrib:
                if text:
                    dictionary[xml_element.tag]['#text'] = text
            else:
                dictionary[xml_element.tag] = text
        return dictionary
