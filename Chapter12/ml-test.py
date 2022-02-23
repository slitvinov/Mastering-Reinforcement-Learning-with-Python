from copy import deepcopy
from gym.envs.classic_control.pendulum import PendulumEnv
from penenv3 import PenEnv
from ray import tune
from ray.rllib.agents.maml.maml import MAMLTrainer, DEFAULT_CONFIG
import gym
import numpy as np
import ray

config = deepcopy(DEFAULT_CONFIG)


ray.init()
tune.run(
    "MAML",
    stop={"training_iteration": 500},
    config=dict(
        DEFAULT_CONFIG,
        **{
            "env": PenEnv,
            "horizon": 200,
            "rollout_fragment_length": 200,
            "num_envs_per_worker": 10,
            "inner_adaptation_steps": 1,
            "maml_optimizer_steps": 5,
            "gamma": 0.99,
            "lambda": 1.0,
            "lr": 0.001,
            "vf_loss_coeff": 0.5,
            "clip_param": 0.3,
            "kl_target": 0.01,
            "kl_coeff": 0.001,
            "num_workers": 60,
            "num_gpus": 1,
            "inner_lr": 0.03,
            "explore": True,
            "clip_actions": False,
            "model": {"fcnet_hiddens": [64, 64],
                      "free_log_std": True
                      },
            "use_meta_env": True,
        }
    ),
    checkpoint_freq=10,
)
