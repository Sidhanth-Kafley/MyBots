import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:

    def __init__(self, jointName):

        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.motorValues = np.zeros(1000)
        n = np.linspace(-np.pi, np.pi, 1000)
        self.amplitude = c.amplitude_backLeg
        self.frequency = c.frequency_backLeg
        if self.jointName == "Torso_FrontLeg":
            self.frequency/=2
        self.offset = c.phaseOffset_backLeg
        for i in range(1000):
            self.motorValues[i] = np.sin(self.frequency * n[i] + self.offset) * self.amplitude


    def Set_Value(self, robot, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = desiredAngle,
        maxForce =30)

    def Save_Values(self):
        np.save('data/motorValues.npy', self.motorValues)
