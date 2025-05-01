import os
import cv2
import numpy as np

folder_dir = ""

for images in os.listdir(folder_dir):
    if images.endswith(".jpg"):
        img_path = os.path.join(folder_dir, images)
        print(f"Processing image: {img_path}")
        
        # Load the image to get dimensions
        img = cv2.imread(img_path)
        height, width, _ = img.shape  # Get image dimensions
        
        # Find the corresponding YOLO .txt file
        txt_file = images.replace('.jpg', '.txt')
        txt_path = os.path.join(folder_dir, txt_file)
        
        if os.path.exists(txt_path):
            print(f"Found YOLO annotation file: {txt_path}")
            
            # Create a black image (mask) of the same dimensions as the original image
            mask = np.zeros_like(img)
            
            # Load YOLO annotations
            with open(txt_path, 'r') as f:
                yolo_data = f.readlines()
            
            # Iterate through each bounding box in the YOLO annotation
            for line in yolo_data:
                elements = line.strip().split()
                class_id = int(elements[0])  # The class (object) ID
                x_center, y_center, bbox_width, bbox_height = map(float, elements[1:])
                
                # Convert normalized coordinates back to pixel values
                x_center = int(x_center * width)
                y_center = int(y_center * height)
                bbox_width = int(bbox_width * width)
                bbox_height = int(bbox_height * height)
                
                # Calculate the top-left and bottom-right corners of the bounding box
                x_min = int(x_center - (bbox_width / 2))
                y_min = int(y_center - (bbox_height / 2))
                x_max = int(x_center + (bbox_width / 2))
                y_max = int(y_center + (bbox_height / 2))
                
                # Draw a filled rectangle (mask) for the bounding box on the mask
                cv2.rectangle(mask, (x_min, y_min), (x_max, y_max), (255, 255, 255), thickness=-1)
            
            # Save the masked image to a new file
            masked_img_path = os.path.join(folder_dir, f"masked_{images}")
            cv2.imwrite(masked_img_path, mask)
            print(f"Masked image saved: {masked_img_path}")
