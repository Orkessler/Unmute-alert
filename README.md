# mouth-open
Identifies when you're talking on a "mute" mode during an online meeting.

We detect a situation of opening the mouth and playing sound and only then send an alert to the user who is on mute.
This way the user does not get an alert when he just opens his mouth.
And also there is no alert in case of external sound that does not come from the user's speech.


## Referenced Code

[mauckc - mouth-open](https://github.com/mauckc/mouth-open)

I was interested in recognizing the open mouth, and in absorbing a change in sound to recognize the person's speech in front of the camera

## Dependencies
Python modules for:
* scipy
* imutils
* numpy
* dlib
* cv2
* pyaudio
* wave
* threading

## Usage
This sample version uses your webcam, so make sure that the device you are using has one. Also make sure that the sound input on the device is working properly
#### To run the code
```bash
python temp.py
```


![sample gif](./video/mouth_open.gif)

