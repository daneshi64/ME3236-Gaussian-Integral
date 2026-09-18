import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# --------------------------------------------------
# Page setup
# --------------------------------------------------
st.set_page_config(
    page_title="Standard Normal Integral Calculator",
    layout="centered"
)

st.title("Standard Normal Integral Calculator")

st.latex(
    r"\mathrm{P}(0 \leq \xi \leq z)=\frac{1}{\sqrt{2\pi}}"
    r"\int_0^z e^{-\xi^2/2}\,d\xi"
)

# --------------------------------------------------
# Input
# --------------------------------------------------
a = st.number_input(
    "Enter the value of z:",
    min_value=0.0,
    max_value=4.0,
    value=1.0,
    step=0.01,
    format="%.2f"
)

# --------------------------------------------------
# Calculate erf(a)
# --------------------------------------------------
integral, error = quad(
    lambda z: np.exp(-z**2 / 2),
    0,
    a
)

result = integral / np.sqrt(2 * np.pi)

# --------------------------------------------------
# Generate curve exp(-z^2/2)
# --------------------------------------------------
z = np.linspace(0, 4, 500)
y = np.exp(-z**2 / 2)

# Value of curve at z = a
y_a = np.exp(-a**2 / 2)

# --------------------------------------------------
# Plot
# --------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))

# Plot the integrand
ax.plot(
    z,
    y,
    linewidth=2.5,
    label=r"$e^{-z^2/2}$"
)

# Vertical line from y = 0 to the intersection
ax.vlines(
    x=a,
    ymin=0,
    ymax=y_a*1.1,
    linestyle="--",
    linewidth=2
)

# Mark intersection
ax.plot(
    a,
    y_a,
    "o",
    markersize=7
)

# Label a
ax.text(
    a,
    -0.07,
    f"a = {a:.2f}",
    ha="center",
    fontsize=11
)

# --------------------------------------------------
# Plot formatting
# --------------------------------------------------
ax.set_xlabel("a", fontsize=13)
ax.set_ylabel(r"$e^{-\xi^2/2}$", fontsize=13)

ax.set_xlim(0, 4)
ax.set_ylim(0, 1.05)

# Keep ticks but hide numerical tick labels
ax.tick_params(
    axis="both",
    which="both",
    labelbottom=False,
    labelleft=False
)

ax.grid(alpha=0.2)
ax.legend(fontsize=12)

plt.tight_layout()

st.pyplot(fig)

# --------------------------------------------------
# Display result
# --------------------------------------------------
st.subheader("Result")

st.latex(
    rf"P(0 \leq a \leq {a:.2f}) = {result:.5f}"
)


st.markdown(
    """
    <div style="text-align: center; font-size: 11px; color: gray; margin-top: 40px;">
        Developed by Masoud Daneshi
    </div>
    """,
    unsafe_allow_html=True
)
