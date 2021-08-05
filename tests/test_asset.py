import pytest
import os
import binascii

from Odin import Project, Asset


@pytest.fixture(scope="module")
def tmp_dir(tmp_path_factory):
    tmp_path = tmp_path_factory.getbasetemp()

    yield str(tmp_path).replace("\\", "/")


@pytest.fixture(scope="session")
def name():
    yield str(binascii.b2a_hex(os.urandom(2))).split("'")[1].upper()

@pytest.fixture(scope="function")
def asset_name():
    yield str(binascii.b2a_hex(os.urandom(2))).split("'")[1].upper()


@pytest.fixture(scope="module")
def project(tmp_dir, name):
    try:
        prj = Project.load(tmp_dir, name)
    except RuntimeError:
        prj = Project.new(tmp_dir, name)

    yield prj


@pytest.fixture(scope="module")
def asset(project, asset_name):
    try:
        asset = Asset.load(project, asset_name, "CHARA")
    except RuntimeError:
        asset = Asset.new(project, asset_name, "CHARA")


parameters = [
    (pytest.lazy_fixture("project"), "C01", "CHARA"),
    (pytest.lazy_fixture("project"), "P01", "PROPS"),
    (pytest.lazy_fixture("project"), "S01", "SET"),
    (pytest.lazy_fixture("project"), "F01", "FX"),
]


@pytest.mark.parametrize("prj, asset_name, asset_type", parameters)
def test_asset_new(prj, asset_name, asset_type):

    asset = Asset.new(prj, asset_name, asset_type)

    assert asset.name == asset_name
    assert asset.asset_type == asset_type
    assert asset_name in asset.list(prj, asset_type)


def test_asset_load(asset, tmp_dir, name):
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
