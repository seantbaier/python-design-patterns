import json
import xml.etree.ElementTree as etree
from typing import Union
from pprint import pprint


class JSONDataExtractor:
    def __init__(self, filepath: str) -> None:
        self.data = dict()
        with open(filepath, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLDataExtractor:
    def __init__(self, filepath: str) -> None:
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def data_extraction_factory(filepath: str) -> Union[JSONDataExtractor, XMLDataExtractor]:
    if filepath.endswith("json"):
        return JSONDataExtractor(filepath)
    elif filepath.endswith("xml"):
        return XMLDataExtractor(filepath)
    else:
        raise ValueError("Cannot extract data from {}".format(filepath))


def extract_data_from(filepath: str):
    factory_obj = None
    try:
        factory_obj = data_extraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj


def main():
    json_factory = extract_data_from("factory/data/movies.json")
    json_data = json_factory.parsed_data
    print(f"Found: {len(json_data)} movies")
    pprint(json_data)

    xml_factory = extract_data_from("factory/data/person.xml")
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//person[lastName='Liar']")

    print(f"found: {len(liars)} persons\n")
    for liar in liars:
        firstname = liar.find("firstName").text
        print(f"first name: {firstname}")
        lastname = liar.find("lastName").text
        print(f"last name: {lastname}")
        [print(f"phone number ({p.attrib['type']}):", p.text) for p in liar.find("phoneNumbers")]
        print()


if __name__ == "__main__":
    main()
