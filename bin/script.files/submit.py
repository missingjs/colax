import base64
import json
import logging
import sys
from typing import Any, List

import requests

logger = logging.getLogger(__name__)


def main():
    language = sys.argv[1]
    source_file = sys.argv[2]
    config = load_config()
    test_data_file = "./colax-test.json"

    s_source = load_file(source_file)
    s_test = load_file(test_data_file)

    data = {
        "project": config.project_name,
        "language": language,
        "test_data": base64_encode(s_test),
        "source_code": base64_encode(s_source),
    }

    url = "http://localhost:6733/solution"

    resp = requests.post(url, json=data)
    print(resp)


def base64_encode(s: str) -> str:
    return base64.standard_b64encode(s.encode()).decode()


def load_file(path: str) -> str:
    with open(path, "rt") as fp:
        return fp.read()


class ColaxConfig:
    def __init__(self, config_dict: dict):
        self.conf = config_dict

    @property
    def project_name(self) -> str:
        return self.conf["project_name"]


def load_config() -> ColaxConfig:
    config_file = "colax.proj.conf"
    conf_dict = {}
    with open(config_file, "rt") as fp:
        for line in fp:
            if line.startswith("#"):
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()
            conf_dict[key] = value
    return ColaxConfig(conf_dict)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s - %(message)s")
    main()
