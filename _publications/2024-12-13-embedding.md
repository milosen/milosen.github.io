---
title: "Embedding Safety into RL: A New Take on Trust Region Methods"
collection: publications
permalink: /publication/2024-12-13-embedding
excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
date: 2024-12-13
venue: 'arxiv'
#slidesurl: 'http://academicpages.github.io/files/slides1.pdf'
paperurl: 'https://arxiv.org/abs/2411.02957'
citation: 'Milosevic, Nikola, Johannes Müller, and Nico Scherf. "Embedding Safety into RL: A New Take on Trust Region Methods." arXiv preprint arXiv:2411.02957 (2024).'
---

Reinforcement Learning (RL) agents are able to solve a wide variety of tasks but are prone to producing unsafe behaviors. Constrained Markov Decision Processes (CMDPs) provide a popular framework for incorporating safety constraints. However, common solution methods often compromise reward maximization by being overly conservative or allow unsafe behavior during training. We propose Constrained Trust Region Policy Optimization (C-TRPO), a novel approach that modifies the geometry of the policy space based on the safety constraints and yields trust regions composed exclusively of safe policies, ensuring constraint satisfaction throughout training. We theoretically study the convergence and update properties of C-TRPO and highlight connections to TRPO, Natural Policy Gradient (NPG), and Constrained Policy Optimization (CPO). Finally, we demonstrate experimentally that C-TRPO significantly reduces constraint violations while achieving competitive reward maximization compared to state-of-the-art CMDP algorithms.