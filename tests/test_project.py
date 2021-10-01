import binascii
import os

import pytest

from Odin import Project


@pytest.fixture(scope="module")
def tmp_dir(tmp_path_factory):
    tmp_path = tmp_path_factory.getbasetemp()

    yield str(tmp_path).replace("\\", "/")


@pytest.fixture(scope="session")
def name():
    yield str(binascii.b2a_hex(os.urandom(2))).split("'")[1].upper()


@pytest.fixture(scope="module")
def project(tmp_dir, name):
    try:
        prj = Project.load(tmp_dir, name)
    except RuntimeError:
        prj = Project.new(tmp_dir, name)

    yield prj


def test_project_new(tmp_dir, name):

    prj = Project.new(tmp_dir, name)

    prj_data = os.path.join(tmp_dir, name, "odin.yaml")

    assert prj.name == name
    assert prj.project_path == tmp_dir
    assert os.path.isfile(prj_data) is True


def test_project_load(project, tmp_dir, name):
    prj = Project.load(tmp_dir, name)

    prj_data = os.path.join(tmp_dir, name, "odin.yaml")

    assert prj.name == project.name
    assert prj.data == project.data
    assert os.path.isfile(prj_data) is True


def test_project_load_error():
    with pytest.raises(RuntimeError):
        Project.load("bad_root", "bad_name")


def test_project_list(project, tmp_dir):
    prj_list = project.list(tmp_dir)

    assert isinstance(prj_list, list)
    assert project.name in prj_list
