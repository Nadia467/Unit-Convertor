import streamlit as st

# Step 2: Title aur heading set karo
st.title("🔁Unit Converter")
st.write("Welcome to unit convertor")

# Step 3: User se conversion type pocho
conversion_type = st.selectbox("What do you want to convert?", ["Length", "Weight"])

# Step 4: Value input lo
value = st.number_input("Enter value:", value=0.0)

# Step 5: Units define karo
if conversion_type == "Length":
    st.write("Units: Meters, Kilometers")
    
    from_unit = st.selectbox("From unit", ["Meters", "Kilometers"])
    to_unit = st.selectbox("To unit", ["Meters", "Kilometers"])

    # Step 6: Simple if-else se conversion logic
    if from_unit == "Meters" and to_unit == "Kilometers":
        result = value / 1000
    elif from_unit == "Kilometers" and to_unit == "Meters":
        result = value * 1000
    else:
        result = value  # Same units

elif conversion_type == "Weight":
    st.write("Units: Grams, Kilograms")

    from_unit = st.selectbox("From unit", ["Grams", "Kilograms"])
    to_unit = st.selectbox("To unit", ["Grams", "Kilograms"])

    if from_unit == "Grams" and to_unit == "Kilograms":
        result = value / 1000
    elif from_unit == "Kilograms" and to_unit == "Grams":
        result = value * 1000
    else:
        result = value  # Same units

# Step 7: Button dabao aur result dekho
if st.button("Convert"):
    st.success(f"Convert value is: {result} {to_unit}")
