# Python Image Processing Application

## Overview
This **Python Image Processing Application** demonstrates fundamental image processing techniques using **OpenCV** and **NumPy**. The project provides a comprehensive suite of features for manipulating and analyzing images, showcasing the power and flexibility of modern image processing libraries.

## Features
- **Edge Detection**: Implements various edge detection algorithms including:
  - Canny Edge Detection
  - Sobel Edge Detection
  - Laplacian Edge Detection
  - Deriche Edge Detection
- **Face Detection**:
  - Static and real-time face detection using Haar cascades.
- **Image Enhancement**:
  - Image sharpening and gamma correction.
- **Thresholding Techniques**:
  - Otsu's thresholding
  - Adaptive thresholding
- **Object Detection**:
  - Watershed algorithm for object segmentation.
- **Image Analysis**:
  - Histogram analysis and contour detection.
- **Interactive Visualization**:
  - Real-time demonstrations of various algorithms.

## Project Structure
```
imageProcessing-main
│
├── adaptive_threshold_example.py      # Adaptive thresholding example
├── apply_gamma_correction.py          # Gamma correction example
├── apply_sobel_and_show_edges.py      # Sobel edge detection
├── canny_edge_detection.py            # Canny edge detection example
├── cassade_detect_faces.py            # Haar cascade face detection
├── contour_detection.py               # Contour detection example
├── deriche_edge_detection.py          # Deriche edge detection
├── face_detection.py                  # Face detection example
├── harris_corner_detection.py         # Harris corner detection
├── image_histogram_example.py         # Image histogram analysis
├── image_processing_example.py        # General image processing example
├── image_sharpening_example.py        # Image sharpening example
├── laplacian_edge_detection.py        # Laplacian edge detection
├── live_face_detection.py             # Real-time face detection
├── otsu_threshold_example.py          # Otsu's thresholding example
├── watershed_algorithm.py             # Watershed segmentation
├── watershed_algorithm_2.py           # Alternate watershed implementation
├── haarcascade_frontalface_default.xml # Haar cascade classifier file
├── main.py                            # Entry point for the application
```

## Technologies Used
- **Programming Language**: Python 3.9+
- **Libraries**:
  - **OpenCV**: For image processing and computer vision tasks
  - **NumPy**: For numerical computations
- **Algorithms**:
  - Edge detection: Canny, Sobel, Laplacian, Deriche
  - Segmentation: Otsu, Adaptive Thresholding, Watershed
  - Feature Detection: Harris Corner, Contour Detection

## Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.9 or later
- Required Python libraries:
  ```bash
  pip install opencv-python-headless numpy
  ```

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/imageProcessing.git
   cd imageProcessing-main/pythonProject
   ```

2. Run the main application:
   ```bash
   python main.py
   ```

### Configuration
- Modify specific scripts to use custom images by replacing file paths.
- Ensure the `haarcascade_frontalface_default.xml` file is in the correct directory for face detection.

## Usage
- **Run Individual Scripts**: Execute any script to test specific functionality. Example:
  ```bash
  python canny_edge_detection.py
  ```
- **Real-Time Detection**: Use `live_face_detection.py` for live face tracking using a webcam.
- **Experiment**: Modify parameters in scripts (e.g., threshold values) to observe changes in output.

## Contribution
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For any inquiries or feedback, feel free to reach out:
- **Email**: eraykelesk@gmail.com
- **LinkedIn**: [Eray Keleş](https://linkedin.com/in/eraykeles)
