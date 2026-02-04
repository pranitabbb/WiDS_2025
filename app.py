import streamlit as st
import json

st.title("Federated Learning Training Monitor")

st.markdown("""
This dashboard visualizes **global model performance** across federated rounds
for the PlantVillage dataset.
""")

# Load metrics
with open("week4_round_accuracy.json", "r") as f:
    acc = json.load(f)

rounds = list(map(int, acc.keys()))
values = list(acc.values())

# Create dataframe-like structure
chart_data = {
    "Federated Round": rounds,
    "Global Accuracy": values
}

# Plot using Streamlit (NO matplotlib)
st.line_chart(chart_data, x="Federated Round", y="Global Accuracy")

st.markdown("### Final Result")
st.write(f"Final Global Accuracy: **{values[-1]*100:.2f}%**")

st.markdown("""
**Observation**
- Accuracy improves rapidly in early rounds
- Stabilizes after convergence
- Demonstrates effective federated aggregation
""")
