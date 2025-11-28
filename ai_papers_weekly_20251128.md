# 🤖 Top 5 AI Papers This Week
## Week of November 28, 2025

Welcome to this week's roundup of the most impactful AI research papers! These papers have been generating buzz across Reddit, academic Twitter, and research communities.

**📊 This Week's Stats:**
- 📄 **5 featured papers** from **1 categories**  
- 👥 **43 contributing authors**
- 🔥 **Average engagement score:** 25.0
- 🏆 **Highest scorer:** 25 points

---

## 1. ToolOrchestra: Elevating Intelligence via Efficient Model and Tool Orchestration

🧠 **Category:** CS.AI | 📅 **Published:** November 26, 2025 | 🔥 **Score:** 25 points

**Authors:** Hongjin Su, Shizhe Diao, Ximing Lu et al. (+13 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2511.21689v1) | [PDF Download](https://arxiv.org/pdf/2511.21689v1.pdf)

Large language models are powerful generalists, yet solving deep and complex problems such as those of the Humanity's Last Exam (HLE) remains both conceptually challenging and computationally expensive.. We show that small orchestrators managing other models and a variety of tools can both push the upper bound of intelligence and improve efficiency in solving difficult agentic tasks..

We introduce ToolOrchestra, a method for training small orchestrators that coordinate intelligent tools.. ToolOrchestra explicitly uses reinforcement learning with outcome-, efficiency-, and user-preference-aware rewards.. Using ToolOrchestra, we produce Orchestrator, an 8B model that achieves higher accuracy at lower cost than previous tool-use agents while aligning with user preferences on which tools are to be used for a given query.. On HLE, Orchestrator achieves a score of 37.1%, outperforming GPT-5 (35.1%) while being 2.5x more efficient.. On tau2-Bench and FRAMES, Orchestrator surpasses GPT-5 by a wide margin while using only about 30% of the cost..

Extensive analysis shows that Orchestrator achieves the best trade-off between performance and cost under multiple metrics, and generalizes robustly to unseen tools.. These results demonstrate that composing diverse tools with a lightweight orchestration model is both more efficient and more effective than existing methods, paving the way for practical and scalable tool-augmented reasoning systems..

---

## 2. Agentic Learner with Grow-and-Refine Multimodal Semantic Memory

🧠 **Category:** CS.AI | 📅 **Published:** November 26, 2025 | 🔥 **Score:** 25 points

**Authors:** Weihao Bo, Shan Zhang, Yanpeng Sun et al. (+9 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2511.21678v1) | [PDF Download](https://arxiv.org/pdf/2511.21678v1.pdf)

MLLMs exhibit strong reasoning on isolated queries, yet they operate de novo -- solving each problem independently and often repeating the same mistakes.. Existing memory-augmented agents mainly store past trajectories for reuse..

However, trajectory-based memory suffers from brevity bias, gradually losing essential domain knowledge.. More critically, even in truly multimodal problem-solving settings, it records only a single-modality trace of past behavior, failing to preserve how visual attention and logical reasoning jointly contributed to the solution.. This is fundamentally misaligned with human cognition: semantic memory is both multimodal and integrated, preserving visual and abstract knowledge through coordinated but distinct representational streams.. We thus introduce ViLoMem, a dual-stream memory framework that constructs compact, schema-based memory.. It separately encodes visual distraction patterns and logical reasoning errors, enabling MLLMs to learn from their successful and failed experiences.. Following a grow-and-refine principle, the system incrementally accumulates and updates multimodal semantic knowledge -- preserving stable, generalizable strategies while avoiding catastrophic forgetting.. Across six multimodal benchmarks, ViLoMem consistently improves pass@1 accuracy and substantially reduces repeated visual and logical errors..

Ablations confirm the necessity of dual-stream memory with explicit distraction--hallucination separation, demonstrating the value of error-aware multimodal memory for lifelong and cross-domain agentic learning.. Our project page will be available at https://weihao-bo.github.io/ViLoMeo-page..

---

## 3. On the Limits of Innate Planning in Large Language Models

🧠 **Category:** CS.AI | 📅 **Published:** November 26, 2025 | 🔥 **Score:** 25 points

**Authors:** Charles Schepanowski, Charles Ling

**Links:** [ArXiv Paper](https://arxiv.org/abs/2511.21591v1) | [PDF Download](https://arxiv.org/pdf/2511.21591v1.pdf)

Large language models (LLMs) achieve impressive results on many benchmarks, yet their capacity for planning and stateful reasoning remains unclear.. We study these abilities directly, without code execution or other tools, using the 8-puzzle: a classic task that requires state tracking and goal-directed planning while allowing precise, step-by-step evaluation..

Four models are tested under common prompting conditions (Zero-Shot, Chain-of-Thought, Algorithm-of-Thought) and with tiered corrective feedback.. Feedback improves success rates for some model-prompt combinations, but many successful runs are long, computationally expensive, and indirect.. We then examine the models with an external move validator that provides only valid moves.. Despite this level of assistance, none of the models solve any puzzles in this setting..

Qualitative analysis reveals two dominant deficits across all models: (1) brittle internal state representations, leading to frequent invalid moves, and (2) weak heuristic planning, with models entering loops or selecting actions that do not reduce the distance to the goal state.. These findings indicate that, in the absence of external tools such as code interpreters, current LLMs have substantial limitations in planning and that further progress may require mechanisms for maintaining explicit state and performing structured search..

---

## 4. Tool-RoCo: An Agent-as-Tool Self-organization Large Language Model Benchmark in Multi-robot Cooperation

🧠 **Category:** CS.AI | 📅 **Published:** November 26, 2025 | 🔥 **Score:** 25 points

**Authors:** Ke Zhang, Xiaoning Zhao, Ce Zheng et al. (+5 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2511.21510v1) | [PDF Download](https://arxiv.org/pdf/2511.21510v1.pdf)

This study proposes Tool-RoCo, a novel benchmark for evaluating large language models (LLMs) in long-term multi-agent cooperation based on RoCo, a multi-robot cooperative benchmark.. Recent research on LLM-based multi-agent systems has relied on predefined orchestration, while ignoring agent autonomy..

Tool-RoCo treats other agents as tools and introduces cooperative tools, leveraging tool usage to evaluate multi-agent cooperation and self-organization.. Tool usage means that each agent (LLM) selects a tool from a candidate set based on the current state, receives feedback, and adjusts its selection in subsequent rounds.. To evaluate different autonomy levels, we propose four LLM paradigms: (1) centralized cooperation, where a single LLM allocates tools to all agents; (2) centralized self-organization, where a central LLM autonomously activates agents while keeping others inactive; (3) decentralized cooperation, where each agent has its own LLM and calls tools based on local information; and (4) self-organization, where a randomly chosen initial agent can request collaboration, activating additional agents via tool calls.. Tool-RoCo includes three multi-robot tasks, SORT, PACK, and CABINET, to measure format and parameter accuracy and agent coordination through tool usage.. The results using several LLMs showed that cooperative tools accounted for only 7.09% of all tools, indicating that LLM-based agents rarely invoked others as assistants.. Moreover, activation tools accounted for 96.42%, suggesting that current LLMs tend to maintain active agents while seldom deactivating them for adaptive coordination..

Tool-RoCo provides a systematic benchmark to evaluate LLM autonomy and cooperation in multi-agent tasks.. Code and Demo: https://github.com/ColaZhang22/Tool-Roco.

---

## 5. SpatialBench: Benchmarking Multimodal Large Language Models for Spatial Cognition

🧠 **Category:** CS.AI | 📅 **Published:** November 26, 2025 | 🔥 **Score:** 25 points

**Authors:** Peiran Xu, Sudong Wang, Yao Zhu et al. (+2 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2511.21471v1) | [PDF Download](https://arxiv.org/pdf/2511.21471v1.pdf)

Spatial cognition is fundamental to real-world multimodal intelligence, allowing models to effectively interact with the physical environment.. While multimodal large language models (MLLMs) have made significant strides, existing benchmarks often oversimplify spatial cognition, reducing it to a single-dimensional metric, which fails to capture the hierarchical structure and interdependence of spatial abilities..

To address this gap, we propose a hierarchical spatial cognition framework that decomposes spatial intelligence into five progressively complex levels from basic observation to high-level planning.. Building upon this taxonomy, we construct SpatialBench, a large-scale, fine-grained benchmark covering 15 tasks aligned with these cognitive levels.. To provide a unified evaluation across heterogeneous tasks, we further introduce a high-level capability-oriented metric that reliably assesses a model's overall spatial reasoning ability.. Extensive experiments over massive MLLMs reveal distinct performance stratification across cognitive levels: models exhibit strong perceptual grounding yet remain limited in symbolic reasoning, causal inference, and planning..

Additional human tests demonstrate that humans perform selective, goal-directed abstraction, while MLLMs tend to over-attend to surface details without coherent spatial intent.. Our work establishes the first systematic framework for measuring hierarchical spatial cognition in MLLMs, laying the foundation for future spatially intelligent systems..

---


## 📈 About This Analysis

Each week, I analyze recent AI papers from ArXiv and rank them based on:

🗣️ **Social Media Engagement** - Mentions and discussions on Reddit  
🎯 **Research Impact Indicators** - Trending keywords and methodologies  
👥 **Collaboration Signals** - Author networks and institutional diversity  
⏰ **Recency Factor** - Boost for just-published papers  

**Methodology:** Papers are scored using a composite algorithm that weighs social media mentions (Reddit discussions, estimated Twitter activity) alongside content analysis for breakthrough keywords like "transformer," "multimodal," "reasoning," and others that typically indicate high-impact research.

**Coverage:** This analysis scans 7 major AI categories on ArXiv: Artificial Intelligence, Machine Learning, Natural Language Processing, Computer Vision, Neural Networks, Robotics, and Statistics ML.

---

*🤖 This analysis is automatically generated every Friday by monitoring ArXiv submissions and tracking social media engagement.*

**📬 Subscribe** for weekly AI research updates  
**💬 Share your thoughts** on this week's selections in the comments  
**🔗 Follow the project** on [GitHub](https://github.com/kjanik70/ai-papers-agent)

*Next edition: December 05, 2025*
