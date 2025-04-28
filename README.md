# 🏙️ Walkability Feature Detection from Street View Images in Kolkata

This project uses computer vision techniques 🖥️ to detect walkability-related features from Google Street View (GSV) images 📷 in Kolkata, India.  
A YOLOv5-based deep learning model 🤖 is trained and deployed to automatically identify four important pedestrian environment elements:
- 🌳 Trees
- 💡 Streetlights
- 🚶‍♂️ Footpaths
- 🚧 Encroachments

---

## 📍 Study Area and Sampling

- 📍 **City:** Kolkata, India 🇮🇳
- 📈 **Sampling Points:** 53,343 points generated at 500-meter intervals on pedestrian-accessible road segments.
- 🗺️ **Data Sources:** OpenStreetMap (OSM) + Google Street View Static API.
- 📸 **Final Cleaned Images:** 21,942 high-quality GSV images used for detection after quality control.

---

## 🛠️ Feature Detection Pipeline

1. **GSV Image Downloading** 🔻  
   - Automated image collection using Google Street View API.
   - Metadata API used for pre-checking image availability.

2. **Dataset Annotation** 🏷️  
   - 1,000 GSV images annotated manually on Roboflow.
   - Object classes: Trees, Streetlights, Footpaths, Encroachments.

3. **Model Training** 📚  
   - YOLOv5s model fine-tuned with data augmentation techniques.
   - Training for 150 epochs with a 70/30 train-validation split.

4. **Inference Across City** 🏙️  
   - Detecting walkability features across the entire cleaned GSV dataset.
   - Saving detection results with bounding boxes and confidence scores.

5. **Feature Scoring** 🧮  
   - Tree coverage calculated as a normalized area fraction.
   - Binary scoring for Streetlights, Footpaths, and Encroachments.
---
## 📂 Project Structure
walkability-detection-kolkata/ ├── code/ │ ├── GSV_Image_extraction.py │ ├── Train_YOLOv5.py │ ├── extracet_infromation.py │ └── final Feature Scoring.py ├── README.md ├── requirements.txt ├── .gitignore


## ⚙️ Requirements

Install the required Python libraries:

```bash
pip install -r requirements.txt
Main libraries used:

🐍 Python 3.8+

🔥 PyTorch

📷 OpenCV

🌐 Requests

📈 tqdm

📦 roboflow

🤖 YOLOv5
```

## 🚀 How to Run the Project

(1)Download GSV Images
```bash
python code/GSV_Image_extraction.py
```

(2)Train YOLOv5 Model
```bash
python code/Train_YOLOv5.py
```
(3)Run Inference on Images
```bash
python code/extracet_infromation.py
```

(4)Score the Features
```bash
python code/final\ Feature\ Scoring.py
```

## 🙌 Acknowledgments
🗺️ OpenStreetMap contributors for pedestrian network data.

🏢 Google Inc. for Google Street View API.

🛠️ YOLOv5 by Ultralytics for object detection models.

🧠 Roboflow for annotation platform support.

✨ Project Highlights

🌏 City-scale streetscape feature mapping.

🚶‍♂️ Focus on pedestrian infrastructure analysis.

🤖 Application of deep learning to urban planning.

