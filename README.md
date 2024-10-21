# Grid2Op Reinforcement Learning Project

This project explores the implementation of reinforcement learning algorithms, specifically the Soft Actor-Critic (SAC) and Proximal Policy Optimization (PPO), within the Grid2Op environment. The primary focus is on optimizing the flow of power in the l2rpn_case14_sandbox grid while adhering to the N-1 reliability criterion.

# Table of Contents

Authors

Installation

Dependencies

Usage

Project Structure

Results

Evaluation

License

# Authors
Thapelo Mafabatho Harvey (1744565)

Rita Jmanagile (2094913)

# Installation
To run this project, clone the repository and install the required dependencies using pip.

```bash
git clone https://github.com/ThapeloGithub/Grid2Op-Reinforcement-Learning-Project
cd Grid2Op-Reinforcement-Learning-Project
pip install -r requirements.txt
```

# Dependencies
The following packages are required to run this project:

torch

torchvision

numpy

gymnasium

grid2op

matplotlib

stable-baselines3
# Usage 
The code is designed to be run in a Google Colab notebook. Make sure to upload the necessary scripts and data files to your Colab environment before executing the code.
# Project structure
ThapeloGithub/Grid2Op-Reinforcement-Learning-Project

# Project Directory Structure

```plaintext
SAC&PPO
├── plots
└── files
    ├── sac&ppo.ipynb
    ├── env.py
    └── run_sac_ppo.py
└── requirements.txt  # List of required Python packages
```
## Running the SAC & PPO Script

To run the `sac&ppo.ipynb` notebook programmatically, you can use the following command:

```bash
python files/run_sac_ppo.py
```

# Evaluation
The performance of the agents will be evaluated based on the Combined Reward, which aims to maximize the flow of power through the grid while ensuring the N-1 reliability criterion is met.
# License
This project is available for public use. Feel free to use, modify, and distribute it.
