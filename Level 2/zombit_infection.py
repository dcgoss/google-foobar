"""
Zombit infection
(Level 2, Problem 1)
================

Dr. Boolean continues to perform diabolical studies on your fellow rabbit kin, and not all of it is taking place in
the lab. Reports say the mad doctor has his eye on infecting a rabbit in a local village with a virus that transforms
rabbits into zombits (zombie-rabbits)!

Professor Boolean is confident in the virus's ability to spread, and he will only infect a single rabbit.
Unfortunately, you and your fellow resistance agents have no idea which rabbit will be targeted. You've been asked to
predict how the infection would spread if uncontained, so you decide to create a simulation experiment. In this
simulation, the rabbit that Dr. Boolean will initially infect will be called "Patient Z".

So far, the lab experts have discovered that all rabbits contain a property they call "Resistance", which is capable
of fighting against the infection. The virus has a particular "Strength" which Dr. Boolean needs to make at least as
large as the rabbits' Resistance for it to infect them.

You will be provided with the following information:
population = A 2D non-empty array of positive integers. (The dimensions of the array are not necessarily equal.) Each
cell represents one rabbit, and the value of the cell represents that rabbit's Resistance. All cells contain a rabbit.
x = The X-Coordinate (column) of "Patient Z" in the population array.
y = The Y-Coordinate (row) of "Patient Z" in the population array.
strength = A constant integer value representing the Strength of the virus.

Here are the rules of the simulation: First, the virus will attempt to infect Patient Z. Patient Z will only be
infected if the infection's Strength equals or exceeds Patient Z's Resistance. From then on, any infected rabbits
will attempt to infect any uninfected neighbors (cells that are directly - not diagonally - adjacent in the array).
They will succeed in infecting any neighbors with a Resistance lower than or equal to the infection's Strength. This
will continue until no further infections are possible (i.e., every uninfected rabbit adjacent to an infected rabbit
has a Resistance greater than the infection's Strength.)

You will write a function answer(population, x, y, strength), which outputs a copy of the input array representing
the state of the population at the end of the simulation, in which any infected cells value has been replaced with -1.
The Strength and Resistance values will be between 0 and 10000. The population grid will be at least 2x2 and no
larger than 50x50. The x and y values will be valid indices in the population arrays, with numbering beginning from 0.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) population = [[1, 2, 3], [2, 3, 4], [3, 2, 1]]
    (int) x = 0
    (int) y = 0
    (int) strength = 2
Output:
    (int) [[-1, -1, 3], [-1, 3, 4], [3, 2, 1]]

Inputs:
    (int) population = [[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]]
    (int) x = 2
    (int) y = 1
    (int) strength = 5
Output:
    (int) [[6, 7, -1, 7, 6], [6, -1, -1, -1, 7], [-1, -1, -1, -1, 10], [8, -1, -1, -1, 9], [8, 7, -1, 9, 9]]
"""

class InfectionSimulation:
    def __init__(self, population, x, y, virus_strength):
        self.virus_strength = virus_strength
        self.population = population
        self.starting_rabbit = [x, y]
        self.vulnerable_cells = []
        # add starting rabbit to begin
        self.vulnerable_cells.append(self.starting_rabbit)

    def run_simulation(self):
        while True:
            self.process_vulnerable_cells()
            if not self.vulnerable_cells:
                return self.population
            self.vulnerable_cells.extend(self.find_vulnerable_cells())

    def find_vulnerable_cells(self):
        """
        :return: array of coordinates of adjacent cells
        """

        """
        array to hold arrays containing [x, y] coordinates of adjacent cells
        ex.
        [
            [1, 3]
            [1, 5]
            etc.
        ]
        """
        adjacent_cells = []

        for cell in self.vulnerable_cells:
            x = cell[0]
            y = cell[1]

            if x != 0:
                """
                target is not the first cell in row.
                we can add the cell to the left:
                * 0 O
                """
                adjacent_cells.append(tuple((x - 1, y)))
            if x != len(self.population[y]) - 1:
                """
                target is not the last cell in row.
                we can add the cell to the right:
                O 0 *
                """
                adjacent_cells.append(tuple((x + 1, y)))

            if y != 0:
                """
                target (0) is not in the first row.
                we can add the above cell:
                O O *
                O O 0
                """
                adjacent_cells.append(tuple((x, y - 1)))
            if y != len(self.population) - 1:
                """
                target (0) is not in the last row.
                we can add the below cell:
                O O 0
                O O *
                """
                adjacent_cells.append(tuple((x, y + 1)))

        return list(set(adjacent_cells))

    def process_vulnerable_cells(self):
        cell_indexes_to_delete = []
        for index, cell in enumerate(self.vulnerable_cells):
            x = cell[0]
            y = cell[1]
            if not self.virus_does_infect_rabbit_with_resistance(self.get_rabbit_resistance(x, y)):
                cell_indexes_to_delete.insert(0, index)
            else:
                self.infect_rabbit(x, y)
        for index in cell_indexes_to_delete:
            del self.vulnerable_cells[index]

    def infect_rabbit(self, x, y):
        self.population[y][x] = -1

    def get_rabbit_resistance(self, x, y):
        return self.population[y][x]

    def virus_does_infect_rabbit_with_resistance(self, rabbit_resistance):
        return rabbit_resistance <= self.virus_strength and rabbit_resistance != -1

def answer(population, x, y, strength):
    simulation = InfectionSimulation(population, x, y, strength)
    return simulation.run_simulation()

