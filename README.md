# 🌌 ZORA | Neural Guardian Interface

ZORA is an AI-driven emotional gatekeeper designed to protect neural health. It intercepts users before they enter the "Sanctuary" by scanning their current emotional state (via social media posts or tweets) using a Machine Learning model.

## 🚀 System Architecture
1. **The Gatekeeper**: A pre-interface overlay that performs a "Neural Scan."
2. **The Brain**: A Flask backend using `Scikit-learn` and `Joblib` to process text.
3. **The Intervention**: If "High Risk" is detected, the app locks the dashboard and forces an "Emergency Recovery" sequence (Sensory Anchor & Orb Games).

## 🛠️ Installation & Setup

### 1. Prerequisites
Ensure you have Python installed, then install the required neural libraries:
```bash
pip install flask joblib scikit-learn pandas
