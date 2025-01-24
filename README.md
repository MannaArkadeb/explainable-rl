# Explainable Reinforcement Learning Through Causality

A structural causal model (SCM) approach to explainable reinforcement learning.

This project extends previous work by Madumal et al. [1] to develop and implement a fully domain-agnostic explanation generation approach. By detecting the underlying causal relationships, and with our novel explanation generation algorithm, we ensure that this tool is generalisable to a range of RL environments.

## Structure
`main.py`: runs the whole SCM approach.

`rl_algorithms/`: contains the RL algorithms used in evaluation.

`causal_discovery/`: runs the different causal discovery methods investigated.

`structural_causal_model.py`: includes code for training and generating predictions from a structural causal model.

`generate_explanations.py`: includes code for generating why and counterfactual explanations.

`evaluation.py`: includes code for evaluating the accuracy of the trained structural causal models.

## Run
To run the approach on an individual RL environment:

```
python main.py --env <Environment> --rl <RL Algorithm>
```

To run on all the included environments:

```
./test_all_environments.sh
```


## RL Algorithms
Some of the RL algorithms presented in this codebase were adapted from the following sources:
| RL Algorithm | Source | License |
| --- | --- | --- |
| `SARSA` | [dennybritz/reinforcement-learning](https://github.com/dennybritz/reinforcement-learning) | MIT License |
| `Policy Gradient` | [bentrevett/pytorch-rl/tree/master](https://github.com/bentrevett/pytorch-rl/tree/master) | MIT License |

## References
[1] Madumal P, Miller T, Sonenberg L, Vetere F. (2020). Explainable reinforcement learning through a causal lens. Proceedings of the AAAI Conference on Artificial Intelligence, 34(3), 2493-2500.
