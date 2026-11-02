# 3D Solar System Orbit Visualization

A Python project using Matplotlib and NumPy to render an interactive 3D representation of the 8 major planetary orbits in our Solar System scaled in Astronomical Units ($\text{AU}$).

## 📌 Features

* **3D Spatial Plotting:** Interactive 3D visualization using Matplotlib's `mplot3d` toolkit.

* **Scale Accuracy:** Orbital radii are scaled based on real semi-major axis values in Astronomical Units ($\text{AU}$).

* **Dark Sky Theme:** Styled with `dark_background` for astronomical presentation.

* **Complete Planetary System:** Includes all 8 major planets from Mercury to Neptune.

## 📐 Mathematical Model

The orbital paths are calculated using 2D parametric circle equations embedded in a 3D coplanar space ($z = 0$):

$$
x(\theta) = a \cdot \cos(\theta)
$$

$$
y(\theta) = a \cdot \sin(\theta)
$$

$$
z(\theta) = 0
$$

Where:

* $a$ = Semi-major axis of the planet's orbit in Astronomical Units ($\text{AU}$)

* $\theta \in [0, 2\pi]$ = Angular progression array (100 evaluation points)

* $1 \text{ AU} \approx 149,597,870.7 \text{ km}$ (Earth-Sun average distance)

## 🪐 Included Planetary Data

| Planet | Semi-Major Axis ($a$ in $\text{AU}$) | Orbital Period ($T$ in Years) |
| :--- | :--- | :--- |
| **Mercury** | $0.39 \text{ AU}$ | $0.24 \text{ years}$ |
| **Venus** | $0.72 \text{ AU}$ | $0.62 \text{ years}$ |
| **Earth** | $1.00 \text{ AU}$ | $1.00 \text{ years}$ |
| **Mars** | $1.52 \text{ AU}$ | $1.88 \text{ years}$ |
| **Jupiter** | $5.20 \text{ AU}$ | $11.86 \text{ years}$ |
| **Saturn** | $9.58 \text{ AU}$ | $29.46 \text{ years}$ |
| **Uranus** | $19.22 \text{ AU}$ | $84.01 \text{ years}$ |
| **Neptune** | $30.05 \text{ AU}$ | $164.80 \text{ years}$ |

## 🛠️ Prerequisites & Installation

Ensure you have Python 3.8+ installed along with `numpy` and `matplotlib`:

```bash
pip install numpy matplotlib
```

## 🚀 How to Run

1. Navigate to the project directory:

   ```bash
   cd Solar_System_3D
   ```

2. Execute the script:

   ```bash
   python solar_system_visualization.py
   ```

## 📊 Output

Running the script opens an interactive Matplotlib 3D figure where you can rotate, pan, and zoom to explore the relative orbital spacing of inner and outer planets.