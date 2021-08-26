import re
from typing import List, Union

import requests

version_pattern = re.compile(r"^(?P<major>\d).(?P<minor>\d).(?P<micro>\d)b?(?P<beta>\d*)?$")


def new_update(version, is_beta):
    # type: (str, bool) -> Union[None, str]
    url = "https://api.github.com/repos/titomncl/odin/tags"

    r = requests.request(method="GET", url=url)

    tags = r.json()

    actual_version = version_pattern.match(version).groupdict()

    for tag in tags:
        last_version = version_pattern.match(tag["name"])

        if last_version:
            last_version = last_version.groupdict()

            actual_v = [int(actual_version["major"]), int(actual_version["minor"]), int(actual_version["micro"])]
            if actual_version["beta"]:
                actual_v.append(int(actual_version["beta"]))

            last_v = [int(last_version["major"]), int(last_version["minor"]), int(last_version["micro"])]
            if last_version["beta"]:
                last_v.append(int(last_version["beta"]))

            if version_verification(actual_v, last_v, is_beta):
                return tag["name"]


def version_verification(actual, new, is_beta):
    # type: (List[int], List[int], bool) -> bool
    if len(actual) < len(new):
        if is_beta:
            new.pop(-1)
            if actual > new:
                return False
            else:
                return True
        else:
            return False
    elif len(actual) > len(new):
        actual.pop(-1)
        if actual > new:
            return False
        else:
            return True
    elif len(new) == 4 and not is_beta:
        return False
    else:
        if actual < new:
            return True
        else:
            return False
