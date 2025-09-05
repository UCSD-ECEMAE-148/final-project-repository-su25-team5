def run(self):
    with self.lock:
        if self.data_store.get("new_cmd", False):
            angle = self.data_store.get("angle", 0.0)
            throttle = self.data_store.get("throttle", 0.0)
            self.data_store["new_cmd"] = False
        else:
            # No new ROS command: safe fallback values
            angle = 0.0
            throttle = 0.0

    return float(angle), float(throttle)

