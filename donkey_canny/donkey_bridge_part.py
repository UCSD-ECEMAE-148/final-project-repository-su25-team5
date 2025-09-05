# donkey_bridge_part.py
import threading

class ROS2BridgePart:
    def __init__(self, data_store):
        """
        data_store: a dict-like object shared between ROS2 node and DonkeyCar
        Example: {"angle": 0.0, "throttle": 0.0, "new_cmd": False}
        """
        self.data_store = data_store
        self.lock = threading.Lock()

    def run(self):
        """
        Returns (angle, throttle) only if a new ROS2 command exists.
        Otherwise, returns (None, None) so joystick/manual control is not overwritten.
        """
        with self.lock:
            # Check if ROS2 has a new command
            if self.data_store.get("new_cmd", False):
                angle = self.data_store.get("angle", 0.0)
                throttle = self.data_store.get("throttle", 0.0)
                # Reset the flag so this command is only used once
                self.data_store["new_cmd"] = False
                return angle, throttle
            else:
                # No new command; do not overwrite manual/joystick inputs
                return None, None

