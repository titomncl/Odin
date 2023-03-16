import os

import pytest

from Odin.odin.source.core.yaml_parser import Parser


@pytest.fixture(scope="module")
def tmp_dir(tmp_path_factory):
    tmp_path = tmp_path_factory.getbasetemp()

    yield str(tmp_path).replace("\\", "/")


@pytest.fixture(scope="module")
def yaml_file(tmp_dir):
    yield os.path.join(tmp_dir, "yaml_file.yaml").replace("\\", "/")


@pytest.fixture(scope="module")
def parser(yaml_file):
    p = Parser.open(yaml_file)

    if not p:
        p = Parser.new(yaml_file, dict())

    yield p



def test_parser_new(yaml_file):
    p = Parser.new(yaml_file, dict())

    assert p.filepath == yaml_file
    assert p.data == dict()
    assert os.path.isfile(yaml_file) is True


def test_parser_open(parser, yaml_file):
    p = Parser.open(yaml_file)

    assert p.filepath == parser.filepath
    assert p.data == parser.data


def test_parser_open_error():
    assert Parser.open("") is None


def test_parser_write(parser):
    data = {1: 2}
    parser.write(data)

    assert parser.data == data


def test_parser_filepath_setter(parser):
    path = "path"
    parser.filepath = path

    assert parser.filepath == path
