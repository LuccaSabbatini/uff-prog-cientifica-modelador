"""
Leapfrog method for solving the wave equation.
"""
import json
import numpy as np
import matplotlib.pyplot as plt


def main():
    """
    Main function of the program.
    """
    with open(file="../inputs/leapfrog.json", mode="r", encoding="utf-8") as file:
        model = json.load(file)

    spring_constant = 210000000000
    particles_mass = 7850
    particles_radius = 1
    contacts = model["connect"]
    restrictions = model["boundary_values"]

    x = [coord[0] for coord in model["coords"]]
    y = [coord[1] for coord in model["coords"]]
    f = np.array(list(model["initial_values"]))

    num_particles = len(model["coords"])

    f = f.reshape(2 * num_particles)
    fi = np.zeros(2 * num_particles)
    v = np.zeros(2 * num_particles)
    u = np.zeros(2 * num_particles)
    a = (1 / particles_mass) * f

    n = 100
    h = 0.00004
    d_test = np.zeros(n)

    for i in range(n):
        v += a + h / 2
        u += v * h
        # Contato
        for j in range(num_particles):
            if restrictions[j][0] == 1:
                u[2 * j] = 0

            if restrictions[j][1] == 1:
                u[2 * j + 1] = 0

            num_particle_contacts = contacts[j][0]
            xj = x[j] + u[2 * j]
            yj = y[j] + u[2 * j + 1]

            for k in range(num_particle_contacts - 1):
                k_particle = contacts[j][k + 1]
                xk = x[k_particle] + u[2 * k_particle]
                yk = y[k_particle] + u[2 * k_particle + 1]
                dx = xj - xk
                dy = yj - yk
                d_particles = np.sqrt((float(dx) ** 2) + (float(dy) ** 2))
                d_force = d_particles - (2 * particles_radius)
                dx = d_force * dx / d_particles
                dy = d_force * dy / d_particles
                fi[2 * j] += spring_constant * dx
                fi[2 * j + 1] += spring_constant * dy

        a = (1 / particles_mass) * (f - fi)
        v += a * h / 2
        fi *= 0
        d_test[i] = u[17 * 2]

    plt.plot(d_test)
    plt.show()


if __name__ == "__main__":
    main()
