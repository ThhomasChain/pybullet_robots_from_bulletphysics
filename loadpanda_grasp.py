import pybullet as p
import pybullet_data as pd
import math
import time
import numpy as np
import panda_sim_grasp as panda_sim

p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_Y_AXIS_UP,1)
p.setAdditionalSearchPath(pd.getDataPath())

timeStep=1./240.
p.setTimeStep(timeStep)
p.setGravity(0,-9.8,0)
 
panda = panda_sim.PandaSim(p,[0,0,0])
while (1):
	panda.step()
	p.stepSimulation()
	time.sleep(timeStep)
	