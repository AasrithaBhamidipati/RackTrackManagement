import os
import json
import logging
from PIL import Image
import shutil

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_image(image_path):
    """
    Mock segmentation function that creates a working demo
    while we resolve the YOLO model dependencies
    """
    try:
        # Check if image exists and is valid
        if not os.path.exists(image_path):
            return {'success': False, 'error': f'Image not found: {image_path}'}
        
        # Try to open the image to validate it
        try:
            with Image.open(image_path) as img:
                width, height = img.size
        except Exception as e:
            return {'success': False, 'error': f'Invalid image file: {str(e)}'}
        
        OUTPUT_DIR = "static/segmented_outputs"
        COORDINATES_FILE = "static/segmented_outputs/coordinates.json"
        
        # Create output directories
        categories = ['Rack', 'Switch', 'Port', 'Cable']
        for category in categories:
            os.makedirs(os.path.join(OUTPUT_DIR, category), exist_ok=True)
        
        # Copy original image to static folder for web access
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        original_static_path = f"static/segmented_outputs/original_{base_name}.jpg"
        shutil.copy2(image_path, original_static_path)
        
        # Create demo segmented images by copying the original
        segmented_images = []
        coordinates_data = {}
        
        # Create mock detections for demo
        mock_detections = [
            {'class': 'Rack', 'confidence': 0.85, 'coords': [50, 50, 200, 300]},
            {'class': 'Switch', 'confidence': 0.92, 'coords': [220, 100, 400, 180]},
            {'class': 'Cable', 'confidence': 0.78, 'coords': [100, 320, 350, 380]},
            {'class': 'Port', 'confidence': 0.89, 'coords': [250, 120, 280, 140]}
        ]
        
        for i, detection in enumerate(mock_detections):
            class_name = detection['class']
            confidence = detection['confidence']
            x1, y1, x2, y2 = detection['coords']
            
            # Create output filename
            filename = f"{base_name}_{class_name}_{i}.jpg"
            out_path = os.path.join(OUTPUT_DIR, class_name, filename)
            
            # Copy original image as placeholder (in real implementation, this would be the cropped segment)
            shutil.copy2(image_path, out_path)
            
            rel_path = out_path.replace("\\", "/")
            coordinates_data[rel_path] = {
                "x1": x1, "y1": y1, "x2": x2, "y2": y2,
                "width": x2 - x1, "height": y2 - y1,
                "confidence": confidence,
                "class_name": class_name
            }
            
            segmented_images.append({
                'path': rel_path,
                'class': class_name,
                'original_class': class_name,
                'confidence': confidence,
                'coordinates': {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2}
            })
        
        # Save coordinates
        os.makedirs(os.path.dirname(COORDINATES_FILE), exist_ok=True)
        with open(COORDINATES_FILE, 'w') as f:
            json.dump(coordinates_data, f, indent=2)
        
        # Group images by class
        grouped_images = {}
        for img_data in segmented_images:
            class_name = img_data['class']
            if class_name not in grouped_images:
                grouped_images[class_name] = []
            grouped_images[class_name].append(img_data)
        
        logging.info(f"Demo segmentation complete. Created {len(segmented_images)} mock detections")
        
        # Create mock comparison results for demo
        comparison_results = []
        for img_data in segmented_images:
            comparison_results.append({
                'cropped_image': img_data['path'],
                'category': img_data['class'],
                'name': f"Sample {img_data['class']} Component",
                'description': f"This is a demo {img_data['class'].lower()} component detected in your network infrastructure image.",
                'similarity_score': 0.85 + (len(comparison_results) * 0.02),  # Vary scores slightly
                'matched_image': None,  # No catalog images in demo mode
                'coordinates': img_data['coordinates']
            })

        return {
            'success': True,
            'total_components': len(segmented_images),
            'segmented_images': segmented_images,
            'grouped_images': grouped_images,
            'coordinates_file': COORDINATES_FILE,
            'original_image': '/' + original_static_path,
            'comparison_results': comparison_results,
            'demo_mode': True
        }
        
    except Exception as e:
        logging.error(f"Error in mock process_image: {str(e)}")
        return {'success': False, 'error': str(e)}