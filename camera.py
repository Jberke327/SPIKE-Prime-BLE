import cv2
import numpy as np
import serial

from time import sleep


# define a video capture object
vid = cv2.VideoCapture(0)

def find_largest_color_contour(original_image, image_to_analyze, lower, upper, color, ready):
    x, y, w, h = [0, 0, 0, 0] # for initialization

    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    # find the colors within the specified boundaries and apply the mask
    mask = cv2.inRange(image_to_analyze, lower, upper)
    output = cv2.bitwise_and(image_to_analyze, image_to_analyze, mask=mask)

    ret, thresh = cv2.threshold(mask, 40, 255, 0)
    if (int(cv2.__version__[0]) > 3):
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    else:
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) != 0:
        # draw in blue the contours that were founded
        cv2.drawContours(output, contours, -1, (0, 0, 255), 3)

        # find the biggest countour (c) by the area
        c = max(contours, key=cv2.contourArea)
        # x, y, w, h = [0, 0, 0, 0]
        boundingRect = cv2.boundingRect(c)
        x, y, w, h = boundingRect
        # print(f"x,y,w,h: {boundingRect}")

        # show the images
        if color == "red":
            # draw the biggest contour (c) in Red
            cv2.rectangle(output, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.imshow('dummy', (np.hstack([output, image_to_analyze])))

        else:
            # draw the biggest contour (c) in Green
            cv2.drawContours(original_image, [c], -1, (0, 255, 0), 2)
            # draw it as a box
            cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # find center of largest contour, c.
            M = cv2.moments(c)
            if M["m00"] != 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                # return cx, cy
                # draw itq as a point/circle
                cv2.circle(frame, (cx, cy), 7, (255, 0, 0), -1)
                cv2.putText(frame, "center", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                # Tell Pico which movement to do
                if cx < 320 and cy < 240 and ready:
                    # pico.write(b"l\n")
                    print("LEFT!")
                    pico.write(b"l\n")
                elif cx > 320 and cy < 240 and ready:
                    print("RIGHT!")
                    pico.write(b"r\n")
                elif cx < 320 and cy > 240 and ready:
                    print("FORWARDS!")
                    pico.write(b"f\n")
                elif cx > 320 and cy > 240 and ready:
                    print("BACKWARDS!")
                    pico.write(b"b\n")
                print(f"cx, cy: {[cx, cy]}")
            # Left Box
            cv2.rectangle(original_image, (0, 0), (320, 240), (255, 0, 255), 1)
            cv2.putText(frame, "Go Left", (160 - 30, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
            # Right Box
            cv2.rectangle(original_image, (320, 0), (320 + 320, 240), (255, 0, 255), 1)
            cv2.putText(frame, "Go Right", (320 + 160 - 30, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
            # Forwards Box
            cv2.rectangle(original_image, (0, 240), (320, 240+240), (255, 0, 255), 1)
            cv2.putText(frame, "Go Forwards", (160 - 50, 240+120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
            # Backwards Box
            cv2.rectangle(original_image, (320, 240), (320+320, 240 + 240), (255, 0, 255), 1)
            cv2.putText(frame, "Go Backwards", (320 + 160 - 55, 240 + 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)

            # Display Everything as a Window
            cv2.imshow('greentrack', (np.hstack([output, original_image])))


    # Return area of the biggest contour
    # return w * h
    # if cx is not None or cy is not None:
    #     return [cx, cy]

pico = serial.Serial("COM6", 115200) # connect to pico
sleep(0.1)
ready = False  # allows for prints/writes to Pico if True
# pico.write(b"join\n")
# ready = True
# sleep(0.1)

while(True):
    ret, frame = vid.read()
    cv2_image = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
    # cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('j'):
        # sleep(1)
        print("writing")
        # pico.write(b"join\n")
        ready = True
        # sleep(15)

    if cv2.waitKey(1) & 0xFF == ord('l'):
        # pico.write(b"quit\n")
        # sleep(8)
        print("stop writing")
        # pico.write(b"quit\n")
        ready = False
        # sleep(1)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        print("STOP!")
        pico.write(b"s\n")
        # pico.write(b"stop\n")

    # Find Largest Green
    # lower_g = [20, 80, 20]
    # upper_g = [140, 255, 90]
    # lower_g = [80, 95, 80] # NOLOP 1
    # upper_g = [110, 255, 130]
    lower_g = [95, 130, 80] # NOLOP 2
    upper_g = [120, 255, 130]
    # Find Largest Red
    # lower_r = [20, 20, 120]
    # upper_r = [110, 100, 255]
    direction = find_largest_color_contour(frame, cv2_image, lower_g, upper_g, "green", ready)
    # sleep(1)
    # incoming_data = pico.readline()
    # print(f"from pico:{incoming_data}")

vid.release()
cv2.destroyAllWindows()
pico.write(b"quit\n")
