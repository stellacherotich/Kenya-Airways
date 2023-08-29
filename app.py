import streamlit as st
import pickle

# Load the pre-trained sentiment analysis model
with open('sentiment_pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

def get_sentiment_type(sentiment_label):
    if sentiment_label == -1:
        return "Negative"
    elif sentiment_label == 0:
        return "Neutral"
    elif sentiment_label == 1:
        return "Positive"
    else:
        return "Unknown"

def main():
    st.set_page_config(page_title="Sky Opinion", page_icon="✈️")

    # Custom CSS style (using the provided CSS)
    st.markdown(
        """
        <style>
        body {
            background-color: #ffffff;
            color: #000000;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .stApp {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
            background-color: #FFFFFF;
        }
        .stButton button {
            background-color: #2E8B57;
            color: #FFFFFF;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        .stButton button:hover {
            background-color: #a7d1ba;
        }
        .stTextInput>div>div>input {
            border-radius: 11px;
            padding: 10px;
            font-size: 16px;
        }
        .stTextInput label {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .stTitle {
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .stSubheader {
            font-size: 24px;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Sky Opinion")
    st.subheader("Catching the Feelings from the Flights")

    # Input text for prediction
    input_text = st.text_area("Enter your review:", height=150)

    if st.button("Predict"):
        # Perform sentiment prediction using the loaded model
        sentiment_label = pipeline.predict([input_text])[0]
        confidence = pipeline.predict_proba([input_text]).max()

        # Get the sentiment type based on the sentiment label
        sentiment_type = get_sentiment_type(sentiment_label)

        # Display prediction result with improved styling
        st.subheader("Prediction Result")
        st.write("Sentiment Label:", sentiment_label)
        st.write("Sentiment Type:", sentiment_type)
        st.write("Confidence:", f"{confidence:.2f}")

if __name__ == "__main__":
    main()
