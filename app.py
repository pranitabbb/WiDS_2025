import streamlit as st
import json
import matplotlib.pyplot as plt

# Title
st.title("Federated Learning Training Monitor")

st.markdown("""
This dashboard visualizes **global model performance** across federated rounds
for the PlantVillage dataset.
""")

# Load metrics
with open("week4_round_accuracy.json", "r") as f:
    accuracy_dict = json.load(f)

rounds = list(map(int, accuracy_dict.keys()))
accuracies = list(accuracy_dict.values())

# Plot
plt.figure(figsize=(8, 4))
plt.plot(rounds, accuracies, marker="o", linewidth=2)
plt.xlabel("Federated Round")
plt.ylabel("Global Test Accuracy")
plt.title("Global Accuracy vs Federated Rounds")
plt.grid(True)

st.pyplot(plt)

# Final summary
st.markdown("### Final Result")
st.write(f"Final Global Accuracy: **{accuracies[-1]*100:.2f}%**")

st.markdown("""
**Observation:**
- Accuracy improves rapidly in early rounds
- Stabilizes after convergence
- Demonstrates effective federated aggregation
""")
