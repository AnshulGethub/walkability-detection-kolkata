# Train YOLOv5 on your dataset

import os

# Step 1: Change directory to YOLOv5
os.chdir(r"C:\Users\EURG-LAB\yolov5")  # <-- path where yolov5 folder is

# Step 2: Set parameters
data_yaml_path = 🔁 Replace this Annotation data path
weights_path = "yolov5s.pt"
img_size = 416
batch_size = 16
epochs = 150
project_name = "train"
experiment_name = "try3_model"

# Step 3: Create training command
command = f'python train.py --img {img_size} --batch {batch_size} --epochs {epochs} --data "{data_yaml_path}" --weights {weights_path} --project {project_name} --name {experiment_name} --cache'

# Step 4: Run the command
os.system(command)
