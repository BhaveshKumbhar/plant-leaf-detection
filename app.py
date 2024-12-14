import streamlit as st
import requests

# Page Configurations
st.set_page_config(
    page_title="Plant Leaf Health Detection",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Webpage Header
st.markdown(
    """
    <style>
        .title {
            font-size: 50px;
            font-weight: bold;
            text-align: center;
            color: #2E8B57;
        }
        .subtitle {
            font-size: 20px;
            text-align: center;
            color: #555;
        }
    </style>
    <div class="title">Plant Leaf Health Detection</div>
    <div class="subtitle">Upload an image of a plant leaf to analyze its health</div>
    """,
    unsafe_allow_html=True,
)

st.write("")

# Image Upload Widget
uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

# Upload Button
if st.button("Analyze"):
    if uploaded_file is not None:
        # Display uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Send the image to the REST API
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://127.0.0.1:5001/predict", files={"file": uploaded_file})

        if response.status_code == 200:
            # Display prediction result
            result = response.json().get("result")
            st.success(f"Prediction: {result}")
        else:
            st.error("Error: Unable to process the image.")
    else:
        st.error("Please upload an image first.")
