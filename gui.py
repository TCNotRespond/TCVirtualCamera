from design import Ui_TCVirtualCamera
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QObject, QThread, Signal
from PyCameraList.camera_device import *
import sounddevice as sd
from camera import Camera
from soundplay import Soundplay


class Worker2(QObject, Soundplay):
    finished = Signal()  # Signal to indicate the operation has finished

    def __init__(self, file_path, device_id):
        super().__init__()
        self.file_path = file_path
        self.device_id = device_id

    def run(self):
        self.play_sound(file=self.file_path,device_id=self.device_id)
        self.finished.emit()


class Worker(QObject, Camera, Soundplay):
    finished = Signal()  # Signal to indicate the operation has finished

    def __init__(self, type, content):
        super().__init__()
        self.type = type
        self.content = content

    def run(self):
        # Perform the time-consuming operation here
        self.Send(type=self.type, content=self.content)
        self.finished.emit()


class MyMainWindow(QMainWindow, Ui_TCVirtualCamera, Camera):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_data()
        self.init_connection()

    def init_data(self):
        self.setFixedSize(480, 270)
        self.camera = list_video_devices()  # 把数据添加到comboBox中
        for index, (id, name) in enumerate(self.camera):
            self.comboBox.addItem(name, userData=id)

        self.device = sd.query_devices()
        for index in range(len(self.device)):
            name = self.device[index]["name"]
            id = self.device[index]["index"]
            self.comboBox_2.addItem(name, userData=id)

    def init_connection(self):
        self.comboBox.currentIndexChanged.connect(self.handle_combobox_change)
        self.pushButton.clicked.connect(self.refresh_camera_list)
        self.pushButton_4.clicked.connect(self.start_send)
        self.pushButton_5.clicked.connect(self.stop)
        self.pushButton_2.clicked.connect(self.select_file)

    def handle_combobox_change(self, index):
        self.selected_data = self.comboBox.currentData()
        print(f"Selected data: {self.selected_data}")

    def refresh_camera_list(self):
        self.comboBox.clear()
        for index, (id, name) in enumerate(self.camera):
            self.comboBox.addItem(name, userData=id)
        self.camera = list_video_devices()
        self.comboBox.update()

    def start_send(self):
        if self.tabWidget.currentIndex() == 0:
            type = "capture"
            content = self.comboBox.currentData()

            print(f"Source from: {self.camera[self.comboBox.currentData()][1]}")
            print([{"type": type}, {"content": content}])
            print("")

        if self.tabWidget.currentIndex() == 1:
            type = "video"
            content = self.file_path

            print(f"Source from: {self.file_path}")
            print([{"type": type}, {"content": content}])
            print("")

            self.start_play()

        if self.tabWidget.currentIndex() == 2:
            type = "stream"
            content = self.plainTextEdit_4.toPlainText()

            print(f"Source from: {self.plainTextEdit_4.toPlainText()}")
            print([{"type": type}, {"content": content}])
            print("")

        self.pushButton_4.setEnabled(False)
        # Create a worker and move it to a new thread

        self.worker = Worker(type=type, content=content)
        self.thread = QThread()

        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.on_worker_finished)

        # Start the thread
        self.thread.start()

    def stop(self):
        with open('stop.lock', 'w') as f:
            f.write('This file is used to signal stop operation.')
        self.pushButton_4.setEnabled(True)

        with open('stop.play', 'w') as f:
            f.write('This file is used to signal stop playing.')

    def on_worker_finished(self):
        print("Operation completed.")
        # Clean up thread and worker
        self.thread.quit()
        self.thread.wait()
        self.worker.deleteLater()
        self.thread.deleteLater()

    def start_play(self):
        self.worker2 = Worker2(file_path=self.file_path,device_id=self.comboBox_2.currentData())
        self.thread2 = QThread()

        self.worker2.moveToThread(self.thread2)
        self.thread2.started.connect(self.worker2.run)
        self.worker2.finished.connect(self.on_worker2_finished)

        # Start the thread
        self.thread2.start()

    def on_worker2_finished(self):
        print("Operation2 completed.")
        # Clean up thread and worker
        self.thread2.quit()
        self.thread2.wait()
        self.worker2.deleteLater()
        self.thread2.deleteLater()

    def select_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle('选择文件')
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)

        if file_dialog.exec():
            self.file_path = file_dialog.selectedFiles()[0]
            self.plainTextEdit_5.setPlainText(self.file_path)
            print(f"{self.file_path}")
        else:
            print("None File")


if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec()
