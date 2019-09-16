from flask import Flask
from keras.models import load_model
from keras.application.resnet50 import ResNet50

app = Flask(__name__)

MODEL_PATH = 'models/my_model.h5' # this is where models file will be stored

model = ResNet50(weights = 'imagenet')


@app.route('/')
def index():
    return render_template('index.html')  # index method will call html page and render it

def model_predict(img_path, model):
    img = image.load_img(img_path)
    x = image.img_to_array(img)
    preds = model.predict(x)
    return preds




@app.route('/predict', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(file_path)
        # below line does prediction we call model_predict method and then give file path and model
        preds = model_predict(file_path, model)
        # it will help decode what preditcion machine does and return first prediction
        pred_class = decode_predictions(preds, top=1)
        return pred_class
