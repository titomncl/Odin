import os
import re
import time
import keyboard
import pytest
import win32clipboard as cb

def glob_path_recursive(path, content):
    for dir_path, dirs, _ in os.walk(path):
        for dir in dirs:
            file_path = os.path.join(dir_path, dir).replace("\\", "/")
            if content in file_path:
                os.rename(file_path, file_path.replace(content, "MOUNTAIN"))
            else:
                files = os.listdir(file_path)
                for f in files:
                    if content in f:
                        new_name = str(f).replace(content, "MOUNTAIN")
                        os.rename(os.path.join(file_path, f), os.path.join(file_path, new_name))


def bla():

    pattern = r"(?P<name>SEA)_([A-Za-z_]+)(?P<tx_type>BaseColor|Height|Metalness|Normal|Roughness).(?P<udim>[0-9]+).exr"

    path = r"C:\Users\t.nicole\Desktop\001"

    files = os.listdir(path)

    regex = re.compile(pattern)

    for f in files:
        is_match = regex.match(f)

        if is_match:
            filename = is_match.groupdict()
            new_filename = filename["name"] + "_" +  filename["tx_type"] + "." + filename["udim"] + ".exr"

            os.rename(os.path.join(path, f), os.path.join(path, new_filename))


def camelize(text):
    # type: (str) -> str
    text_split = re.split('[_ -]', text)

    camelize_text = list(map(str.title, text_split))
    camelize_text[0] = camelize_text[0].lower()

    return "".join(camelize_text)


def decamelize(text):

    decamelize_text = ""

    for letter in text:
        if letter.isupper():
            decamelize_text += "_"
        decamelize_text += letter.lower()


    # text_split = [t for t in re.split(r"([A-Z][a-z]+)", text) if t]
    #
    # decamelize_text = ""
    # for text_part in text_split:
    #     text_part = text_part.lower()
    #     if not decamelize_text:
    #         decamelize_text = text_part
    #     else:
    #         decamelize_text += "_" + text_part

    return  decamelize_text



def rename_file():
    pattern = r"(START_BATTLEFIELD)_(LAYOUT)_(?P<version>[0-9]+)."

    path = "X:/VSPA/DATA/FILM/SEQ/S120/S120P110/LAYOUT/VERSION"

    files = [f for f in os.listdir(path) if re.match(pattern, f)]

    regex = re.compile(pattern)

    for f in files:
        is_match = regex.match(f)

        if is_match:
            filename = is_match.groupdict()
            new_filename = "S120P110_LAYOUT_" + filename["version"]

            if ".ma" in f:
                new_filename += ".ma"
            else:
                new_filename += ".hip"

            # print(os.path.join(path, f), os.path.join(path, new_filename))
            os.rename(os.path.join(path, f), os.path.join(path, new_filename))


