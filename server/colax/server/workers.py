from collections import defaultdict
from typing import List


class ServiceWorkerDesc:
    def __init__(self, info: dict):
        self.host = info["Address"]
        self.port = info["Port"]


class WorkerManager:

    service_prefix = "colax-worker-"

    def __init__(self):
        self.service_map = defaultdict(list)

    def service_name(self, language: str) -> str:
        return f"{self.service_prefix}{language}"

    def get_services(self, language: str) -> List[ServiceWorkerDesc]:
        key = self.service_name(language)
        return self.service_map.get(key, [])

    def update_from_consul(self, consul_sd: dict) -> None:
        new_map = defaultdict(list)
        for _, info in consul_sd.items():
            service_name = info["Service"]
            desc = ServiceWorkerDesc(info)
            new_map[service_name].append(desc)
        self.service_map = new_map
