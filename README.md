# Status of project: ON GOING

# Face Recognition
This project is based on [MTCNN](https://github.com/ipazc/mtcnn) and pretend to work with Face Recognition, where faces might has oclusion of its parts.

![Demo](https://github.com/RodrigoCMoraes/face_recognition/blob/master/demo_faces.jpg)

# Features implemented:
* Detect faces
* Draw ROI in faces
* Save faces detected
* Calculate time of operations

# Features to be implemented:
* Augment face images ([TensorFlow](https://github.com/tensorflow/tensorflow))
* Extract features(embeddings) from augmented images([FaceNet](https://github.com/davidsandberg/facenet))
* Train classifier to recognize people([KNN CUDA](https://github.com/chrischoy/knn_cuda))

# Setup used for generate this code:
* For Windows and Linux are used latest Python from [Anaconda](https://www.anaconda.com/download/#linux)
* SO versions: Windows 10 x64 Pro and Linux Mint 19 x64
* Conda environment with commands:
  ```
  # create environment
  conda create -n ai python=3.6
  
  # activate environment Windows
  conda activate ai
  
  # activate environment in Linux
  source activate ai
  
  # install dependencies with environment activated - windows
  pip install -r requirements_windows.txt # windows
  
  # install dependencies with environment activated - linux
  pip install -r requirements_linux.txt   # linux
  ```
# Demo
1. Clone this repository
2. Create environment
3. Install dependencies on environment
4. Execute script mtcnn_demo.py
```
python mtcnn_demo.py
```

## Expected Terminal output
```
(load_detector) time: 0.89s                                                                                                                                                                                                                    
(load_image) time: 1.29s                                                                                                                                                                                                                       
(detect_faces) time: 0.40s                                                                                                                                                                                                                     
3468                                                                                                                                                                                                                                           
(write_image) time: 0.00s                                                                                                                                                                                                                      
4800                                                                                                                                                                                                                                           
(write_image) time: 0.00s                                                                                                                                                                                                                      
4107                                                                                                                                                                                                                                           
(write_image) time: 0.00s                                                                                                                                                                                                                      
3675                                                                                                                                                                                                                                           
(write_image) time: 0.00s                                                                                                                                                                                                                      
3888                                                                                                                                                                                                                                           
(write_image) time: 0.00s                                                                                                                                                                                                                      
3468                                                                                                                                                                                                                                           
(write_image) time: 0.00s                                                                                                                                                                                                                      
4332                                                                                                                                                                                                                                           
(write_image) time: 0.00s                                                                                                                                                                                                                      
3072                                                                                                                                                                                                                                           
(write_image) time: 0.00s                                                                                                                                                                                                                      
4107                                                                                                                                                                                                                                           
(write_image) time: 0.00s                                                                                                                                                                                                                      
3888                                                                                                                                                                                                                                           
(write_image) time: 0.00s                                                                                                                                                                                                                      
2700                                                                                                                                                                                                                                           
(write_image) time: 0.00s                                                                                                                                                                                                                      
(crop_faces) time: 0.00s                                                                                                                                                                                                                       
(draw_faces) time: 0.00s                                                                                                                                                                                                                       
(write_image) time: 0.00s
```
## Expected output images:
![Demo](https://github.com/RodrigoCMoraes/face_recognition/blob/master/demo_faces.jpg)

| | | | |
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
|<img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/docs/face_0.jpg">  |  <img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/docs/face_3.jpg">|<img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/docs/face_6.jpg">|<img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/docs/face_9.jpg">|
|<img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/docs/face_1.jpg">  |  <img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/docs/face_4.jpg">|<img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/docs/face_7.jpg">|<img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/docs/face_10.jpg">|
|<img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/docs/face_2.jpg">  |  <img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/docs/face_5.jpg">|<img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/docs/face_8.jpg">||