# def write_clipboard():
    # cb.OpenClipboard()
    # test = '''{"SessionId":"eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJidSI6IjEwMDExIiwic2kiOiI2MGE5YWQ4NC1lOTNkLTQ4MGYtODBkNi1hZjM3NDk0ZjJlMjIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjQ1NTc4NDU5IiwiaWQiOiJhNmQzMWY4OC0zODEwLTRiNWUtOTc0OC0xZmQ1N2Q2Nzc3ZjQiLCJ0IjoiMSIsImwiOiJlbi1HQiIsImRjIjoiMzY0NCIsImFlZCI6IjIwMjItMDktMjRUMTI6MDc6MzkuNzA1WiIsImR0IjoiMSIsImVkIjoiMjAyMi0xMC0xMFQxMjowNzozOS43MDVaIiwiY2VkIjoiMjAyMi0wOS0xMVQxMjowNzozOS43MDVaIiwiaXAiOiIyYTAxOmUwYToxNzo0NzA6ZjFmYTo1MTljOjJjOTI6MzMxOCIsImMiOiJWSUxMRSIsInN0IjoiNjAiLCJjbyI6IkZSQSIsIm5iZiI6MTY2MjgxMTY1OSwiZXhwIjoxNjY1NDAzNjU5LCJpc3MiOiJhc2NlbmRvbi50diIsImF1ZCI6ImFzY2VuZG9uLnR2In0.y6dK5esHai7lc60RvVV-SCnHJ6m1UBa6XR0UTG1qXSA","PasswordIsTemporary":false,"Subscriber":{"FirstName":"Thomas","LastName":"NICOLE","HomeCountry":"FRA","Id":45578459,"Email":"thomas-nicole@hotmail.fr","Login":"thomas-nicole@hotmail.fr"},"Country":"FRA","data":{"subscriptionStatus":"active","subscriptionToken":"eyJraWQiOiIxIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJFeHRlcm5hbEF1dGhvcml6YXRpb25zQ29udGV4dERhdGEiOiJGUkEiLCJTdWJzY3JpcHRpb25TdGF0dXMiOiJhY3RpdmUiLCJTdWJzY3JpYmVySWQiOiI0NTU3ODQ1OSIsIkZpcnN0TmFtZSI6IlRob21hcyIsIkxhc3ROYW1lIjoiTklDT0xFIiwiZXhwIjoxNjYzMTU3MjU5LCJTZXNzaW9uSWQiOiJleUpoYkdjaU9pSm9kSFJ3T2k4dmQzZDNMbmN6TG05eVp5OHlNREF4THpBMEwzaHRiR1J6YVdjdGJXOXlaU05vYldGakxYTm9ZVEkxTmlJc0luUjVjQ0k2SWtwWFZDSjkuZXlKaWRTSTZJakV3TURFeElpd2ljMmtpT2lJMk1HRTVZV1E0TkMxbE9UTmtMVFE0TUdZdE9EQmtOaTFoWmpNM05EazBaakpsTWpJaUxDSm9kSFJ3T2k4dmMyTm9aVzFoY3k1NGJXeHpiMkZ3TG05eVp5OTNjeTh5TURBMUx6QTFMMmxrWlc1MGFYUjVMMk5zWVdsdGN5OXVZVzFsYVdSbGJuUnBabWxsY2lJNklqUTFOVGM0TkRVNUlpd2lhV1FpT2lKaE5tUXpNV1k0T0Mwek9ERXdMVFJpTldVdE9UYzBPQzB4Wm1RMU4yUTJOemMzWmpRaUxDSjBJam9pTVNJc0ltd2lPaUpsYmkxSFFpSXNJbVJqSWpvaU16WTBOQ0lzSW1GbFpDSTZJakl3TWpJdE1Ea3RNalJVTVRJNk1EYzZNemt1TnpBMVdpSXNJbVIwSWpvaU1TSXNJbVZrSWpvaU1qQXlNaTB4TUMweE1GUXhNam93Tnpvek9TNDNNRFZhSWl3aVkyVmtJam9pTWpBeU1pMHdPUzB4TVZReE1qb3dOem96T1M0M01EVmFJaXdpYVhBaU9pSXlZVEF4T21Vd1lUb3hOem8wTnpBNlpqRm1ZVG8xTVRsak9qSmpPVEk2TXpNeE9DSXNJbU1pT2lKV1NVeE1SU0lzSW5OMElqb2lOakFpTENKamJ5STZJa1pTUVNJc0ltNWlaaUk2TVRZMk1qZ3hNVFkxT1N3aVpYaHdJam94TmpZMU5EQXpOalU1TENKcGMzTWlPaUpoYzJObGJtUnZiaTUwZGlJc0ltRjFaQ0k2SW1GelkyVnVaRzl1TG5SMkluMC55NmRLNWVzSGFpN2xjNjBSdlZWLVNDbkhKNm0xVUJhNlhSMFVURzFxWFNBIiwiaWF0IjoxNjYyODExNjU5LCJTdWJzY3JpYmVkUHJvZHVjdCI6IkYxIFRWIFBybyBBbm51YWwiLCJqdGkiOiIzMDQzYjRjZi01NmQ1LTQ1ODAtYmIzZC03NDJkYWJjNzk5NTQifQ.rBbMYLIUuUqRe9cGZRH3OXvYpL-CCcxEGvklejkO6AZVKET0wA3xX6Oz8w-Ea1Q48-51oNZzxesYndfZiTBH04WOFRaT20dxXI2N_LVkrplPJ6CMbiwXGSpUMMyD3U3f035IX3aOlDDml-XITglRyAU-qe05lf_45gEY6BjtaQspfeM_CAEwNVT3H8UfEslqLnWXZ9qKRhopcjR1BmGAFvt8ZEHY4mULnf5WjTEZbM6fz2zhfmOUZqZA6w18AvOF4YR0W9Fn6cvhn_nlo1o1AVymBbS8c5m2jXhrrbjK4W6eHdV-Dz1BcH4HlOlHdLZNp2yV64rRqm0Z1rOYrohoPA"}}'''
    # keyboard.write(test)
    # cb.CloseClipboard()


