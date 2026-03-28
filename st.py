import streamlit as st
import joblib

# Load the pre-trained model
@st.cache_resource  # Cache the model for faster reloading
def load_model():
    return joblib.load("customer_model.pkl")  # Replace with the actual file path

model = load_model()

# Streamlit app title
st.title("Purchase Amount Predictor")

# Input fields
customer_id = st.text_input("Customer ID:")
age = st.number_input("Age:", min_value=0, max_value=120, step=1)
gender = st.radio("Gender:", ["Male", "Female"])
item_purchased = st.text_input("Item Purchased:")
review_rating = st.slider("Review Rating (1-5):", 1, 5)
subscription_status = st.radio("Subscription Status:", ["Yes", "No"])
discount_applied = st.radio("Discount Applied:", ["Yes", "No"])

# Prediction function
def predict_purchase_amount(customer_id, age, gender, item_purchased, review_rating, subscription_status, discount_applied):
    # Replace this with actual logic for your model
    # Prepare input features
    input_features = {
        "Customer ID": customer_id,
        "Age": age,
        "Gender": gender,
        "Item Purchased": item_purchased,
        "Review Rating": review_rating,
        "Subscription Status": subscription_status,
        "Discount Applied": discount_applied,
    }
    
    # Example: Predict using the loaded model (uncomment below if using a model)
    # predicted_amount = model.predict([list(input_features.values())])[0]
    
    # Placeholder for the predicted amount
    predicted_amount = 85.50  # Replace with your model's prediction
    return predicted_amount

# Add a Predict button
if st.button("Predict Purchase Amount"):
    if not customer_id or not item_purchased:
        st.error("Please fill in all required fields!")
    else:
        predicted_amount = predict_purchase_amount(
            customer_id, age, gender, item_purchased, review_rating, subscription_status, discount_applied
        )
        st.success(f"Predicted Purchase Amount (USD): ${predicted_amount:.2f}")
