from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
import joblib
import os

app = Flask(__name__)

# ── Load model & encoders once at startup ─────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model    = pickle.load(open(os.path.join(BASE_DIR, 'model_rf.pkl'), 'rb'))
encoders = joblib.load(os.path.join(BASE_DIR, 'encoders.pkl'))

FEATURES = [
    'latitude', 'longitude', 'speed', 'acceleration', 'steering_angle',
    'heading', 'trip_duration', 'trip_distance', 'fuel_consumption', 'rpm',
    'brake_usage', 'lane_deviation', 'weather_conditions', 'road_type',
    'traffic_condition', 'stop_events', 'route_deviation_score',
    'acceleration_variation', 'behavioral_consistency_index',
    'hour', 'day_of_week', 'is_weekend', 'is_night'
]

CAT_FEATURES = ['weather_conditions', 'road_type', 'traffic_condition']

ADVICE = {
    'Low'   : ('Safe trip! Your driving behaviour is within normal parameters.',
               'Keep maintaining safe speed, stay in lanes, and follow traffic rules.'),
    'Medium': ('Moderate risk detected. Please drive more carefully.',
               'Reduce speed, increase following distance, and stay alert to road conditions.'),
    'High'  : ('HIGH RISK! Dangerous driving behaviour detected.',
               'Pull over safely if possible. Reduce speed immediately and avoid sudden manoeuvres.'),
}

def encode_value(le, value):
    value = str(value)
    if value in le.classes_:
        return int(le.transform([value])[0])
    return -1


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        user_input = {}

        # Parse and validate all inputs
        int_fields    = ['steering_angle', 'brake_usage', 'stop_events',
                         'hour', 'day_of_week', 'is_weekend', 'is_night']
        float_fields  = ['latitude', 'longitude', 'speed', 'acceleration',
                         'heading', 'trip_duration', 'trip_distance',
                         'fuel_consumption', 'rpm', 'lane_deviation',
                         'route_deviation_score', 'acceleration_variation',
                         'behavioral_consistency_index']

        for f in float_fields:
            user_input[f] = float(data[f])
        for f in int_fields:
            user_input[f] = int(data[f])

        # Encode categorical
        for col in CAT_FEATURES:
            user_input[col] = encode_value(encoders[col], data[col])

        # Build feature array in correct order
        X_input = np.array([[user_input[col] for col in FEATURES]])

        # Predict
        prediction  = model.predict(X_input)[0]
        risk_label  = encoders['risk_level'].inverse_transform([prediction])[0]

        # Probabilities
        proba       = model.predict_proba(X_input)[0]
        classes     = encoders['risk_level'].classes_.tolist()
        prob_dict   = {cls: round(float(p) * 100, 1) for cls, p in zip(classes, proba)}

        advice_short, advice_long = ADVICE.get(risk_label, ('', ''))

        return jsonify({
            'success'      : True,
            'risk_level'   : risk_label,
            'probabilities': prob_dict,
            'advice_short' : advice_short,
            'advice_long'  : advice_long,
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)
