#Detecting Pikachu on Android using Tensorflow Object Detection
Overview
This repo contains the code used in my experiment titled "Detecting Pikachu on Android using Tensorflow Object Detection". In this experiment, which is available here, I explained the many steps needed to train a custom object detection model using TensorFlow Object Detection API and how to deploy it in an Android device.

The project was done on TensorFlow 1.4

This project has been updated with a video detection feature. For a detailed explanation of why it was updated, and how the video detection was done, check out my second article titled Detecting Pikachu in videos using Tensorflow Object Detection

The code
The content of this repo is mostly divided in 4 parts

The directory android contains the 'gradle.build' file used to build the example TensorFlow provides, and the file 'DetectorActivity.java' which is the responsible of performing the detection in the app
The directory training has the final models my training produced, as well as the pipeline configuration file required for the training.
The script detection_video.py which is used for performing the detections in videos
The rest of the files are those scripts needed to prepare the dataset.
Instructions
All this code by itself does not do anything. It must be used in combination with the Object Detection API. The report linked above has all the instructions on how to use the code alongside the API.
