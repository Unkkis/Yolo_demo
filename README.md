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

Program uses QT for graphical interface and using Pyside6 as binding, so Pyside6 is needed
```
pip install pyside6
```

- Have to have YOLOv8 (https://docs.ultralytics.com/) (and all requirements for ultralytics package etc. PyTorch and OpenCv) installed
```
pip install ultralytics
```

- PaFy (https://pypi.org/project/pafy/) is needed for youtube videos
```
pip install pafy
```

- Youtube-DL (https://youtube-dl.org/) is needed for Youtube content. As ow writing, only version 2020.12.2 seems to work
```
pip install youtube_dl==2020.12.2
```

## Usage
Clone/unzip this repository to your computer and install things above.
Run main.py and enjoy.

If you want to use your other YOLO models or if you have video files that you want to use, copy them to the root folder of the project. Program does a search for .pt files (yolo models) and video files on startup and presents them on the list.

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




