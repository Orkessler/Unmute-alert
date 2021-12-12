# mouth-open
Identifies when you're talking on a "mute" mode during an online meeting

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

[dlib shape predictor](https://github.com/AKSHAYUBHAT/TensorFace/blob/master/openface/models/dlib/shape_predictor_68_face_landmarks.dat)

![sample gif](./video/mouth_open.gif)

