import os.path

import sounddevice as sd
from pydub import AudioSegment
import numpy as np

class Soundplay:
    def play_sound(self,device_id,file):
        if os.path.exists("stop.play"):
            os.remove("stop.play")
        audio = AudioSegment.from_file(file)
        frames = np.array(audio.get_array_of_samples()).reshape(-1, audio.channels)
        sample_rate = audio.frame_rate
        total_frames = len(frames)
        stream = sd.OutputStream(samplerate=sample_rate,
                                 device=device_id,
                                 channels=audio.channels,
                                 dtype='int16')

        with stream:
            for i in range(0, total_frames, sample_rate):
                if os.path.exists("stop.play"):
                    break
                chunk = frames[i:i+sample_rate]
                stream.write(chunk)
        print("Finished playing")