from src.network import *


def miss_field_exception(field_name):
    raise Exception("Agent initialization without %s" % field_name)


def config_self(field_name, options, self):
    if field_name not in options:
        miss_field_exception(field_name)
    else:
        setattr(self, field_name, options[field_name])


def assert_node(should_be_node):
    assert isinstance(should_be_node, Node), "Requires type: Node, get type: " + type(should_be_node).__name__


def assert_path(should_be_path):
    assert isinstance(should_be_path, Path), "Requires type: Path, get type: " + type(should_be_path).__name__


def assert_type(o, c):
    assert isinstance(o, c), "Requires type: %s, get %s" % (c.__name__, type(o).__name__)
