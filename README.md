# CT Scan-based Brain Hemorrhage Detection using Faster R-CNN

This repository contains the code and resources for a deep learning-based project aimed at detecting brain hemorrhages from CT scan images using the Faster R-CNN architecture. This project was developed as part of the Minor 1 curriculum for a B.Tech in Computer Science and Engineering.

## Overview
Brain hemorrhages are life-threatening conditions that require immediate attention. This project utilizes Faster R-CNN, a state-of-the-art object detection model, to identify hemorrhage regions in CT scan images. The goal is to assist medical professionals by providing an automated detection system.

## Features
- **Model Architecture**: Faster R-CNN for object detection.
- **Datasets Used**:
  - Roboflow's CT Brain Hemorrhage Dataset
- **Input Image Resolution**: 640x640 pixels.
- **Output**: Detected regions of hemorrhages in CT scan images with bounding boxes and probabilities.

## Dataset
The project uses:
1. **Roboflow CT Brain Hemorrhage Dataset**: Curated dataset available from Roboflow, formatted for object detection tasks.

### Preprocessing Steps
- Images resized to 640x640.
- Label annotations were formatted to be compatible with Faster R-CNN requirements.

## Model
The Faster R-CNN model was selected for its ability to provide high accuracy in object detection tasks. The architecture consists of:
- Region Proposal Network (RPN)
- Feature Pyramid Network (FPN)
- Fast RCNN classifier and regressor for object detection.

## Installation
Clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/yourusername/ct-scan-injury-detection.git
cd ct-scan-injury-detection
pip install -r requirements.txt
```

## Usage
1. **Prepare the dataset**:
   - Download the datasets and place them in the `data/` directory.
   - Ensure the annotations are in COCO or Pascal VOC format.

2. **Train the model**:
   ```bash
   python train.py --config configs/faster_rcnn_config.yaml
   ```

3. **Evaluate the model**:
   ```bash
   python evaluate.py --model checkpoints/best_model.pth
