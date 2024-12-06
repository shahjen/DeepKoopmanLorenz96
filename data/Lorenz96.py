import numpy as np
from scipy.integrate import odeint
import pandas as pd
import matplotlib.pyplot as plt

def gen_trajs(initial, t_eval, F):
    num_trajs, N = initial.shape
    odefunc = lambda x, t : (np.roll(x, -1) - np.roll(x, 2)) * np.roll(x, 1) - x + F
    trajs = np.zeros((num_trajs, len(t_eval), N))
    for i in range(num_trajs):
        if i%100 == 0:
            print(i)
        trajs[i,:,:] = odeint(odefunc, initial[i,:], t_eval)
    return trajs

initial = np.random.randn(5000, 4)
t_eval = np.linspace(0,5,100)
F = 8

trajs = gen_trajs(initial, t_eval, F)

i = 0

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(trajs[i, :, 0], trajs[i, :, 1], trajs[i, :, 2])
plt.show()

print(trajs.shape)
trajs = trajs.reshape((trajs.shape[0]*trajs.shape[1], trajs.shape[2]))
print(trajs.shape)

trajs = pd.DataFrame(trajs)
# trajs.to_csv("data/Lorenz96_train1_x.csv", header=False, index=False)
trajs.to_csv("data/Lorenz96_val_x.csv", header=False, index=False)
