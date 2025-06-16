# Network Infrastructure Segmentation Application

## Overview

This is a Flask-based web application that uses YOLO (You Only Look Once) deep learning models to automatically detect and segment network infrastructure components in uploaded images. The application can identify and extract Racks, Switches, Ports, and Cables from images, providing detailed segmentation results with downloadable outputs.

## System Architecture

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Web Server**: Gunicorn for production deployment
- **File Handling**: Werkzeug for secure file uploads
- **Image Processing**: OpenCV and PIL for image manipulation
- **Deep Learning**: YOLO models via Ultralytics for object detection and segmentation

### Frontend Architecture
- **Template Engine**: Jinja2 (Flask's default)
- **CSS Framework**: Bootstrap 5 with dark theme
- **JavaScript**: Vanilla JS for file upload handling and preview
- **Icons**: Font Awesome for UI elements

### Model Architecture
- **General Model**: `best.pt` - Detects Cable, Switch, Rack, and Fuse components
- **Specialized Model**: `port_best.pt` - Specialized for Port detection
- **Inference Engine**: YOLO v8 through Ultralytics library

## Key Components

### Core Application Files
- `app.py`: Flask application initialization and configuration
- `main.py`: Application entry point
- `routes.py`: HTTP route handlers for upload and processing
- `utils/segmentation.py`: Core image processing and YOLO model integration

### Processing Pipeline
- `segment.py`: Standalone segmentation script for batch processing
- `cropped_embeddings.py`: CLIP model integration for feature extraction
- `comparision.py`: Feature comparison and matching utilities

### Frontend Components
- `templates/`: HTML templates using Jinja2
- `static/css/`: Custom styling with Bootstrap integration
- `static/js/`: Client-side JavaScript for upload handling

### Storage Structure
- `uploads/`: Temporary storage for uploaded images
- `static/segmented_outputs/`: Processed segmentation results organized by component type

## Data Flow

1. **Image Upload**: User uploads image through web interface
2. **File Validation**: Server validates file type, size, and format
3. **Model Processing**: 
   - General YOLO model detects Cables, Switches, Racks, and Fuses
   - Specialized Port model detects Port components
4. **Segmentation**: Detected objects are cropped and saved by category
5. **Results Generation**: Coordinates and metadata are saved as JSON
6. **Response**: Web interface displays results with download options

## External Dependencies

### Python Packages
- `flask`: Web framework
- `ultralytics`: YOLO model implementation
- `opencv-python`: Image processing
- `pillow`: Image manipulation
- `numpy`: Numerical operations
- `torch`: PyTorch for deep learning
- `clip`: OpenAI CLIP for embeddings
- `faiss`: Vector similarity search
- `gunicorn`: WSGI HTTP Server

### System Dependencies
- `libGL`, `libGLU`: OpenGL libraries for image processing
- `openssl`: Cryptographic functions
- `postgresql`: Database support (prepared for future use)

## Deployment Strategy

### Development Environment
- Uses Flask's built-in development server
- Debug mode enabled for development
- File watching for automatic reloads

### Production Environment
- Gunicorn WSGI server with auto-scaling deployment
- Configured for binding on all interfaces (0.0.0.0:5000)
- Process reuse and reload capabilities enabled
- 16MB file upload limit for image processing

### Infrastructure Requirements
- Python 3.11+ runtime environment
- CUDA support optional (falls back to CPU)
- Sufficient storage for model files and temporary processing

## Recent Changes
- June 16, 2025: Extended segmentation pipeline with embedding comparison system
- Added catalog matching using CLIP embeddings and FAISS similarity search
- Integrated cropped_embeddings.py and comparison.py for component identification
- Results displayed in card format with similarity scores
- Automatic cleanup of previous outputs on each upload
- Support for catalog files: all_categories_data.pkl and metadata.pkl

## Changelog
- June 16, 2025. Initial setup

## User Preferences

Preferred communication style: Simple, everyday language.