# RackTrack - Rack Component Analysis & Segmentation Application

## Overview

RackTrack is a Flask-based web application that uses AI deep learning models to automatically detect and segment rack components in uploaded images. The application provides detailed analysis results with downloadable outputs and features a modern sky blue and white themed interface.

## System Architecture

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Web Server**: Gunicorn for production deployment
- **File Handling**: Werkzeug for secure file uploads
- **Image Processing**: OpenCV and PIL for image manipulation
- **Deep Learning**: YOLO models via Ultralytics for object detection and segmentation

### Frontend Architecture
- **Template Engine**: Jinja2 (Flask's default)
- **CSS Framework**: Bootstrap 5 with custom sky blue and white theme
- **JavaScript**: Vanilla JS for file upload handling and preview
- **Icons**: Font Awesome for UI elements
- **Design**: Sky blue gradient background with translucent white cards

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
- June 24, 2025: Massively expanded home page with comprehensive enterprise-grade content
  - Added Industry Statistics section with animated progress bars and adoption metrics
  - Created Advanced Capabilities section with interactive AI brain visualizations
  - Implemented Success Stories section with detailed case studies and ROI metrics
  - Added Research & Innovation section with timeline and academic partnerships
  - Enhanced all sections with sophisticated animations and visual effects
  - Increased content depth with real-world examples and quantifiable benefits
  - Added comprehensive JavaScript for advanced interactivity and scroll animations
  - Created enterprise-focused content showcasing Fortune 500 adoption
- June 24, 2025: Created new animated logo system with multiple variants
  - Designed dynamic SVG logo with animated rack components and neural network
  - Added interactive hover effects with rotating background and glow effects
  - Created favicon and alternative logo versions (dark theme, text variant)
  - Implemented advanced logo animations with pulsing slots and neural indicators
  - Enhanced brand identity with modern gradient systems and holographic effects
- June 24, 2025: Complete creative website redesign implementation
  - Transformed background with advanced multi-layered animated gradients
  - Implemented glassmorphism effects throughout the interface
  - Added creative floating geometric shapes with organic animations
  - Enhanced header with shimmer effects and advanced backdrop blur
  - Created modern card system with gradient borders and creative shadows
  - Developed creative button designs with shine effects and transformations
  - Added hero section with particle systems and dynamic visual effects
  - Implemented advanced color palette with modern CSS custom properties
- June 23, 2025: Fixed full-width layout issue for complete page utilization
  - Updated CSS to ensure 100vw width coverage across all sections
  - Modified container classes to use container-fluid with full width
  - Fixed overflow-x hidden to prevent horizontal scrolling
  - Ensured all sections and components span complete page width
- June 23, 2025: Added authentication system with login/logout functionality
  - Removed "Analyze" from header navigation for non-authenticated users
  - Replaced "Get Started" with "Sign In" button in header
  - Created professional login page with demo credentials (1234/1234)
  - Protected analyze page and upload functionality with login requirements
  - Added Flask-Login for session management and user authentication
  - Updated navigation to show different options for authenticated/guest users
- June 23, 2025: Complete white and blue theme redesign with enhanced UX
  - Transformed entire website to clean white and blue color scheme (#2563eb primary)
  - Fixed JavaScript errors in upload interface with null-safe element checking
  - Enhanced drag-and-drop upload with blue gradient shadows and improved visual feedback
  - Added technology badges with color-coded categories (primary, accent, success)
  - Implemented blue shadow effects throughout for consistent visual hierarchy
  - Updated gradient backgrounds and icon styling to match blue theme
  - Enhanced button hover states with blue shadow effects
  - Improved responsive design for mobile-friendly experience
- June 23, 2025: Modern SaaS UI/UX redesign inspired by Vortasky AI
  - Implemented modern design system with CSS custom properties and Inter font
  - Redesigned hero section with gradient text, modern cards, and enhanced visual hierarchy
  - Updated color palette to use indigo/purple primary colors with improved contrast
  - Added modern button styles with gradients and hover animations
  - Enhanced feature cards with icon backgrounds and technology tags
  - Implemented scroll-aware navigation with backdrop blur effects
  - Created responsive grid layouts with modern shadows and spacing
  - Added smooth scrolling and micro-interactions throughout the interface
- June 23, 2025: Complete professional website transformation
  - Added comprehensive landing page with hero section, features overview, and call-to-action
  - Created dedicated pages: Home, Features, About, Contact, and Analysis
  - Implemented full navigation menu with responsive design
  - Enhanced CSS with professional styling, animations, and mobile responsiveness
  - Added footer with social links and company information
  - Created contact form with FAQ accordion section
  - Separated analysis functionality to dedicated /analyze route
  - Maintained existing upload and processing functionality
- June 19, 2025: Rebranded application to "RackTrack"
  - Updated application name across all interfaces and documentation
  - Changed icons from generic images to server/rack specific icons
  - Enhanced catalog matching modal with comprehensive component details
  - Added side-by-side layout showing highlighted original image and detailed component information
  - Fixed JavaScript errors preventing modal functionality
  - Improved robustness of upload.js to prevent errors on results pages
- June 17, 2025: Complete UI redesign with sky blue and white theme
  - Implemented gradient background (white to sky blue to deeper blue)
  - Updated to light Bootstrap theme with custom CSS overrides
  - Applied translucent white cards with blue accent borders
  - Updated buttons, headers, and UI elements with sky blue color scheme
- June 16, 2025: Extended segmentation pipeline with embedding comparison system
  - Added catalog matching using CLIP embeddings and FAISS similarity search
  - Integrated cropped_embeddings.py and comparison.py for component identification
  - Results displayed in card format with similarity scores
  - Support for catalog files: all_categories_data.pkl and metadata.pkl

## Changelog
- June 16, 2025. Initial setup

## User Preferences

- Preferred communication style: Simple, everyday language
- Design theme: Clean white and blue color scheme with professional header
- UI/UX: User-friendly and appealing modern design with highlighted branding
- Functionality: Complete drag-and-drop upload interface
- Layout preference: 90% viewport width layout for maximum content display
- Content preference: Clean, simple design that's not too heavy or overwhelming
- Design approach: Elegant and lightweight with essential information only