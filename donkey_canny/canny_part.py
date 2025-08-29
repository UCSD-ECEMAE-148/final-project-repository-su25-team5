import cv2
import numpy as np

class CannyPart:
    def __init__(self, low_threshold=100, high_threshold=200):
        self.low = low_threshold
        self.high = high_threshold

    def run(self, img_arr):
        gray = cv2.cvtColor(img_arr, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, self.low, self.high)
        edges_rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

        return edges_rgb
    
# the code below is for testing
# if __name__ == "__main__":
#     # Load an image
#     img = cv2.imread("test1.jpg")  # replace with your filename
#     canny = CannyPart(low_threshold=100, high_threshold=200)

#     edges = canny.run(img)

#     # Show both original and edges
#     cv2.imshow("Original", img)
#     cv2.imshow("Edges", edges)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()