try:
    from typing import NoReturn, Optional
except ImportError:
    pass


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

    def new(self, data=None, filepath=None):
        # type: (dict, str) -> Parser
        """
        Create a new yaml file

        Args:
            data (dict):
            filepath (str): filepath of the yaml file

        Returns:
            Parser: Parser object that contain the new yaml file with its data

        """
        import yaml
        import os
        from CommonTools.os_ import make_dirs

        self.filepath = filepath or self.filepath
        self.data = data or self.data

        path, _ = os.path.split(self.filepath)
        make_dirs(path)

        content = yaml.safe_dump(self.data)

        with open(self.filepath, "w") as file_:
            file_.write(content)

        return self

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
        import os

        self.data = data or self.data

        if os.path.isfile(self.filepath):
            with open(self.filepath, "w") as file_:
                yaml.dump(self.data, file_)
        else:
            raise RuntimeError("Use 'Parser.new()' to create a new yaml file.")

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
        # type: (str) -> Parser
        """
        Generate a Parser object from the given yaml file or create one if the yaml file does not exists

        Args:
            filepath (str): yaml file path to open

        Returns:
            Parser: Parser object that contain the yaml file with its data

        """
        import yaml

        try:
            data = yaml.load(open(filepath, "r"), Loader=yaml.Loader)

            return cls(filepath, data)
        except IOError:
            data = dict()
            return cls(filepath, data).new()
