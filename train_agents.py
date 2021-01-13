#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 16:03:09 2021

@author: tennismichel
"""
# import os
import numpy as np
import matplotlib.pyplot as plt
import gym
import torch

# from networks import NNetwork, NeuralNetworkPolicy
from agents import Q_Agent, Q_DQN_Agent, SARSA_Agent, SARSA_DQN_Agent
from agents_nnp import AAC_Agent, MC_PolGrad_Agent

#%% ENVIRONMENT
env = gym.make('Acrobot-v1')

#%% SEED
random_seed = 111 # 222 # 1234
np.random.seed(random_seed)
torch.manual_seed(random_seed)
env.seed(random_seed)

#%% TRAINING
training_results = list() # A list for storing the hyperparameters and the corresponding results
MAX_EPISODES = 1500
EPS = 0.2
DROPOUT = 0.6 # 0.6
LR_POL = 0.001
LR_QNET = 0.0001
GAMMA = 0.99
HIDDEN_DIM_POL = 256
HIDDEN_DIM_QNET = 16
LOG_INTERVAL = 100


# #%% Train AAC-Agent (neural network policy - agent) ###
# hyperparam_dict = {'name': 'AAC-Agent', 'learning_rate':LR_POL, 'gamma':GAMMA}

# aac_agent = AAC_Agent(env, num_episodes=MAX_EPISODES, num_steps=500, learning_rate=LR_POL,
#                       gamma=GAMMA, hidden_dim=HIDDEN_DIM_POL, dropout=DROPOUT, log_interval=LOG_INTERVAL)
# ep_rewards, running_rewards = aac_agent.train()
# training_results.append((hyperparam_dict, ep_rewards, running_rewards))


# #%% Train Monte Carlo policy gradient Agent (REINFORCE - Agent) ###
# hyperparam_dict = {'name': 'MC_PolGrad-Agent', 'learning_rate':LR_POL, 'gamma':GAMMA}
# mc_polGrad_agent = MC_PolGrad_Agent(env, num_episodes=MAX_EPISODES, num_steps=500, learning_rate=LR_POL,
#                       gamma=GAMMA, hidden_dim=HIDDEN_DIM_POL, dropout=DROPOUT, log_interval=LOG_INTERVAL)
# ep_rewards, running_rewards = mc_polGrad_agent.train()
# training_results.append((hyperparam_dict, ep_rewards, running_rewards))


# #%% Train Q_DQN-Agent (semi-gradient) ###
# # neurons=16 and epsilon=0.2
# hyperparam_dict = {'name': 'Q-DQN-Agent', 'learning_rate':LR_QNET, 'gamma':GAMMA, 'epsilon':EPS}
# q_dqn_agent = Q_DQN_Agent(env, num_episodes=MAX_EPISODES, num_steps=500, learning_rate=LR_QNET,
#                   gamma=GAMMA, epsilon=EPS, hidden_dim=HIDDEN_DIM_QNET, log_interval=LOG_INTERVAL)
# ep_rewards, running_rewards = q_dqn_agent.train()
# training_results.append((hyperparam_dict, ep_rewards, running_rewards))


# #%% Train SARSA_DQN-Agent (semi-gradient) ###
# # neurons=16 and epsilon=0.2
# hyperparam_dict = {'name': 'SARSA-DQN-Agent', 'learning_rate':LR_QNET, 'gamma':GAMMA, 'epsilon':EPS}
# sarsa_dqn_agent = SARSA_DQN_Agent(env, num_episodes=MAX_EPISODES, num_steps=500, learning_rate=LR_QNET,
#                   gamma=GAMMA, epsilon=EPS, hidden_dim=HIDDEN_DIM_QNET, log_interval=LOG_INTERVAL)
# ep_rewards, running_rewards = sarsa_dqn_agent.train()
# training_results.append((hyperparam_dict, ep_rewards, running_rewards))


# #%% Train Q-Agent (semi-gradient) ###
# hyperparam_dict = {'name': 'Q-Agent', 'learning_rate':LR_QNET, 'gamma':GAMMA, 'epsilon':EPS}
# q_agent = Q_Agent(env, num_episodes=MAX_EPISODES, num_steps=500, learning_rate=LR_QNET,
#                   gamma=GAMMA, epsilon=EPS, hidden_dim=HIDDEN_DIM_QNET, log_interval=LOG_INTERVAL)
# ep_rewards, running_rewards = q_agent.train()
# training_results.append((hyperparam_dict, ep_rewards, running_rewards))


#%% Train SARSA-Agent (semi-gradient) ###
hyperparam_dict = {'name': 'SARSA-Agent', 'learning_rate':LR_QNET, 'gamma':GAMMA, 'epsilon':EPS}
sarsa_agent = SARSA_Agent(env, num_episodes=MAX_EPISODES, num_steps=500, learning_rate=LR_QNET,
                  gamma=GAMMA, epsilon=0.99, hidden_dim=HIDDEN_DIM_QNET, log_interval=LOG_INTERVAL)
ep_rewards, running_rewards = sarsa_agent.train()
training_results.append((hyperparam_dict, ep_rewards, running_rewards))

#%% VISUALIZATION
plt.rcParams.update({'font.size': 18})

# Plot the results
fig = plt.figure(1, figsize=(20,8))

for result in training_results:
    hp = result[0]
    ep_rewards = result[1]
    running_rewards = result[2]
    # plt.plot(range(len(ep_rewards)), ep_rewards, lw=2, color="red", label=hp['name'])
    plt.plot(range(len(running_rewards)), running_rewards, lw=2, label=hp['name'])
    
    # title_str = hp['name'] + '($\gamma$:' + str(hp['gamma']) + ',lr:' + str(hp['learning_rate']) + ')'
    title_str = "Acrobot-v1 ($hiddenDim_{qnet}$: " + str(HIDDEN_DIM_QNET) + ", $hiddenDim_{pol}$: " + str(HIDDEN_DIM_POL) + ")"
    plt.title(title_str)

plt.grid()
plt.xlabel('Episodes')
plt.ylabel('Running average of Rewards')
plt.legend() # ncol=1
plt.show()
