# remove tensorflow messages and deprecation from mtcnn packages
import tensorflow as tf
import os
tf.logging.set_verbosity(tf.logging.ERROR)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
################################################################

# decorator to time function 
def timeit(method):
    from time import time
    def timed(*args, **kw):
        start = time()
        result = method(*args, **kw)
        end = time()
        print(f'({method.__name__}) time: {end - start:.2f}s')
        return result
    return timed

@timeit
def load_detector():
    from mtcnn.mtcnn import MTCNN
    return MTCNN()

@timeit
def load_image():
    from os import system
    url_image = 'https://cdn.foxsports.com.br/sites/foxsports-br/files/img/scaled/630x/notes/materia/selecao-br-servia-lucasfigcbf-time-950.jpg?ver=34efb875-0e66-4f7d-afba-62751615638c'
    system(f'curl --silent {url_image} -o demo.jpg')
    import cv2
    return cv2.imread("demo.jpg")

@timeit
def detect_faces(detector, image):
    return detector.detect_faces(image)

@timeit
def crop_faces(results, image):
    import cv2
    for i, result in enumerate(results):
        bb = result['box']
        keypoints = result['keypoints']
        face = image[bb[1]:bb[1]+bb[3] , bb[0]:bb[0]+bb[3]]  
        print(face.size)
        write_image(f'face_{i}.jpg', face)

@timeit
def draw_faces(result_from_detector, image):
    import cv2
    for result in result_from_detector:
        bounding_box = result['box']
        keypoints = result['keypoints']
        cv2.rectangle(image, (bounding_box[0], bounding_box[1]),
                             (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                             (0,155,255),
                             2)
    return image

@timeit
def write_image(filename, image):
    import cv2
    cv2.imwrite(filename, image)

if __name__ == "__main__":
    detector = load_detector()
    image = load_image()
    result = detect_faces(detector, image)
    crop_faces(result, image)
    image = draw_faces(result, image)
    write_image('demo_faces.jpg', image)
