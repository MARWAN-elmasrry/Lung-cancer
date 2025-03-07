# from flask import Flask, request, jsonify
# import numpy as np
# import joblib

# # Load trained model and scaler
# model = joblib.load("best_model.pkl")  
# scaler = joblib.load("scaler.pkl")

# # joblib.dump(model, "lung_cancer_model_v1_1_3.pkl", compress=3)

# app = Flask(__name__)

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Extract JSON data
#         data = request.get_json()
#         features = data['features']

#         # Debugging: Print received features
#         print("Received features:", features)
        
#         # Ensure gender is encoded correctly
#         if features[0] == "M":
#             features[0] = 1
#         elif features[0] == "F":
#             features[0] = 0
        
#         # Convert all values to float
#         features = np.array(features, dtype=float).reshape(1, -1)
        
#         # Debugging: Print processed features
#         print("Processed features:", features)
        
#         # Check feature count before transformation
#         if features.shape[1] != scaler.n_features_in_:
#             return jsonify({"error": f"Expected {scaler.n_features_in_} features , but got {features.shape[1]}."})

#         # Scale input features
#         features_scaled = scaler.transform(features)
        
#         # Make prediction
#         prediction = model.predict(features_scaled)
        
#         return jsonify({"lung_cancer": int(prediction[0])})
    
#     except Exception as e:
#         return jsonify({"error": str(e)})

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)



# from flask import Flask, request, jsonify
# import numpy as np
# import joblib

# # Load trained model (RandomForestClassifier) and scaler
# model = joblib.load("best_model.pkl")  
# scaler = joblib.load("scaler.pkl")

# app = Flask(__name__)

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Extract JSON data
#         data = request.get_json()
#         features = data['features']

#         # Debugging: Print received features
#         print("Received features:", features)
        
#         # Ensure gender is encoded correctly
#         if features[0] == "M":
#             features[0] = 1
#         elif features[0] == "F":
#             features[0] = 0
        
#         # Convert all values to float
#         features = np.array(features, dtype=float).reshape(1, -1)
        
#         # Debugging: Print processed features
#         print("Processed features:", features)
        
#         # No need to transform features for RandomForestClassifier
#         features_transformed = features  

#         # Make prediction
#         prediction = model.predict(features_transformed)
        
#         return jsonify({"lung_cancer": int(prediction[0])})
    
#     except Exception as e:
#         return jsonify({"error": str(e)})

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)


from flask import Flask, request, jsonify
import numpy as np
import joblib

# Load trained model (KNeighborsClassifier)
model = joblib.load("best_model.pkl")  
scaler = joblib.load("scaler.pkl")

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract JSON data
        data = request.get_json()
        features = data['features']

        # Ensure gender is encoded correctly
        if features[0] == "M":
            features[0] = 1
        elif features[0] == "F":
            features[0] = 0
        
        # Convert all values to float
        features = np.array(features[:10], dtype=float).reshape(1, -1)  # Keep only 10 features

        # Make prediction
        prediction = model.predict(features)
        
        return jsonify({"lung_cancer": int(prediction[0])})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
