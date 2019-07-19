import time
from subprocess import call

call('fswebcam --no-banner/home/pi/Desktop/Picktures/%Y-%m-%d_%H%M.jpg',shell=true)

sudo apt-get install motion

sudo nano /etc/motion/motion.conf


ctrl + w : find
framerate 24
event_gap 0
target_dir /home/pi/Desktop/Pictures
outpost_pictures best
ffmeg_outpost_movies off
on_event_START python3 /home/pi/Desktop/motionDetection.py %f


























     
