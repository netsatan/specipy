from unittest import TestCase

from py_d2 import Direction

from specifipy.diagram_engines.hashable_connection import D2HashableConnection


class TestDiagramEngines(TestCase):
    def test_connections_uniqueness(self):
        connection_1 = D2HashableConnection("a", "b", "some_label", Direction.TO)
        connection_2 = D2HashableConnection("a", "b", "some_label", Direction.TO)
        assert connection_1 == connection_2

    def test_connections_hash(self):
        connection_1 = D2HashableConnection("a", "b", "some_label", Direction.TO)
        assert isinstance(connection_1.__hash__(), int)

    def test_connections_not_equal(self):
        connection_1 = D2HashableConnection("a", "b", "some_label", Direction.TO)
        connection_2 = D2HashableConnection("a", "b", "some_label2", Direction.TO)
        connection_3 = D2HashableConnection("a1", "b", "some_label", Direction.TO)
        connection_4 = D2HashableConnection("a", "b1", "some_label", Direction.TO)
        connection_5 = D2HashableConnection("a", "b", "some_label", Direction.FROM)
        assert connection_1 != connection_2
        assert connection_1 != connection_3
        assert connection_1 != connection_4
        assert connection_1 != connection_5
