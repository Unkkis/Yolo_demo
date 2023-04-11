# Yolo_demo

This is a project made to Haaga-Helia University of applied sciences (https://www.haaga-helia.fi/).
Goal was to make a application that could demo YOLO object detection. Application that could be installed to a computer and run to show how YOLO finds objects from a video.

## Application
Application is made to use object detection model YOLOv8 (https://docs.ultralytics.com/).
The app itself is made with Pyside6, the Qt for Python (https://doc.qt.io/qtforpython/quickstart.html).
OpenCV (https://opencv.org/) is also used to use and format webcam video.
For youtube videos, PaFy (https://pythonhosted.org/pafy/) is used.

## Prequisites
- Have to have Python (3.7 ->) installed (https://www.python.org/downloads/)


- Have to have YOLOv8 (and all requirements for ultralytics package etc. PyTorch and OpenCv) installed
```
pip install ultralytics
```

- PaFy is needed for youtube videos
```
pip install pafy
```

## Usage
If you want to use your other YOLO models or if you have video files that you want to use, copy them to the root of the project file. Program does a search for .pt files (yolo models) and video files on startup and presents them on the list.

Run main.py and enjoy.

## Packaging
If you want to package this app to executable I've also added  main.spec -file and YOLO default.yaml -file.
To package first install Pyinstaller (https://pyinstaller.org/en/stable/)

```
pip install pyinstaller
```

Then run
```
pyinstaller main.spec
```




