
import cv2
import numpy as np


class RPCamera :
    def __init__(self, address, name):
        self.address = address
        self.name = name

        self.cam = cv2.VideoCapture(address)
        if self.cam.read()[1] is not None:
            print(f"Connection made with {name}")
        else :
            print("Connection didn't work")
        pass

    def live(self):
        while True:
            ret, frame = self.cam.read()
            # Display the captured frame
            cv2.imshow('Camera', frame)

            # Press 'q' to exit the loop
            if cv2.waitKey(1) == ord('q'):
                break

        # Release the capture and writer objects
        self.cam.release()
        cv2.destroyAllWindows()
    
    def capture(self):
        _, frame = self.cam.read()
        return frame


    def getAverageBW(self):
        """
        Captures a photo and calculate the average black and white value.
        """
        ret, frame = self.cam.read()

        average_value = np.mean(frame)
        
        return average_value
    
    def getAverageColor(self, color_channel):
        """
        Captures a photo and calculate the average value of one of the RGB color.
        """
        ret, frame = self.cam.read()
        
        blue, green, red = cv2.split(frame)
        # Split the image into its Blue, Green, and Red channels
        if color_channel == 'red':
            return np.mean(red)
        elif color_channel == 'green':
            return np.mean(green)
        elif color_channel == 'blue':
            return np.mean(blue)
        else:
            raise ValueError("Invalid color channel. Choose 'red', 'green', or 'blue'.")
    
address_1 = "http://IP OF THE RP:8080/video_feed_0" # Change this for the address of the feed
camera1 = RPCamera(address_1, "camera 1")
camera1.live()
