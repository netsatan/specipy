import unittest
from enum import Enum
from typing import Union
from unittest.mock import MagicMock

from specifipy.parsers.generic_parser import (
    FileType,
    GenericParser,
    JavaParser,
    ParserFactory,
    PythonParser,
)


class TestParserFactory(unittest.TestCase):
    class FakeFileType(Enum):
        PYTHON = 1
        JAVA = 2
        CPP = 3

    def test_can_return_python_parser(self):
        factory = ParserFactory()
        parser = factory.get_parser(FileType.PYTHON)
        self.assertIsInstance(parser, GenericParser)
        self.assertIsInstance(parser, PythonParser)

    def test_can_return_java_parser(self):
        factory = ParserFactory()
        parser = factory.get_parser(FileType.JAVA)
        self.assertIsInstance(parser, GenericParser)
        self.assertIsInstance(parser, JavaParser)

    def test_fails_at_not_implemented_parser(self):
        factory = ParserFactory()
        mock_file_type = MagicMock(spec=FileType)
        mock_file_type.__value__ = 3
        with self.assertRaises(NotImplementedError):
            factory.get_parser(mock_file_type)
