# Python RPcamera
This is a simple and quick way to control a RP5 camera with a python terminal on a PC. The workflow has not been tested with MAC. The system uses [CamUI for picamera2](https://github.com/monkeymademe/CamUI) to generate a web feed and opencv to retrieve it.

You first have to configure the raspberry pi cameras. The rest of this mini protocol assumes that you are able to use the camera on the raspberry pi. You can test this with the command `libcamera-hello --camera 0` in the bash. You should see a live preview.

## Installing CamUI for picamera2
CamUI for picamera2 is a web interface for the picamera. It uses the python library Picamera2 to control the camera and Flask to display the image and the control GUI on a local server. To install it, you have to clone the repository to the Raspberry Pi with the command : `gitclone https://github.com/monkeymademe/picamera2-WebUI.git` Once this is installed you can enter the directory : `cd picamera2-WebUI`. To finally run the application which allows you to access the camera via your browser : python app.py. You should then be able to access the application on any device that is connected to the same via the following address : `http://IP OF THE RP:8080/`. Refer to the project's [GitHub repository](https://github.com/monkeymademe/CamUI) for more information.

### Common issue 
I have noticed that you cannot connect via EduRoam. The simplest way I have managed to fixed this is by connecting the raspberry pi to my pc via an Ethernet
to USB cable and sharing my network. To do so you have to access the "Network Connections" windowc. Right clic on the connection you want to share and select "Properties". Then access the "Sharing" tab and select "Allow user ####"

## Retrieve feed 
Open CV is a library for computer vision, specialized in real time analysis. The feed is retrieved with `cv2.VideoCapture(address)`, where address is the address of the video feed. To find the address of the video feed, connect via `http://IP OF THE RP:8080/`, access the camera you want to retrieve the feed from, right clic on the image and select "Inspect". You should easly find the link, it shoudl look something like `http://IP OF THE RP:8080/video_feed_0`. You can then access with a Python terminal using the script "RP5_camera.py" by changing the address where indicated. I have included in this reprository a simple example of how you could retrieve the feed.
