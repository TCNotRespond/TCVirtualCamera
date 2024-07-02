# TCVirtualCamera
A GUI Client for pyvirtualcam

![123.png](https://krseoul.imgtbl.com/i/2024/07/02/668394280a429.png)

## What's the usage?

Transfer the image to the virtual camera. Aim at solve the problem that some software banned OBS Virtual Camera, like WeChat Desktop.



## How to RUN

1. Download driver from

 [schellingb/UnityCapture: Streams Unity rendered output to other Windows applications as virtual capture device (github.com)](https://github.com/schellingb/UnityCapture)

2. Install `UnityCaptureFilter32.dll` and `UnityCaptureFilter64.dll` with command

```
regsvr32 "UnityCaptureFilter32.dll" "/i:UnityCaptureName=Virtual Camera"
regsvr32 "UnityCaptureFilter64.dll" "/i:UnityCaptureName=Virtual Camera"
```

3. Install requirements with command

```
pip install pyside6 pycameralist soundplay
```

4. Run `gui.py`



## Attention

1. Don't choose Virtual Camera in camera mode, or it will crash.

2. Custom data is not available.
3. Sound out is in experiment now. Using OBS Virtual Camera + Virtual Cable instead is recommended.
