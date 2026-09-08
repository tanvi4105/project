# import streamlit as st
# import joblib
# import re

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(
#     page_title="Emotion Detection",
#     page_icon="🎭",
#     layout="centered"
# )

# # ---------------- LOAD MODELS ----------------
# model = joblib.load("svm_model.pkl")
# vectorizer = joblib.load("tfidf_vectorizer.pkl")
# label_encoder = joblib.load("label_encoder.pkl")

# # ---------------- SESSION STATE ----------------
# if "text_key" not in st.session_state:
#     st.session_state.text_key = 0

# # ---------------- TEXT CLEANING + NEGATION ----------------
# NEGATION_WORDS = ["not", "no", "never", "n't","nobody"]

# def clean_text(text):
#     text = text.lower()
#     text = re.sub(r"http\S+", "", text)
#     text = re.sub(r"@\w+|#\w+", "", text)
#     text = re.sub(r"[^a-z\s]", "", text)
#     text = re.sub(r"\s+", " ", text).strip()
#     return text

# def handle_negation(text):
#     words = text.split()
#     result = []
#     negate = False
    
#     for word in words:
#         if word in NEGATION_WORDS:
#             negate = True
#             continue
        
#         if negate:
#             result.append("not_" + word)
#             negate = False
#         else:
#             result.append(word)
    
#     return " ".join(result)


# # ---------------- STYLING ----------------
# st.markdown("""
# <style>
# .stApp {
#     background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee);
# }
# .container {
#     background: rgba(255,255,255,0.95);
#     padding: 35px;
#     border-radius: 25px;
#     box-shadow: 0px 15px 40px rgba(0,0,0,0.25);
# }
# .title {
#     text-align: center;
#     font-size: 42px;
#     font-weight: bold;
# }
# .subtitle {
#     text-align: center;
#     font-size: 18px;
#     color: #444;
# }
# .emojis {
#     text-align: center;
#     font-size: 48px;
# }
# .result {
#     background: linear-gradient(135deg, #00f2fe, #4facfe);
#     color: white;
#     padding: 18px;
#     border-radius: 15px;
#     text-align: center;
#     font-size: 24px;
#     font-weight: bold;
#     margin-top: 20px;
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- UI ----------------
# st.markdown("<div class='emojis'>😊 😢 😡 😍 😱 😮 😌</div>", unsafe_allow_html=True)
# # st.markdown("<div class='container'>", unsafe_allow_html=True)

# st.markdown("<div class='title'>Emotion Detection System 🎭</div>", unsafe_allow_html=True)
# #st.markdown("<div class='subtitle'>Colorful UI • Negation Handling • ML Model</div>", unsafe_allow_html=True)

# # ---------------- TEXT AREA (KEY-BASED RESET) ----------------
# user_text = st.text_area(
#     "✍️ Enter your sentence",
#     height=120,
#     placeholder="Example: I am not happy today",
#     key=f"text_{st.session_state.text_key}"
# )

# # ---------------- BUTTONS ----------------
# col1, col2 = st.columns(2)
# with col1:
#     predict = st.button("🔍 Detect Emotion")
# with col2:
#     clear = st.button("🧹 Clear Text")

# # ---------------- CLEAR (SAFE RESET) ----------------
# if clear:
#     st.session_state.text_key += 1
#     st.rerun()

# # ---------------- PREDICTION ----------------

# if predict and user_text.strip():
#     try:
#         cleaned = clean_text(user_text)
#         final_text = handle_negation(cleaned)

#         # ✅ ADD VALIDATION HERE
#         if not final_text.strip():
#             st.warning("⚠️ Please enter valid text (not only numbers or symbols).")
#         else:
#             vector = vectorizer.transform([final_text])
#             pred_num = model.predict(vector)[0]
#             emotion = label_encoder.inverse_transform([pred_num])[0].upper()

#             emoji_map = {
#                 "HAPPINESS": "😊",
#                 "SADNESS": "😢",
#                 "ANGER": "😡",
#                 "LOVE": "😍",
#                 "FEAR": "😱",
#                 "SURPRISE": "😮",
#                 "NEUTRAL": "😐"
#             }

#             st.markdown(
#                 f"<div class='result'>{emoji_map.get(emotion,'😐')} DETECTED EMOTION: {emotion}</div>",
#                 unsafe_allow_html=True
#             )

#     except Exception as e:
#         st.error("⚠️ Error during prediction. Please try again.")

