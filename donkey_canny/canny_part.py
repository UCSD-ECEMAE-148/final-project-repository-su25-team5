import cv2
import numpy as np

class CannyPart:
    def __init__(self, low_threshold=800, high_threshold=1400):
        self.low = low_threshold
        self.high = high_threshold

    def run(self, img_arr):
        

        ## Day/Night Changes -----------------------------------------

        lab = cv2.cvtColor(img_arr, cv2.COLOR_BGR2LAB)
        L, A, B = cv2.split(lab)

        mean_L = np.mean(L)
        dark_ratio = np.sum(L < 60) / L.size


        if (mean_L < 120):
            lower_y = 0
        else:
            lower_y = 33

        ## -----------------------------------------


        ## Enhance Yellow and White Lines ----------------------------------------------------

        hsv = cv2.cvtColor(img_arr, cv2.COLOR_BGR2HSV)

        # yellow mask
        lower_yellow = np.array([0, lower_y, 60])
        upper_yellow = np.array([50, 255, 255])
        mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

        # white mask
        lower_white = np.array([91, 0, 190])
        upper_white = np.array([152, 255, 255])
        mask_white = cv2.inRange(hsv, lower_white, upper_white)

        # combine masks
        mask_colors = cv2.bitwise_or(mask_yellow, mask_white)

        # enhance brightness in those areas
        h, s, v = cv2.split(hsv)
        v_boost = v.copy()
        v_boost[mask_colors > 0] = np.clip(v_boost[mask_colors > 0] * 1.9, 0, 255).astype(np.uint8)

        hsv_boost = cv2.merge([h, s, v_boost])
        img_boost = cv2.cvtColor(hsv_boost, cv2.COLOR_HSV2BGR)


        ##  ----------------------------------------------------------------

        ## Brightening the Shadows ----------------------------------------------------

        shadow_percentile=52
        mask_smooth=1
        gamma=0.16
        alphaMul = .9

        # find dark regions via luminance 
        lab = cv2.cvtColor(img_boost, cv2.COLOR_BGR2LAB)
        L, A, B = cv2.split(lab)

        mean_L = np.mean(L)

        if mean_L < 150:       # image very dark
            shadow_percentile = 52
        elif mean_L > 170:    # image very bright
            shadow_percentile = 30

        thr = np.percentile(L, shadow_percentile)
        mask = (L < thr).astype(np.uint8) * 255  # 0/255 mask

        if mask_smooth > 0:
            k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (mask_smooth, mask_smooth)) # use ellipse
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, k)
            mask = cv2.GaussianBlur(mask, (0, 0), 3)

        dark_ratio = np.sum(L < 60) / L.size

        if dark_ratio*10 > 0.55:       # lots of dark pixels
            gamma = 0.09
        elif dark_ratio*10 > 0.3:     
            gamma = 0.55
        else:                       # image is bright
            gamma = 0.85

        # brighten only dark pixels 
        Lf = L.astype(np.float32) / 255.0
        L_gamma = np.power(Lf, gamma) * 255.0      # gamma<1 = lift shadows
        L_gamma = np.clip(L_gamma, 0, 255).astype(np.uint8)

        alpha = (mask.astype(np.float32) / 255.0) * alphaMul 
        L_lift = ((1 - alpha) * L.astype(np.float32) + alpha * L_gamma.astype(np.float32)).astype(np.uint8)

        lab_lift = cv2.merge([L_lift, A, B])
        img_lift = cv2.cvtColor(lab_lift, cv2.COLOR_LAB2BGR)

        ##  ----------------------------------------------------------------


        ## Bluring Image ----------------------------------------------------

        avg = cv2.blur(img_lift, (2, 2))   # k x k kernel

        ##  ----------------------------------------------------------------


        ## Canny Edge ----------------------------------------------------

        gray = cv2.cvtColor(avg, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 800, 1400, apertureSize=5, L2gradient=True)


        ##  ----------------------------------------------------------------


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
