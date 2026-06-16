from fipy import *
import matplotlib.pyplot as plt

# -------------------------
# Domain
# -------------------------
L = 1.0
nx = 50
dx = L / nx

# -------------------------
# Mesh
# -------------------------
mesh = Grid1D(nx=nx, dx=dx)

# -------------------------
# Temperature Variable
# -------------------------
T = CellVariable(
    name="Temperature",
    mesh=mesh,
    value=0.
)

# -------------------------
# Boundary Conditions
# -------------------------
T.constrain(100., mesh.facesLeft)
T.constrain(0., mesh.facesRight)

# -------------------------
# Heat Equation
# -------------------------
eq = DiffusionTerm()

# Solve
eq.solve(var=T)

# -------------------------
# Plot
# -------------------------
x = mesh.cellCenters[0]

plt.figure(figsize=(8,5))
plt.plot(x, T.value,
         linewidth=3,
         label="Numerical Solution")

plt.xlabel("Length")
plt.ylabel("Temperature (°C)")
plt.title("Case 1: 1D Steady-State Heat Conduction")
plt.grid(True)
plt.legend()

plt.show()

# Print values
print(T.value)
