---
title:          "Central Path Proximal Policy Optimization"
date:           2025-05-29 00:01:00 +0800
selected:       true
pub:            "The Exploration in AI Today Workshop at ICML 2025"
# pub_pre:        "Submitted to "
# pub_post:       'Under review.'
# pub_last:       ' <span class="badge badge-pill badge-publication badge-success">Spotlight</span>'
pub_date:       "2025"

abstract: >-
  In constrained Markov decision processes, enforcing constraints during training is often thought of as decreasing the final return. Recently, it was shown that constraints can be incorporated directly in the policy geometry, yielding an optimization trajectory close to the central path of a barrier method, which does not compromise final return. Building on this idea, we introduce Central Path Proximal Policy Optimization (C3PO), a simple modification of PPO that produces policy iterates, which stay close to the central path of the constrained optimization problem. Compared to existing on-policy methods, C3PO delivers improved performance with tighter constraint enforcement, suggesting that central path-guided updates offer a promising direction for constrained policy optimization.
cover:          /assets/images/covers/c3po_idea.jpg
authors:
  - Nikola Milosevic
  - Johannes Müller
  - Nico Scherf
links:
  Code: https://github.com/milosen/c3po
  Preprint: https://arxiv.org/abs/2506.00700
  OpenReview: https://openreview.net/forum?id=2cvUHCgZbF
  #Unsplash: https://unsplash.com/photos/sliced-in-half-pineapple--_PLJZmHZzk
---
