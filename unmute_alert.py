import pyaudio
import wave
import threading
from pydub import AudioSegment
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")


def check_noise(name):
    RECORD_SECONDS_INIT = 5
    RECORD_SECONDS = 1
    while True:
        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS_INIT)):
            data = stream.read(CHUNK)
            frames.append(data)

        RECORD_SECONDS_INIT = RECORD_SECONDS
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    
    stream.stop_stream()
    stream.close()
    p.terminate()



x = threading.Thread(target=check_noise, args=(1,))
x.start()

print("* done recording")
time.sleep(5)

temp =35
while True:
    song = AudioSegment.from_wav(WAVE_OUTPUT_FILENAME)
    song_10_db_quieter = abs(song.dBFS - 5)
    if song_10_db_quieter < temp -2:
        print("talk")
    temp=song_10_db_quieter
    time.sleep(1)
