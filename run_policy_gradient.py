from causal_discovery.environment import Cartpole
from rl_algorithms.policy_gradient import PolicyGradient

if __name__ == '__main__':
    env = Cartpole()
    agent = PolicyGradient(env)
    # Run a short training for quick smoke-test
    transitions, rewards = agent.train(episodes=10, timestep=1, reward_threshold=1e9)
    print('Collected transitions shape:', transitions.shape)
    print('Collected rewards shape:', rewards.shape)
    print('Last 5 rewards:', rewards[-5:])
