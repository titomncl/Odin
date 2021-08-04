try:
    from typing import NoReturn, Optional, Union, Dict
except ImportError:
    pass

from ..globals import Logger as log


class Parser(object):
    """
    Yaml parser.

    Usage:
        p = Parser.open('filepath')\n
        p.filepath = 'your/new/file/path.yaml'\n
        p.data = {'new': 'data'}\n

    Parameters:
        filepath (str): path/of/your/file.yaml
        data (dict): data to put in the yaml file

    """

    def __init__(self, filepath=None, data=None):
        # type: (Optional[str], Optional[dict]) -> Parser
        self.__file = filepath or str()
        self.__data = data or dict()

    @classmethod
    def new(cls, filepath, data=None):
        # type: (str, Optional[Dict[str]]) -> Parser
        """
        Create a new yaml file

        Args:
            filepath (str): filepath of the yaml file
            data (dict):

        Returns:
            Parser: Parser object that contain the new yaml file with its data

        """
        import yaml
        import os
        from CommonTools.os_ import make_dirs

        path, _ = os.path.split(filepath)
        make_dirs(path)

        content = yaml.safe_dump(data)

        with open(filepath, "w") as file_:
            file_.write(content)

        return cls(filepath, data)

    def write(self, data=None):
        # type: (Optional[dict]) -> NoReturn
        """
        Write the data in the yaml file

        Args:
            data (dict):

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
        # type: (str) -> NoReturn
        self.__file = value

    @property
    def data(self):
        # type: () -> dict
        return self.__data

    @data.setter
    def data(self, values):
        # type: (dict) -> NoReturn
        self.__data = values

    @classmethod
    def open(cls, filepath):
        # type: (str) -> Union[Parser, None]
        """
        Generate a Parser object from the given yaml file

        Args:
            filepath (str): yaml file path to open

        Returns:
            Parser: Parser object that contain the yaml file with its data

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
