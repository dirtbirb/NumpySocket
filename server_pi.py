from numpysocket import NumpyServer
from picamera import PiCamera
from picamera.array import PiBayerArray

npSocket = NumpyServer()
npSocket.start(9999)

# Read until video is completed
camera_port = 0
with PiCamera(camera_port, sensor_mode=2) as camera:
    with PiBayerArray(camera, output_dims=2) as stream:
        camera.capture(
            stream,
            format='jpeg',  # Necessary for bayer=True
            bayer=True,     # Include Bayer data in metadata
            thumbnail=None)
        while True:
            npSocket.send_array(stream.array)

# When everything done, release the video capture object
npSocket.end()
print("Closed successfully")
