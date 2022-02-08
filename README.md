# Project SPECTER

SPECTER is a Edge Detection and Image Measurement Software that is made purely with python.

## Dependencies

```python
import cv2
import tkinter
import PIL

from scipy.spatial import distance as dist
import matplotlib.pyplot as plt
from imutils import perspective
from imutils import contours
import numpy as np
```


## About/Preview
This is a software that allows the detection on infrared/hyperspectral images via contours and thresholding. The image processing sequence is quite straight forward. A simple and pure code only version is found in ```visualize/edgedetection.ipynb``` notebook file and it can easily be set up with the a few main dependent libraries ```matplotlib```, ```imutils```, ```numpy```, ```scipy```, ```OpenCV``` and ```Pillow```.

It is still work in progress and I plan on improving it. A newer and faster version of this software is currently being worked on with C# or Java.

![Slide1](https://user-images.githubusercontent.com/75195899/153037399-ab670a11-f209-43ad-a224-e802be0ed3b5.JPG)

## License
[MIT](https://choosealicense.com/licenses/mit/)
