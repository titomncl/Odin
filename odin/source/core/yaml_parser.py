import sys

if sys.version_info > (3, ):

    import typing

    if typing.TYPE_CHECKING:
        from typing import Dict, Optional, Union

from ..globals import Logger as log


class Parser(object):
    """Yaml parser.

    Usage:
        p = Parser.open('filepath')\n
        p.filepath = 'your/new/file/path.yaml'\n
        p.data = {'new': 'data'}\n

    Parameters:
        filepath (str): path/of/your/file.yaml
        data (dict): data to put in the yaml file

    """

    def __init__(self, filepath=None, data=None):
        # type: (Optional[str], Optional[dict]) -> None
        self.__file = filepath or str()
        self.__data = data or dict()

    @classmethod
    def new(cls, filepath, data=None):
        # type: (str, Optional[Dict[str]]) -> Parser
        """Create a new yaml file.

        Args:
            filepath: filepath of the yaml file
            data:

        Returns:
            Parser object that contain the new yaml file with its data

        """
        import os

        import yaml
        from CommonTools.os_ import make_dirs

        path, _ = os.path.split(filepath)
        make_dirs(path)

        content = yaml.safe_dump(data)

        with open(filepath, "w") as file_:
            file_.write(content)

        return cls(filepath, data)

    def write(self, data=None):
        # type: (Optional[dict]) -> None
        """Write the data in the yaml file.

        Raises:
            RuntimeError: if the file does not exist

        """
        import yaml

        self.data = data or self.data

        with open(self.filepath, "w") as file_:
            yaml.dump(self.data, file_)

    @property
    def filepath(self):
        # type: () -> str
        return self.__file

    @filepath.setter
    def filepath(self, value):
        # type: (str) -> None
        self.__file = value

    @property
    def data(self):
        # type: () -> dict
        return self.__data

    @data.setter
    def data(self, values):
        # type: (dict) -> None
        self.__data = values

    @classmethod
    def open(cls, filepath):
        # type: (str) -> Union[Parser, None]
        """Generate a Parser object from the given yaml file.

        Args:
            filepath: yaml file path to open

        Returns:
            Parser object that contain the yaml file with its data

        Raises:
            IOError: if the file specified does not exist

        """
        import yaml

        try:
            data = yaml.load(open(filepath, "r"), Loader=yaml.Loader)

            return cls(filepath, data)
        except IOError as e:
            log.warning(e)
            return None
