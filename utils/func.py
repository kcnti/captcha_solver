from utils.recog import solve
import urllib.request
import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

def checkIMG(captcha_img, folder, target_array):

    correct = []
    test_case = []

    for n, url_image in enumerate(captcha_img):
        path = folder+str(n)+'.png'
        dl = urllib.request.urlretrieve(url_image, path)

        # path = tf.convert_to_tensor(path)
        result = solve(path)
        for keyword in result:
            if keyword in target_array:
                correct.append(url_image)
                test_case.append(keyword)
                break

    return correct, test_case