# the code below is for testing
import cv2
import numpy as np
class CannyPart:
    def __init__(self, low_threshold=100, high_threshold=200):
        self.low = low_threshold
        self.high = high_threshold

    def run(self, img_arr):

        hsv = cv2.cvtColor(img_arr, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)

        s = cv2.multiply(s, 1.75)   # increase by 50%
        h = cv2.multiply(h, .5)
        v = cv2.multiply(v, 1.75)

        s = np.clip(s, 0, 255).astype(np.uint8)
        h = np.clip(h, 0, 255).astype(np.uint8)
        v = np.clip(v, 0, 255).astype(np.uint8)

        hsv_enhanced = cv2.merge([h, s, v])
        img_colorful = cv2.cvtColor(hsv_enhanced, cv2.COLOR_HSV2BGR)

        gray = cv2.cvtColor(img_arr, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(img_colorful, cv2.COLOR_BGR2GRAY)
        #edges = cv2.Canny(gray, self.low, self.high, apertureSize=5, L2gradient=True)
        #edges_rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

        return gray, gray2, img_colorful

if __name__ == "__main__":
     # Load an image
     img = cv2.imread("586_cam_image_array_.jpg")  # replace with your filename
     canny = CannyPart(low_threshold=1100, high_threshold=1200)

     edges, edges2, color = canny.run(img)

     scale = 4.0 
     resized_img = cv2.resize(img, None, fx=scale, fy=scale)
     resized_edges = cv2.resize(edges, None, fx=scale, fy=scale)
     resized_edges2 = cv2.resize(edges2, None, fx=scale, fy=scale)
     resized_color = cv2.resize(color, None, fx=scale, fy=scale)
     cv2.imshow("Original", resized_img)
     #cv2.imshow("Gray", resized_edges)
     #cv2.imshow("Gray Color", resized_edges2)
     cv2.imshow("Colorful", resized_color)

     cv2.waitKey(0)
     cv2.destroyAllWindows()
