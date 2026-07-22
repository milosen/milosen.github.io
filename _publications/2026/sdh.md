---
title:          "Stochastic Decision Horizons for Constrained Reinforcement Learning"
date:           2026-02-04 00:00:00 +0000
selected:       true
pub_pre:        "Preprint — "
pub:            "arXiv:2602.04599"
pub_date:       "2026"

abstract: >-
  We introduce a framework for constrained RL where constraint satisfaction is enforced
  at every step. A state-action continuation probability models constraint violations as
  effective horizon reductions. Building on Control as Inference, we develop two
  off-policy algorithms: max-entropy AS-SAC, which treats violations as absorbing states,
  and KL-regularized VT-MPO, which halts reward accumulation on violation. VT-MPO
  achieves competitive performance with 4× fewer environment steps on humanoid locomotion
  and identifies optimal reward–constraint tradeoff regimes in Safety Gymnasium.

authors:
  - Nikola Milosevic
  - Leonard Franz
  - Daniel Haeufle
  - Georg Martius
  - Nico Scherf
  - Pavel Kolev
links:
  Preprint: https://arxiv.org/abs/2602.04599
---
