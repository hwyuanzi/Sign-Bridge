from flask import Blueprint, current_app, jsonify
from services.prediction_service import (
    get_latest_prediction,
    get_recent_predictions,
    get_prediction_stats,
)

api_bp = Blueprint("api", __name__)


@api_bp.route("/health")
def health():
    return jsonify({"status": "ok"})


@api_bp.route("/latest")
def latest():
    latest_prediction = get_latest_prediction()
    if latest_prediction is None:
        return jsonify(
            {
                "timestamp": None,
                "predicted_label": "N/A",
                "confidence": 0.0,
                "current_text": "",
                "source": "",
                "frame_number": None,
            }
        )
    return jsonify(latest_prediction)


@api_bp.route("/recent")
def recent():
    data = get_recent_predictions(current_app.config["RECENT_LIMIT"])
    return jsonify(data)


@api_bp.route("/stats")
def stats():
    return jsonify(get_prediction_stats(100))