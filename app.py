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
    max_value=4.5,
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
z = np.linspace(0, 4.5, 500)
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
    label=r"$e^{-\xi^2/2}$"
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
    f"z = {a:.2f}",
    ha="center",
    fontsize=11
)

# --------------------------------------------------
# Plot formatting
# --------------------------------------------------
ax.set_xlabel(r"${\xi}$", fontsize=13)
ax.set_ylabel(r"$e^{-\xi^2/2}$", fontsize=13)

ax.set_xlim(0, 4.5)
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
    rf"P(0 \leq \xi \leq {a:.2f}) = {result:.6f}"
)


st.markdown(
    """
    <div style="text-align: center; font-size: 11px; color: gray; margin-top: 40px;">
        Developed by Masoud Daneshi
    </div>
    """,
    unsafe_allow_html=True
)



# ==================================================
# INVERSE STANDARD NORMAL INTEGRAL CALCULATOR
# ==================================================

st.divider()

st.header("Inverse Standard Normal Integral Calculator")

st.markdown(
    "Enter the value of the integral to calculate the corresponding value of **z**."
)

st.latex(
    r"P=\frac{1}{\sqrt{2\pi}}"
    r"\int_0^z e^{-t^2/2}\,dt"
)

# --------------------------------------------------
# Input target integral value
# --------------------------------------------------
P_target = st.number_input(
    "Enter the integral value P:",
    min_value=0.0,
    max_value=0.499999,
    value=0.341345,
    step=0.001,
    format="%.6f"
)

# --------------------------------------------------
# Standard normal integral
# --------------------------------------------------
def normal_integral(z):
    integral, _ = quad(
        lambda t: np.exp(-t**2 / 2),
        0,
        z
    )

    return integral / np.sqrt(2 * np.pi)


# --------------------------------------------------
# Function whose root we want to find
#
# F(z) = Integral(z) - P_target
# --------------------------------------------------
def F(z, target):
    return normal_integral(z) - target


# --------------------------------------------------
# Bisection method
# --------------------------------------------------
def find_z_bisection(target, tolerance=1e-8):

    z_low = 0.0
    z_high = 5.0

    # Continue until the interval is sufficiently small
    while (z_high - z_low) > tolerance:

        # Midpoint
        z_mid = (z_low + z_high) / 2

        # Evaluate F at midpoint
        F_mid = F(z_mid, target)

        # F(z_low) is negative.
        # If F_mid is negative, root is to the right.
        if F_mid < 0:
            z_low = z_mid

        # If F_mid is positive, root is to the left.
        else:
            z_high = z_mid

    # Best estimate of the root
    return (z_low + z_high) / 2


# --------------------------------------------------
# Calculate z
# --------------------------------------------------
z_result = find_z_bisection(P_target)


# --------------------------------------------------
# Display result
# --------------------------------------------------
st.subheader("Result")

st.latex(
    rf"P(0 \leq Z \leq z) = {P_target:.6f}"
)

st.latex(
    rf"z = {z_result:.4f}"
)
