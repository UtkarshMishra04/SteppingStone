from mocca_envs.walker3d_envs import Walker3DStepperEnv

env = Walker3DStepperEnv(render=True)

env.reset()
env.create_terrain()