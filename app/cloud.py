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
        if status == "SUSPENDED":
            self.client.resume(self.info)
            return 10 # wait time
        elif status == "TERMINATED":
            self.client.start(self.info)
            return 20 # wait time
        else:
            raise Exception("Can't turn on instance")

    def turn_off(self):
        self.client.stop(self.info)
