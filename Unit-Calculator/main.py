import streamlit as st
from agent_with_tools.agent import graph
from langchain_core.messages import HumanMessage, AIMessage

# Conversion factors dictionary
CONVERSION_FACTORS = {
    'length': {
        'meters': 1.0,
        'kilometers': 1000.0,
        'miles': 1609.34,
        'feet': 0.3048,
        'inches': 0.0254
    },
    'mass': {
        'kilograms': 1.0,
        'pounds': 0.453592,
        'grams': 0.001,
        'ounces': 0.0283495
    },
    'volume': {
        'liters': 1.0,
        'gallons': 3.78541,
        'milliliters': 0.001,
        'cubic_meters': 1000.0,
        'cubic_feet': 28.3168
    },
    'area': {
        'square_meters': 1.0,
        'square_feet': 0.092903,
        'acres': 4046.86
    }
}

# Unit categories
UNIT_CATEGORIES = {
    'meters': 'length', 'kilometers': 'length', 'miles': 'length', 'feet': 'length', 'inches': 'length',
    'kilograms': 'mass', 'pounds': 'mass', 'grams': 'mass', 'ounces': 'mass',
    'liters': 'volume', 'gallons': 'volume', 'milliliters': 'volume', 'cubic_meters': 'volume', 'cubic_feet': 'volume',
    'square_meters': 'area', 'square_feet': 'area', 'acres': 'area'
}

def convert_units(value, from_unit, to_unit):
    # Special case for temperature conversion
    if from_unit in ['celsius', 'fahrenheit', 'kelvin'] and to_unit in ['celsius', 'fahrenheit', 'kelvin']:
        # Convert to Kelvin first
        if from_unit == 'celsius':
            kelvin = value + 273.15
        elif from_unit == 'fahrenheit':
            kelvin = (value - 32) * 5/9 + 273.15
        else:  # from Kelvin
            kelvin = value
        
        # Convert from Kelvin to target unit
        if to_unit == 'celsius':
            return kelvin - 273.15
        elif to_unit == 'fahrenheit':
            return (kelvin - 273.15) * 9/5 + 32
        else:  # to Kelvin
            return kelvin

    # For other units
    if from_unit not in UNIT_CATEGORIES or to_unit not in UNIT_CATEGORIES:
        raise ValueError("Unknown units")
    
    if UNIT_CATEGORIES[from_unit] != UNIT_CATEGORIES[to_unit]:
        raise ValueError("Incompatible units")
    
    category = UNIT_CATEGORIES[from_unit]
    # Convert to base unit first, then to target unit
    base_value = value * CONVERSION_FACTORS[category][from_unit]
    return base_value / CONVERSION_FACTORS[category][to_unit]

st.title("Unit Converter")

tab1, tab2 = st.tabs(["AI Chatbot", "Manual Calculator"])

with tab1:
    st.header("Chat with AI")
    st.write("Ask me anything about unit conversion!")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        if isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.write(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("assistant"):
                st.write(message.content)

    if prompt := st.chat_input("Example: Convert 10 kg to pounds"):
        st.session_state.messages.append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.write(prompt)
        
        result = graph.invoke({"messages": [HumanMessage(content=prompt)]})
        assistant_response = result["messages"][-1]
        
        st.session_state.messages.append(assistant_response)
        with st.chat_message("assistant"):
            st.write(assistant_response.content)

with tab2:
    st.header("Manual Calculator")
    
    category = st.selectbox(
        "Category",
        ["Length", "Mass", "Temperature", "Volume", "Area"]
    )
    
    if category.lower() == "temperature":
        available_units = ["celsius", "fahrenheit", "kelvin"]
    else:
        available_units = [unit for unit, cat in UNIT_CATEGORIES.items() 
                         if cat == category.lower()]
    
    col1, col2 = st.columns(2)
    
    with col1:
        input_value = st.number_input("Value", value=1.0)
        input_unit = st.selectbox("From", available_units)

    with col2:
        output_unit = st.selectbox("To", available_units)

    if st.button("Convert"):
        try:
            result = convert_units(input_value, input_unit, output_unit)
            st.success(f"{input_value} {input_unit} = {result:.4f} {output_unit}")
        except ValueError as e:
            st.error(str(e))
        except Exception:
            st.error("Error during conversion. Check your inputs.")

    with st.expander("Help"):
        st.write("• Select a category and units")
        st.write("• Enter a value to convert")
        st.write("• Click Convert to see the result")