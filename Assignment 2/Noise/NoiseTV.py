import cv2
import numpy as np


fps = 24

original_image = cv2.imread('Noise\TV.jpg')
original_image = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)

output_filename = 'noisy_video_with_overlay.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_filename, fourcc, fps, (original_image.shape[1], original_image.shape[0]))


while True:

    noisy_image = np.random.random((175, 242)) *255
    noisy_image = np.array(noisy_image, dtype=np.uint8)

    original_image[160:335,114:356] = noisy_image
    
    colored_image = cv2.cvtColor(original_image, cv2.COLOR_GRAY2BGR)


    cv2.imshow('Noisy Image', colored_image)
    out.write(colored_image)




    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    
out.release()
cv2.destroyAllWindows()
