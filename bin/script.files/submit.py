# import logging
# import sys
# from typing import Any, List

# logger = logging.getLogger(__name__)


# def main():
#     language = sys.argv[1]
#     source_file = sys.argv[2]
#     config = load_config()

#     test_data = load_test_data()


# class ColaxConfig:
#     def __init__(self, config_dict: dict):
#         self.conf = config_dict

#     @property
#     def project_name(self) -> str:
#         return self.conf["project_name"]


# def load_config() -> ColaxConfig:
#     config_file = "colax.proj.conf"
#     conf_dict = {}
#     with open(config_file, "rt") as fp:
#         for line in fp:
#             if line.startswith("#"):
#                 continue
#             key, value = line.split("=", 1)
#             key = key.strip()
#             value = value.strip()
#             conf_dict[key] = value
#     return ColaxConfig(conf_dict)


# def load_test_data() -> List[Any]:
#     # TODO
#     pass


# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s - %(message)s")
#     main()