class BaseObject(object):
    def __init__(self, _id, _code):
        self.type = None
        self.code = _code
        self.id = _id

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
    def _new(cls, code):
        cls.id = id(code)
        return cls(cls.id, code)

    def __dict__(self):
        return {
            "id": self.id,
            "type": self.type,
            "code": self.code,
        }

    def __str__(self):
        return str(self.__dict__())


class Odin(object):
    entity_data = {}

    @classmethod
    def create(cls, entity_type: str, data: dict) -> dict:
        if not entity_type:
            raise RuntimeError("Parameter entity_type not specified.")
        if not data:
            raise RuntimeError("parameter data not specified")

        exec(f"cls.entity_data = {entity_type}._new(data['code'])")

        return cls().entity_data

class Project(BaseObject):
    def __init__(self, _id, _code):
        super(Project, self).__init__(_id, _code)
        self.type = self.__class__.__name__


class Asset(BaseObject):
    def __init__(self, _id, _code):
        super(Asset, self).__init__(_id, _code)
        self.type = self.__class__.__name__


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


class Ctx:
    def __init__(self, bar):
        self.bar = bar

    def __enter__(self):
        if self.bar == "a":
            return self
        else:
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.bar == "a":
            return True
        else:
            return False

foo = [("b", False),
       ("a", True),
       ("c", False),
       ("a", True)]

@pytest.mark.parametrize("entity, expected", foo)
def test_foobarbaz(entity, expected):
    is_conform = True
    created = False
    deleted = False

    try:
        with Ctx(entity) as e:
            if e.bar == "a":
                created = True
            else:
                created = False
            raise NotImplementedError("NI")
    except NotImplementedError:
        deleted = False
    else:
        deleted = True
    finally:
        if created and deleted:
            is_conform = True
        else:
            is_conform = False

    assert is_conform == expected

# if __name__ == '__main__':

    # data = {"code": "prj_test"}

    # prj = Odin.create("Project", data)

    # print(prj)

    # Project = {
    #     "id": 1,
    #     "type": "Project",
    #     "code": "prj_name",
    #     "assets": [{
    #         "id": 11,
    #         "type": "Asset",
    #         "code": "asset_name",
    #         "tasks": [{
    #             "id": 111,
    #             "type": "Task",
    #             "name": "task_name",
    #             "status": "ip",
    #         }]
    #     }],
    #     "sequences": [{
    #         "id": 12,
    #         "type": "Sequence",
    #         "code": "prj_S0123",
    #         "shots": [{
    #             "id": 121,
    #             "type": "Shot",
    #             "code": "prj_S0123_P4567",
    #             "tasks": [{
    #                 "id": 1211,
    #                 "type": "Task",
    #                 "name": "task_name",
    #                 "status": "ip",
    #             }],
    #             "assets": [{
    #                 "id": 11,
    #                 "type": "Asset",
    #                 "code": "asset_name"
    #             }]
    #         }]
    #     }]
    # }


    # time.sleep(4)
    # write_clipboard()

    # a = 3
    # b = 6
    #
    # if a > 5 or b != 3:
    #     b = 4
    # else:
    #     b = 2
    #
    # print(b)
    # path = "Y:/VSPA/OUT/SEQ/S170/S170P120/COMPOSITING/003"

    # files = [f for f in os.listdir(path)]

    # for f in files:
    #     if "S1170P120_COMPOSITING" in f:
    #         new_name = f.replace("S1170P120_COMPOSITING", "S170P120_COMPOSITING")
    #         os.rename(os.path.join(path, f), os.path.join(path, new_name))
    # rename_file()
    # to_camelize = [
    #     "My_Project",
    #     "My Project",
    #     "my_project",
    #     "my project",
    #     "mY_pRoject",
    #     "My_ultimate project-01"
    # ]
    #
    # to_decamelize = []
    #
    # for each in to_camelize:
    #     t = camelize(each)
    #     print(t)
    #     to_decamelize.append(t)
    #
    # for each in to_decamelize:
    #     t = decamelize(each)
    #     print(t)

    # path = r"D:\PROJECT\VSPA\DATA\LIB\PUBLISH\SET"
    #
    # print(glob_path_recursive(path, "MOUTAIN"))
    # to_decamelize = "myUltimate02Project01"

    # print(decamelize(to_decamelize))


