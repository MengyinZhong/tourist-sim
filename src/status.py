from src.util import *


class STATUS:
    ENTERING = "ENTERING"
    MOVING = "MOVING"
    VISITING = "VISITING"
    LEAVING = "LEAVING"


class WithAt:
    def __init__(self, at_node):
        assert_node(at_node)
        self.at_node = at_node


class WithFromAndTo:
    def __init__(self, from_node, to_node):
        assert_node(from_node)
        assert_node(to_node)

        self.to_node = to_node
        self.from_node = from_node


class EnteringStatus(WithAt):
    def __init__(self, at_node):
        super().__init__(at_node)
        self._status = STATUS.ENTERING

    @property
    def name(self):
        return self._status


class MovingStatus(WithFromAndTo):
    def __init__(self, from_node, to_node):
        super().__init__(from_node, to_node)
        self._status = STATUS.MOVING

    @property
    def name(self):
        return self._status


class VisitingStatus(WithAt):
    def __init__(self, at_node):
        super().__init__(at_node)
        self._status = STATUS.VISITING

    @property
    def name(self):
        return self._status


class LeavingStatus(WithAt):
    def __init__(self, at_node):
        super().__init__(at_node)
        self._status = STATUS.LEAVING

    @property
    def name(self):
        return self._status
