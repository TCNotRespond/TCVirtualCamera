import os

import pyvirtualcam
import cv2

class Camera:
    def setSendContent(self,type,content):
        if type=="video":
            self.video_path = content
            self.cap = cv2.VideoCapture(self.video_path)
            self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        if type=="stream":
            self.cap = cv2.VideoCapture(content)
            self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        if type=="capture":
            self.cap = cv2.VideoCapture(content)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
            self.cap.set(cv2.CAP_PROP_FPS, 60)
            self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.fps = self.cap.get(cv2.CAP_PROP_FPS)

    def Send(self,type,content):
        if os.path.exists("stop.lock"):
            os.remove("stop.lock")
        self.setSendContent(type,content)

        if not self.cap.isOpened():
            print("Error: Cannot open video file.")
            exit()

        with pyvirtualcam.Camera(width=self.frame_width,
                                 height=self.frame_height,
                                 fps=self.fps,
                                 device="Virtual Camera",
                                 backend="unitycapture",
                                 fmt=pyvirtualcam.PixelFormat.RGB,
                                 print_fps=True
                                 ) as cam:
            print(f'Using virtual camera: {cam.device}')
            while True:
                if os.path.exists('stop.lock'):
                    break

                ret, frame = self.cap.read()

                if not ret:
                    print("End of video stream or error.")
                    break

                # 将BGR颜色转换为RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # 发送帧到虚拟摄像头
                cam.send(frame)
                cam.sleep_until_next_frame()
if __name__ == '__main__':
    Camera()
