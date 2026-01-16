from flask import Flask,request,jsonify
import joblib

MODEL_VERSION="1.0.0"

#Load saved model

model=joblib.load("customer_purchase_model.pkl")

app=Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "model_version": MODEL_VERSION
    })

@app.route("/predict",methods=["POST"])
def predict():
    data=request.get_json()

    if not data or "customer_visits" not in data:
        return jsonify({"error":"customer_visits is required"}),400

    try:
        visits=int(data["customer_visits"])
    except ValueError:
        return jsonify({"error":"customer_visits must be a number"}),400
    
    if visits<0:
        return jsonify({"error": "customer_visits must be >= 0"}), 400

    prediction=model.predict([[visits]])
    probability=model.predict_proba([[visits]])

    confidence=probability[0][1]*100

    return jsonify({
        "model_version": MODEL_VERSION,
        "customer_visits": visits,
        "purchase_prediction": int(prediction[0]),
        "confidence_percent": round(float(confidence), 2)
    })


if __name__=="__main__":
    app.run(debug=True)


