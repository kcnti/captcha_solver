import sys
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import resnet50

def solve(path):
    model = resnet50.ResNet50()

    picture = image.load_img(path, target_size=(224, 224))
    x = image.img_to_array(picture)
    x = np.expand_dims(x, axis=0)
    x = resnet50.preprocess_input(x)
    predictions = model.predict(x)
    predicted_classes = resnet50.decode_predictions(predictions, top=5)
    result = []
    for imagenet_id, name, likelihood in predicted_classes[0]:
        # print(" - {}: {}".format(name, likelihood))
        result.append(name)
    return result

if __name__ == "__main__":
    solve('/')