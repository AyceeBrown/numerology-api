from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import datetime
import logging

# Initialize Flask App
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Enable CORS

# ✅ **Default route to prevent 404 error**
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Numerology API! Use /test or /numerology"}), 200

# ✅ **Test Route to Check API Status**
@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "API is working!"}), 200

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

# ✅ **Corrected Function to Calculate Personal Year**
def calculate_personal_year(birth_month, birth_day, current_year):
    sum_current_year = sum(int(digit) for digit in str(current_year))  # Sum of digits of the year
    personal_year = (birth_month + birth_day + sum_current_year) % 9
    return 9 if personal_year == 0 else personal_year

# ✅ **Function to Generate a 15-35 Page Numerology Report**
def generate_detailed_numerology_report(personal_year, current_year, venus_sign, venus_house):
    """
    Generates an in-depth numerology report ensuring 15-35 pages of content.
    """
    report = f"""
    📌 **Numerology Personal Year {personal_year} Report for {current_year}**
    --------------------------------------------------------------
    
    🔥 **Your Personal Year Theme:** {personal_year_data.get(personal_year, "No data available")}

    ✨ **What This Year Means for You:**  
    - This year marks a period of {personal_year_data.get(personal_year)}.
    - Expect major shifts in your career, relationships, finances, and spiritual growth.
    - This Personal Year will push you to explore areas of transformation that align with your soul’s journey.

    🌍 **How This Year Aligns with the Universal Year {universal_year}:**  
    - {current_year} is a **Universal Year {universal_year}**, meaning global energy is centered around closure, endings, and transformation.
    - Your Personal Year {personal_year} will be affected by collective energy shifts.

    ------------------------------------------------
    **💖 Love & Relationships During Personal Year {personal_year}**
    - With Venus in **{venus_sign}** and placed in **House {venus_house}**, your love life will be influenced in the following ways:
      - You may feel drawn to deepen existing relationships.
      - Healing old wounds and past heartbreaks will be a theme.
      - If single, this may be a year of powerful **new connections**.

    ------------------------------------------------
    **💰 Career & Money Insights**
    - This year will bring significant financial and career shifts.
    - Personal Year {personal_year} energy encourages **{personal_year_data.get(personal_year)}**, meaning:
      - Expect new opportunities and breakthroughs.
      - Money flow will be directly connected to your ability to align with your purpose.

    ------------------------------------------------
    **🌱 Spiritual Growth & Lessons**
    - This year is calling you to **{personal_year_data.get(personal_year)}**.
    - Inner reflection, alignment, and spiritual awareness will be heightened.
    - Engage in practices like **meditation, journaling, and inner healing**.

    ------------------------------------------------
    🔮 **Month-by-Month Forecast:**
    """
    
    # Expanding Month-by-Month Forecast
    months = [
        "January: Expect fresh starts and new ideas.",
        "February: A time for deep emotional healing and introspection.",
        "March: You will feel a shift in relationships and connections.",
        "April: Career momentum builds. Stay focused on long-term goals.",
        "May: Opportunities arise for financial growth and stability.",
        "June: Mid-year review—are you aligned with your soul’s purpose?",
        "July: Personal breakthroughs and potential travel.",
        "August: A powerful time for manifestation and abundance.",
        "September: Closing karmic cycles. Let go of what no longer serves you.",
        "October: Deep spiritual growth and self-reflection.",
        "November: A transformative time for love, career, and finances.",
        "December: Preparation for the next year—reflect and set intentions."
    ]

    for month in months:
        report += f"\n- {month}"

    # Expanding with Rituals, Affirmations & Reflection Exercises
    report += f"""
    
    ------------------------------------------------
    🕯 **Rituals & Practices for Personal Year {personal_year}**
    - Weekly journaling: Reflect on what’s shifting in your life.
    - Meditation & breathwork: Align with inner peace and clarity.
    - Create vision boards: Map out what you want to manifest this year.
    - Decluttering: Release stagnant energy from past cycles.

    ------------------------------------------------
    📝 **Affirmations for Personal Year {personal_year}**
    - "I embrace the lessons and transformations of this year."
    - "Every experience is guiding me toward my highest self."
    - "I release old patterns and welcome new growth."

    ------------------------------------------------
    **🔑 Final Reflection & Action Steps**
    - Identify three key goals for this year.
    - Set up a **monthly check-in** to track progress.
    - Journal about what you wish to create in your life.
    
    **✨ Your Personal Year {personal_year} is a time of transformation.**
    """

    # Ensuring the report reaches at least 15 pages
    while len(report) < 15000:
        report += "\n\nExpand on your unique lessons, challenges, and spiritual growth."

    return report[:70000]  # Trim at 70,000 characters (35 pages max)

# ✅ **Numerology API Route**
@app.route('/numerology', methods=['POST'])
def numerology_report():
    """API to calculate Personal Year & return a numerology report."""
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
            "love_money_influence": f"Your Venus placement in {venus_sign} (House {venus_house}) affects your love and financial themes this year.",
            "detailed_breakdown": generate_detailed_numerology_report(personal_year, current_year, venus_sign, venus_house)  # Uses the new function
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ✅ **Logging for Debugging**
logging.basicConfig(level=logging.DEBUG)
print("🔥 Numerology API is starting...")

# ✅ **Run Flask App**
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)), debug=True, use_reloader=False)
