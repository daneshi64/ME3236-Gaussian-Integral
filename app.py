import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# --------------------------------------------------
# Page setup
# --------------------------------------------------
st.set_page_config(
    page_title="Gaussian Integral Calculator",
    layout="centered"
)

st.title("Gaussian Integral Calculator")

st.latex(r"I(a)=\int_0^a e^{-z^2}\,dz")

# --------------------------------------------------
# Input
# --------------------------------------------------
a = st.number_input(
    "Enter the value of a:",
    min_value=0.0,
    max_value=4.0,
    value=1.0,
    step=0.1,
    format="%.2f"
)

# --------------------------------------------------
# Calculate integral
# --------------------------------------------------
result, error = quad(lambda z: np.exp(-z**2), 0, a)

# --------------------------------------------------
# Gaussian curve
# --------------------------------------------------
z = np.linspace(0, 4, 500)
y = np.exp(-z**2)

fig, ax = plt.subplots(figsize=(8, 5))

# Gaussian curve
ax.plot(
    z,
    y,
    linewidth=2.5,
    label=r"$e^{-z^2}$"
)


# Mark the intersection with the curve
y_a = np.exp(-a**2)

ax.plot(
    a,
    y_a,
    "o",
    markersize=7
)

# Vertical line at a
ax.axvline(
    x=a,
    ymin=0,
    ymax=y_a*1.1,
    linestyle="--",
    linewidth=2
)
# Label a
ax.text(
    a+0.3,
    y_a,
    f"a = {a:.2f}",
    ha="center",
    fontsize=11
)

# --------------------------------------------------
# Plot formatting
# --------------------------------------------------
ax.set_xlabel("z", fontsize=13)
ax.set_ylabel(r"$e^{-z^2}$", fontsize=13)

ax.set_xlim(0, 4)
ax.set_ylim(0, 1.05)

ax.grid(alpha=0.2)
ax.legend(fontsize=12)

plt.tight_layout()

st.pyplot(fig)

# --------------------------------------------------
# Result
# --------------------------------------------------
st.subheader("Result")

st.latex(
    rf"\int_0^{{{a:.3f}}} e^{{-z^2}}\,dz"
    rf" = {result:.6f}"
)
