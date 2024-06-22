# YOLOv8 Football Player & Ball Detection using fine-tuning

## Project Overview

This project demonstrates an attempt at fine-tuning the YOLOv8 object detection model for football using a custom dataset containing images of footballers on a football pitch. The primary objective is to evaluate the trained model's performance on detecting Football Players and Balls.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset Labeling](#dataset-labeling)
- [Dataset Preparation](#dataset-preparation)
- [Environment Setup](#environment-setup)
- [Running Streamlit](#running-streamlit)
- [Results](#results)

## Dataset Labeling

Creating an accurate dataset is very important for training and evaluating object detection models like YOLOv8. 
For this project, we wanted to try labeling ourselves for once : we used [Label Studio](https://labelstud.io/) to annotate our images by drawing boxes around football players and balls.

## Dataset Preparation

The dataset used in this project consists of 100 images of football players on a pitch with bounding box labels annotated with two classes: `Ball` and `Player`.
We split the dataset into 80 images for training and 20 images for validation.

## Environment Setup

To run FOOTBALL_NEW.ipynb, make sure all data is stored in the "/content/drive/MyDrive/ml_data/" path on google drive as we have run the model training on google colab. In case you wish to run the file locally, you may have to change the paths within FOOTBALL_NEW.ipynb to the cloned directory.

## Running Streamlit

You can try running the Streamlit interface and test our model using the following command, in the working directory :
```
streamlit run app.py
```

## Results

Let's try detection for this image of the France-Austria match (European Championship, 17th June 2024)
![autriche-france-voir-la-premiere-occasion-de-kylian-mbappe-971848-d8aae3-0@3x](https://github.com/BonelessCode/Football-Player-Detection/assets/59204911/93b62ef6-8710-4951-b65f-d33f3b17214d)
Here is detection using YoloV8 before fine-tuning : 
![yolov8](https://github.com/BonelessCode/Football-Player-Detection/assets/59204911/c4273136-c249-4388-94c0-3622cf03ea50)
Here is detection using our trained model :
![temp_image](https://github.com/BonelessCode/Football-Player-Detection/assets/59204911/17426583-9697-4e81-a619-c40f2a848fb8)
We can see that two players which were not picked up with a vanilla Yolov8 have been picked up by our trained model.

Now let's talk about the metrics : 
![è](https://github.com/BonelessCode/Football-Player-Detection/assets/59204911/2dd30c6b-0cf4-46b8-9e46-3a7c499eda75)
![Sans titre](https://github.com/BonelessCode/Football-Player-Detection/assets/59204911/106d0418-8d9f-4a77-8cf0-1ab5fbc1a0a2)
![Sans 2](https://github.com/BonelessCode/Football-Player-Detection/assets/59204911/a4d16cb8-cb7f-4d56-a801-8a5a369942f9)
![Sans 3](https://github.com/BonelessCode/Football-Player-Detection/assets/59204911/6ea32243-4f47-47e6-905a-d100f7665aab)
![Sans 4](https://github.com/BonelessCode/Football-Player-Detection/assets/59204911/17b1c666-8bf3-404e-8aca-9dfb50c88289)
![Sans 5](https://github.com/BonelessCode/Football-Player-Detection/assets/59204911/d062a82c-3c03-4a99-ac31-4f4909983cec)
We have achieved fair metrics, although Ball detection may have to be reviewed. 






## Screenshots
![Sans titre](https://github.com/BonelessCode/Football-Player-Detection/assets/59204911/097b26de-7964-48b5-912e-22ba40bd0398)
![Sans 3](https://github.com/BonelessCode/Football-Player-Detection/assets/59204911/c6c74cb6-8ea0-4dba-a6d1-b3dbe81e10ac)
![Sans 4](https://github.com/BonelessCode/Football-Player-Detection/assets/59204911/63d985ec-6282-44f5-83ff-aaf9771cfbf7)

