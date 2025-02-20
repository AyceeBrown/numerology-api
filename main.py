from flask import Flask, request, jsonify
from flask_cors import CORS
CORS(app)
import datetime

app = Flask(__name__)

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
        # Parse request data
        data = request.get_json()
        birth_month = int(data.get("birth_month"))
        birth_day = int(data.get("birth_day"))
        venus_sign = data.get("venus_sign", "Unknown")
        venus_house = data.get("venus_house", "Unknown")
        current_year = datetime.datetime.now().year

        # Calculate Personal Year
        personal_year = calculate_personal_year(birth_month, birth_day, current_year)
        personal_year_description = personal_year_data.get(personal_year, "No data available")

        # Generate Response
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

if __name__ == '__main__':
    import os
port = int(os.environ.get("PORT", 10000))  # Render assigns a dynamic PORT
app.run(host="0.0.0.0", port=port, threaded=True)
"Fixed port issue for Render"
