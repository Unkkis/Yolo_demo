from glob import glob
import cv2

#https://docs.python.org/3/library/glob.html
def find_files(type):
    results = glob(f"./*.{type}")

    models = [ x.replace(".\\", "") for x in results]
    return models

#This script for drawing the boxes to frames
def draw_boxes(frame, results):
    # https://docs.ultralytics.com/usage/python/
    # https://docs.opencv.org/4.x/dc/da5/tutorial_py_drawing_functions.html
    # https://medium.com/@chanon.krittapholchai/build-object-detection-gui-with-yolov8-and-pysimplegui-76d5f5464d6c

    #Get box measures from results
    xyxy = results.boxes.xyxy.numpy()
    #Get confidence score
    confidence = results.boxes.conf.numpy()
    #Get class ID
    class_id = results.boxes.cls.numpy().astype(int)
    #Get class name
    class_name = [results.names[x] for x in class_id]
    # Pack together for easy use
    sum_output = list(zip(class_name, confidence,xyxy))

    for run_output in sum_output :
        #Unpack
        class_name, confidence, xyxy = run_output
        
        #Color for the box, depending on the confidence score
        if confidence > 0.8:
            box_color = (0, 100, 0)
            text_color = (0,100,0)
        else:
            box_color = (0, 0, 255)
            text_color = (0,0,255)
        #Draw box around the object
        first_half_box = (int(xyxy[0]),int(xyxy[1]))
        second_half_box = (int(xyxy[2]),int(xyxy[3]))
        cv2.rectangle(frame, first_half_box, second_half_box, box_color, 2)
    
        #Create text
        text_print = '{label} {con:.2f}'.format(label = class_name, con = confidence)
        # Specify where the box is drawn
        text_location = (int(xyxy[0]), int(xyxy[1] - 10 ))
   
        #Write text to image
        cv2.putText(frame, text_print ,text_location
                    , cv2.FONT_HERSHEY_SIMPLEX , 1
                    , text_color, 2 ,cv2.LINE_AA)
    return frame