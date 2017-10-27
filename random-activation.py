from osim.env import RunEnv

env = RunEnv(visualize=True)
observation = env.reset(difficulty = 0)
for i in range(200):
    observation, reward, done, info = env.step(env.action_space.sample())
