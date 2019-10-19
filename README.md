# Status of project: ON GOING

# Face Recognition
This project is based on [MTCNN](https://github.com/ipazc/mtcnn) and pretend to work with Face Recognition, where faces might has oclusion of its parts.

![Demo](https://github.com/RodrigoCMoraes/face_recognition/blob/master/img/demo_faces.jpg)

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
* SO versions: Windows 10 x64 Pro and Linux Mint and Ubuntu 19 x64
* Conda environment with commands:
  ```
  # create environment
  conda create -f environment.yml
  
  # activate environment
  conda activate face_recognition
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
![Demo](https://github.com/RodrigoCMoraes/face_recognition/blob/master/img/demo_faces.jpg)

| | | | |
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
|<img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/img/face_0.jpg">  |  <img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/img/face_3.jpg">|<img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/img/face_6.jpg">|<img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/img/face_9.jpg">|
|<img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/img/face_1.jpg">  |  <img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/img/face_4.jpg">|<img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/img/face_7.jpg">|<img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/img/face_10.jpg">|
|<img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/img/face_2.jpg">  |  <img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/img/face_5.jpg">|<img width="80" src="https://github.com/RodrigoCMoraes/face_recognition/blob/master/img/face_8.jpg">||
