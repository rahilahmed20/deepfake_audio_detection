from flask import Flask, request, jsonify
from flask_cors import CORS
import librosa
import numpy as np
from keras.models import load_model

class AudioFakeDetector:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.model = load_model('models/model_audio.h5')
        self.app.route('/detect_fake', methods=['POST'])(self.predict_fake)

    def detect_fake(self, filename):
        sound_signal, sample_rate = librosa.load(filename, res_type="kaiser_fast")
        mfcc_features = librosa.feature.mfcc(y=sound_signal, sr=sample_rate, n_mfcc=40)
        mfccs_features_scaled = np.mean(mfcc_features.T, axis=0)
        mfccs_features_scaled = mfccs_features_scaled.reshape(1, -1)
        result_array = self.model.predict(mfccs_features_scaled)
        result_classes = ["FAKE", "REAL"]
        result = np.argmax(result_array[0])
        return result_classes[result]

    def predict_fake(self):
        file = request.files['file']
        filename = 'temp_audio_file.wav'
        file.save(filename)
        result = self.detect_fake(filename)
        return jsonify({'result': result})

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    detector = AudioFakeDetector()
    detector.run()