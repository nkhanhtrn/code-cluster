from google.cloud import compute_v1
from time import sleep


class CloudMachine():
    def __init__(self, project, instance, zone):
        self.client = compute_v1.InstancesClient()
        self.info = {
            "project": project,
            "instance": instance,
            "zone": zone
        }

    def get_status(self):
        return self.client.get(self.info).status

    def turn_on(self) -> int:
        status = self.get_status()
        if status == "SUSPENDED":
            self.client.resume(self.info)
        elif status == "TERMINATED":
            self.client.start(self.info)

        while status != "RUNNING":
            sleep(3)
            status = self.get_status()

    def turn_off(self):
        status = "RUNNING"
        self.client.stop(self.info)
        while status != "TERMINATED":
            sleep(3)
            status = self.get_status()
