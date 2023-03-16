from pprint import pprint

from odin.source.core.yaml_parser import Parser


class BaseObject(object):
    def __init__(self, id, code):
        self.type = None
        self.code = code
        self.id = id

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, value: str):
        if not isinstance(value, str):
            raise ValueError(f"The code should be a string, not a {type(value)}")
        self.__code = value

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int):
        if not isinstance(value, int):
            raise ValueError(f"The id should be an integer, not a {type(value)}")
        self.__id = value

    @classmethod
    def _new(cls, **kwargs):
        code = kwargs["code"]
        kwargs["id"] = id(code)
        return cls(**kwargs)

    def __dict__(self):
        return {
            "id": self.id,
            "type": self.type,
            "code": self.code,
        }

    def __str__(self):
        return str(self.__dict__())


class Odin(object):
    entity_data = None

    @classmethod
    def create(cls, entity_type: str, data: dict) -> BaseObject:
        if not entity_type:
            raise RuntimeError("Parameter entity_type not specified")
        if not data:
            raise RuntimeError("Parameter data not specified")

        exec(f"cls.entity_data = {entity_type}._new(**data)")

        return cls().entity_data


class Project(BaseObject):
    def __init__(self, id, code):
        super(Project, self).__init__(id, code)
        self.type = self.__class__.__name__


class Asset(BaseObject):
    def __init__(self, id, code, project):
        super(Asset, self).__init__(id, code)
        self.type = self.__class__.__name__
        self.project = project


class Task(BaseObject):
    def __init__(self, _id, _code):
        super(Task, self).__init__(_id, _code)
        self.type = self.__class__.__name__


class Sequence(BaseObject):
    def __init__(self, _id, _code):
        super(Sequence, self).__init__(_id, _code)
        self.type = self.__class__.__name__


class Shot(BaseObject):
    def __init__(self, _id, _code):
        super(Shot, self).__init__(_id, _code)
        self.type = self.__class__.__name__


class Path(BaseObject):
    def __init__(self, _id, _code):
        super(Path, self).__init__(_id, _code)
        self.type = self.__class__.__name__


if __name__ == '__main__':
    # prj = Odin.create("Project", {"code": "prj_test"})

    # asset = Odin.create("Asset", {"code": "asset_test", "project": prj})

    # print(asset)

    yml_file = Parser.open(filepath="./odin/config/db.yml")

    print(yml_file.data)
