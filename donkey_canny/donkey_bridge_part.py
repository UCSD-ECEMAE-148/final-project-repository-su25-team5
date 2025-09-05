import threading 
class ROS2BridgePart: 
    def __init__(self, data_store): 
        """ 
        data_store: a dict-like object shared between ROS2 node and DonkeyCar 
        Example: {"angle": 0.0, "throttle": 0.0} 
        """ 
        self.data_store = data_store 
        self.lock = threading.Lock() 

    def run(self): 
        # Safely grab the latest values written by the ROS2 node 
        with self.lock: 
            angle = self.data_store.get("angle", 0.0) 
            throttle = self.data_store.get("throttle", 0.0) 
            return angle, throttle