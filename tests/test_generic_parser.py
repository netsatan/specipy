import os.path
from unittest import TestCase

from specipy.parsers.generic_parser import GenericParser
from specipy.parsers.results import ParsingResult
from specipy.parsers.structure.code_structure_definitions import StructureEnum


class GenericParserTests(TestCase):
    base_path = os.path.dirname(__file__)

    def __load_test_file_old_python(self):
        with open(f"{self.base_path}/examples/complex_number_old_python.py") as source_code:
            fetched_source = source_code.read()
        return fetched_source

    def __load_test_file_modern_python(self):
        with open(f"{self.base_path}/examples/simple_addition_modern_python.py") as source_code:
            fetched_source = source_code.read()
        return fetched_source

    def test_can_get_file_structure_for_old_python(self):
        # @:given There's a file with docstrings
        fetched_source: str = self.__load_test_file_old_python()

        # @:when It is run through a docstring parser
        generic_parser = GenericParser()
        parsing_result: ParsingResult = generic_parser.parse(fetched_source)

        # @:then Parser understands the structure
        self.assertEqual(len(parsing_result.classes), 3)
        self.assertEqual(len(parsing_result.functions), 2)
        self.assertListEqual([x.name for x in parsing_result.classes], ["BaseClassForTest", "SomeTest", "ComplexNumber"])
        self.assertEqual(parsing_result.classes[0].structure_type, StructureEnum.CLASS)

    def test_can_get_file_structure_for_modern_python(self):
        # @:given There's a file with docstrings
        fetched_source: str = self.__load_test_file_modern_python()

        # @:when It is run through a docstring parser
        generic_parser = GenericParser()
        parsing_result: ParsingResult = generic_parser.parse(fetched_source)

        # @:then Parser understands the structure
        self.assertEqual(len(parsing_result.classes), 2)
        self.assertEqual(len(parsing_result.functions), 2)
        self.assertListEqual([x.name for x in parsing_result.classes], ["MathOperation", "Addition"])
        self.assertEqual(parsing_result.classes[0].structure_type, StructureEnum.CLASS)
