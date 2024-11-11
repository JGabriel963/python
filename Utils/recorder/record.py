import pyaudio
import wave
import customtkinter

window = customtkinter.CTk()
window.geometry('800x300')
window.title("Recorder")

# audio = pyaudio.PyAudio()
# stream = audio.open(
#     input=True,
#     format=pyaudio.paInt16,
#     channels=1,
#     rate=44000,
#     frames_per_buffer=1024
# )

def stop():
    print("Stop")
    button.configure(text="Gravar", command=start)

def start():
    button.configure(text="Gravando", command=stop)
    # frames = []

    # try:
    #     while True:
    #         block = stream.read(1024)
    #         frames.append(block)
    # except KeyboardInterrupt:
    #     pass

    # stream.start_stream()
    # stream.close()
    # audio.terminate()

    # with wave.open("recorder.wav", "wb") as file:
    #     file.setnchannels(1)
    #     file.setframerate(44000)
    #     file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    #     file.writeframes(b"".join(frames))


text = customtkinter.CTkLabel(window, text="Gravador de áudio")
text.pack(padx=10, pady=10)

button = customtkinter.CTkButton(window, text="Gravar", command=start)
button.pack(padx=10, pady=20)

window.mainloop()