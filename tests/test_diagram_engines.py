from unittest import TestCase

from py_d2 import Direction

from specifipy.diagram_engines.hashable_connection import D2HashableConnection


class TestDiagramEngines(TestCase):
    def test_connections_uniqueness(self):
        connection_1 = D2HashableConnection("a", "b", "some_label", Direction.TO)
        connection_2 = D2HashableConnection("a", "b", "some_label", Direction.TO)
        assert connection_1 == connection_2
