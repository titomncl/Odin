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

@pytest.fixture(scope="session")
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
    except KeyError:  # TODO change with RuntimeError
        asset = Asset.new(project, asset_name, "CHARA")

    yield asset


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


def test_asset_load(project, asset, asset_name):
    asset_ = Asset.load(project, asset_name, "CHARA")

    assert asset_.name == asset.name


def test_asset_load_error_bad_type(project, asset, asset_name):
    with pytest.raises(KeyError):  # TODO add proper message
        Asset.load(project, asset_name, "bad_asset_type")


def test_asset_load_error_bad_name(project, asset):
    with pytest.raises(KeyError):  # TODO add proper message
        Asset.load(project, "bad_asset_name", "CHARA")


def test_asset_list(project, asset):
    asset_list = asset.list(project, "CHARA")

    assert isinstance(asset_list, list)
    assert asset.name in asset_list
