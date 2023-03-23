import xmltodict
from src.data.protocols.converter.converter_xml_to_dict import ConverterXmlToDict

class XmlToDictAdapter(ConverterXmlToDict):
    def converter(self, xml: str) -> dict:
        xml_to_dict = xmltodict.parse(xml)
        return xml_to_dict