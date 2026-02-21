from flask import Flask, render_template, request, jsonify
import joblib
import os
import nltk

# --- HACKATHON PRO-TIP: Auto-download NLTK data ---
# This prevents the app from crashing on the judge's computer
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

app = Flask(__name__)

# --- AI MODEL LOADING ---
# Zora tries to load her 'brain'. If files are missing, she uses Keyword Mode.
MODEL_PATH = 'model.pkl'
VECTORIZER_PATH = 'tfidf.pkl'
AI_READY = False

try:
    if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
        model = joblib.load(MODEL_PATH)
        tfidf = joblib.load(VECTORIZER_PATH)
        AI_READY = True
        print("✅ ZORA NEURAL NETWORK: ONLINE")
    else:
        print("⚠️ ZORA NEURAL NETWORK: OFFLINE (Using Keyword Fallback)")
except Exception as e:
    print(f"❌ AI LOAD ERROR: {e}")

# --- HELPER LOGIC ---
def manual_check(text):
    """Fallback keyword detection for high-distress signals."""
    risk_keywords = [
        'suicide', 'kill myself', 'end it', 'hurt myself', 'alone', 
        'give up', 'tired of living', 'no one loves me', 'goodbye',
        'depressed', 'help me', 'sos', 'help', 'hurt', 'sad'
    ]
    return 1 if any(word in text for word in risk_keywords) else 0

# --- ROUTES ---

@app.route('/')
def index():
    """Renders the main Zora Interface."""
    return render_template('main.html')

@app.route('/analyze_api', methods=['POST'])
def analyze_api():
    """Handles text analysis from the chat and social media scan."""
    user_text = request.form.get('message', '').lower().strip()
    
    if not user_text:
        return jsonify({'prediction': 0, 'status': 'empty'})

    # Intervention Logic: Use AI if ready, otherwise use keywords
    if AI_READY:
        try:
            vectorized_text = tfidf.transform([user_text])
            prediction = int(model.predict(vectorized_text)[0])
        except:
            prediction = manual_check(user_text)
    else:
        prediction = manual_check(user_text)

    return jsonify({
        'prediction': prediction,
        'received': user_text,
        'ai_active': AI_READY
    })

if __name__ == '__main__':
    print('--- ZORA STARTING ON http://127.0.0.1:5000 ---')
    app.run(debug=True)