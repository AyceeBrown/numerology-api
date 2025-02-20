import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)  # Initialize Flask first
CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "API is working instantly!"}), 200
CORS(app)  # Now apply CORS

# Universal Year for 2025
universal_year = 9

# Personal Year Meanings
personal_year_data = {
    1: "A year of fresh starts, independence, and leadership.",
    2: "A year of patience, relationships, and emotional healing.",
    3: "A year of creativity, joy, and self-expression.",
    4: "A year of discipline, hard work, and stability.",
    5: "A year of change, movement, and adventure.",
    6: "A year of love, responsibility, and family.",
    7: "A year of deep reflection, spirituality, and learning.",
    8: "A year of power, success, and financial growth.",
    9: "A year of closure, endings, and transformation."
}

# Function to calculate Personal Year
def calculate_personal_year(birth_month, birth_day, current_year):
    personal_year = (birth_month + birth_day + current_year) % 9
    return 9 if personal_year == 0 else personal_year

@app.route('/numerology', methods=['POST'])
def numerology_report():
    """Flask API to calculate Personal Year & return a numerology report."""
    try:
        data = request.get_json()
        birth_month = int(data.get("birth_month"))
        birth_day = int(data.get("birth_day"))
        venus_sign = data.get("venus_sign", "Unknown")
        venus_house = data.get("venus_house", "Unknown")
        current_year = datetime.datetime.now().year

        personal_year = calculate_personal_year(birth_month, birth_day, current_year)
        personal_year_description = personal_year_data.get(personal_year, "No data available")

        response = {
            "personal_year": personal_year,
            "year": current_year,
            "theme": personal_year_description,
            "universal_year_influence": f"Since {current_year} is a Universal Year {universal_year}, your Personal Year {personal_year} is influenced by collective transformation and endings.",
            "love_money_influence": f"Your Venus placement in {venus_sign} (House {venus_house}) affects your love and financial themes this year."
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Use Render’s dynamic port
port = int(os.environ.get("PORT", 10000))
import logging

logging.basicConfig(level=logging.DEBUG)
print("🔥 Numerology API is starting...")
print(f"Running on PORT {port}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)), debug=True)


