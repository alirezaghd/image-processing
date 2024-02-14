import cv2
import numpy as np
import imageio

background_image = cv2.imread('Snow\Snow.jpg')

num_snowflakes = 100

snowflake_size = 2

height, width, _ = background_image.shape

frames = []
while True:
    snow_image = np.zeros_like(background_image)

    for _ in range(num_snowflakes):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        cv2.circle(snow_image, (x, y), snowflake_size, (255, 255, 255, 255), -1)

    snowy_background = cv2.add(background_image, snow_image)

    frames.append(cv2.cvtColor(snowy_background, cv2.COLOR_BGR2RGB))

    cv2.imshow('Snowy Scene', snowy_background)

    if cv2.waitKey(250) & 0xFF == ord('q'):
        break

output_gif = 'snowy_scene.gif'
imageio.mimsave(output_gif, frames, 'GIF', duration=0.25)

cv2.destroyAllWindows()
