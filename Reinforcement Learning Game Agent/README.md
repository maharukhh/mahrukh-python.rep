# Reinforcement Learning Game Agent

A tabular Q-learning agent that learns, purely through trial and error, to navigate a grid world from a start cell to a goal cell while avoiding traps — with no hardcoded path or rules telling it what to do.

## How It Works

1. **Environment** — A small grid world with a fixed start cell, a goal cell, and several trap cells. Moving onto a trap ends the episode with a large penalty; reaching the goal ends it with a large reward; every other move gets a small penalty (to encourage short paths).
2. **Q-table** — The agent keeps a table of estimated values (Q-values) for every `(state, action)` pair — essentially "how good is it to take this action from this cell?"
3. **Training loop** — Over thousands of simulated episodes, the agent:
   - Picks actions using an epsilon-greedy strategy (mostly random early on, increasingly choosing its best-known action as training progresses — the classic explore-vs-exploit tradeoff).
   - Updates its Q-table after every move using the Q-learning update rule, based on the reward received and the best value available from the next state.
4. **Replay** — After training completes (all in the terminal, instantly), a Pygame window opens and replays the agent's final learned (greedy) policy step by step, so you can watch the path it discovered on its own.

## Requirements

- Python 3.x
- Pygame (`pip install pygame`)

## Usage

```bash
pip install pygame
python rl_game_agent.py
```

Training happens automatically and instantly when you run the script (progress prints to the terminal). Once training finishes, the Pygame window opens showing the agent's learned route.

**Controls (in the replay window):**
| Action | Effect |
|---|---|
| `SPACE` | Replay another episode using the current learned policy |
| `T` | Retrain the agent from scratch (new random exploration run) |
| `ESC` | Quit |

## Notes & Limitations

- Because training uses randomness (epsilon-greedy exploration), the exact path learned can vary slightly between runs — pressing `T` to retrain may produce a different (but still valid) route.
- This is tabular Q-learning, which only scales to small, discrete state spaces — it stores one value per `(cell, action)` pair rather than using a neural network, which keeps it simple and fully interpretable but wouldn't scale to a much larger or continuous environment.
- Grid size, trap locations, and hyperparameters (`ALPHA`, `GAMMA`, `EPISODES`) are configurable constants at the top of the file.

## Possible Extensions

- Plot the learning curve (total reward per episode) to visualize training progress over time.
- Add a live-training visualization mode instead of training silently before showing the replay.
- Swap in Deep Q-Learning to scale up to a larger or continuous state space.
