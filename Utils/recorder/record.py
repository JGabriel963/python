import pyaudio
import wave

audio = pyaudio.PyAudio()

stream = audio.open(
    input=True,
    format=pyaudio.paInt16,
    channels=1,
    rate=44000,
    frames_per_buffer=1024
)

frames = []

try:
    while True:
        block = stream.read(1024)
        frames.append(block)
except KeyboardInterrupt:
    pass

stream.start_stream()
stream.close()
audio.terminate()

with wave.open("recorder.wav", "wb") as file:
    file.setnchannels(1)
    file.setframerate(44000)
    file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    file.writeframes(b"".join(frames))