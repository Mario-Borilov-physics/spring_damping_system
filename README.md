## Description
The project simulates mechanical spring-object system on which acts a damping force which is directly proportional to the velocity of the object.
The displacement x and the velocity v_x are presented as functions of time and they are plotted as graphs using matplotlib.pyplot. The x and v_x as functons of t are found by numerical solving of the differential equations from the Newton's second law
The graphs are animated via FuncAnimation from matplotlib.animation
## Features
-physics-based simulation

- calculation are done using NumPy

- the numerical solving of the differencial equations is done by scipy.integrate using odeint solver

- the graphs are plotted and animated with matplotlib.pyplot and matplotlib.animation

## How to run
```bash
pip install matplotlib numpy scipy
python spring_damped_system.py
