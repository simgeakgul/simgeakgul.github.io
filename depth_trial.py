import cv2, numpy as np
d = cv2.imread('depth_vis.jpg', cv2.IMREAD_UNCHANGED) 
d = d / d.max()                                           
cv2.imwrite('depth.jpg', (d*255).astype(np.uint8))
