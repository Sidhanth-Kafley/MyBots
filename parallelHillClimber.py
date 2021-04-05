from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:

    def __init__(self):

        self.parents = {}
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION()

    def Evolve(self):

        for x in range(0, c.populationSize):
            self.parents[x].Evaluate("GUI")

        # self.parent.Evaluate("GUI")
        #
        # for currentGeneration in range(c.numberOfGenerations):
        #
        #     self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):

        self.Spawn()

        self.Mutate()

        self.child.Evaluate("DIRECT")

        self.Print()

        self.Select()

    def Spawn(self):

        self.child = copy.deepcopy(self.parent)

    def Mutate(self):

        self.child.Mutate()

    def Select(self):

        if(self.parent.fitness > self.child.fitness):

            self.parent = self.child

    def Print(self):

        print("\n\n", self.parent.fitness, self.child.fitness, "\n\n")

    def Show_Best(self):

        # self.parent.Evaluate("GUI")
        pass
