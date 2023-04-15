#Screen Recorder

import cv2 as c
import pyautogui as p
import numpy as np

#Create Resolution
resolution = p.size()
filename = input("Please enter the file name and path : (For example : C:/Users/surab/Downloads/LIVE_RECORDING.mp4) ")

#Fix frame rate
fps = 25.0

fourcc = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter(filename, fourcc, fps, resolution)

#Create recording module
c.namedWindow("Live_Recording", c.WINDOW_NORMAL)
c.resizeWindow("Live_Recording", (600, 400))

while True:
    img = p.screenshot()
    f = np.array(img)
    f = c.cvtColor(f, c.COLOR_BGR2RGB)
    output.write(f)
    c.imshow("Live_Recording", f)
    if c.waitKey(1) == ord("q"):
        break

output.release()
c.destroyAllWindows()
