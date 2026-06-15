from fipy import *
import matplotlib.pyplot as plt

mesh = Grid1D(nx=50, dx=1.)

phi = CellVariable(mesh=mesh, value=0.)

phi.constrain(100., mesh.facesLeft)
phi.constrain(0., mesh.facesRight)

eq = DiffusionTerm()

eq.solve(var=phi)

print(phi.value)

# Graph
x = mesh.cellCenters[0]

plt.plot(x, phi.value)
plt.xlabel("Length")
plt.ylabel("Temperature")
plt.title("1D Heat Conduction")
plt.grid(True)
plt.show()