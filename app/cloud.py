from google.cloud import compute_v1


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
        wait_time = 1
        if status == "SUSPENDED":
            self.client.resume(self.info)
            wait_time = 10
        elif status == "TERMINATED":
            self.client.start(self.info)
            wait_time = 20

        return wait_time

    def turn_off(self):
        self.client.stop(self.info)
