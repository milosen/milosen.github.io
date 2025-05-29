---
title:          "Embedding Safety into RL: A New Take on Trust Region Methods"
date:           2025-05-29 00:01:00 +0800
selected:       true
pub:            "International Conference on Machine Learning (ICML)"
# pub_pre:        "Submitted to "
# pub_post:       'Under review.'
pub_last:       ' <span class="badge badge-pill badge-publication badge-success">Spotlight</span>'
pub_date:       "2025"

abstract: >-
  Reinforcement Learning (RL) agents can solve diverse tasks but often exhibit
  unsafe behavior. Constrained Markov Decision Processes (CMDPs) address this by
  enforcing safety constraints, yet existing methods either sacrifice reward
  maximization or allow unsafe training. We introduce Constrained Trust Region
  Policy Optimization (C-TRPO), which reshapes the policy space geometry to
  ensure trust regions contain only safe policies, guaranteeing constraint
  satisfaction throughout training. We analyze its theoretical properties and
  connections to TRPO, Natural Policy Gradient (NPG), and Constrained Policy
  Optimization (CPO). Experiments show that C-TRPO reduces constraint violations
  while maintaining competitive returns.
#cover:          /assets/images/covers/cover3.jpg
authors:
  - Nikola Milosevic
  - Johannes Müller
  - Nico Scherf
links:
  Code: https://github.com/milosen/ctrpo
  Preprint: https://arxiv.org/abs/2411.02957
  OpenReview: https://openreview.net/forum?id=4zRb89SbzG
  #Unsplash: https://unsplash.com/photos/sliced-in-half-pineapple--_PLJZmHZzk
---
