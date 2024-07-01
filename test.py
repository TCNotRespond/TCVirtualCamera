import sounddevice as sd
from pydub import AudioSegment
from tqdm import tqdm
import numpy as np

# 指定设备 ID
print(sd.query_devices())
device_id = 1  # 需要替换为你的设备 ID

# 读取音频文件
audio = AudioSegment.from_file("example.mp3")

frames = np.array(audio.get_array_of_samples()).reshape(-1, audio.channels)
sample_rate = audio.frame_rate

# 计算进度条的总长度
duration = len(audio) / 1000  # 毫秒转换为秒
total_frames = len(frames)

# 播放音频并显示进度条
stream = sd.OutputStream(samplerate=sample_rate, channels=audio.channels, dtype='int16')

with stream:
    # 初始化进度条
    with tqdm(total=total_frames, unit='frame') as pbar:
        for i in range(0, total_frames, sample_rate):
            chunk = frames[i:i+sample_rate]
            stream.write(chunk)
            pbar.update(len(chunk))

print("播放完成")
