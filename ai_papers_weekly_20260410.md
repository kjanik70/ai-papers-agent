# 🤖 Top 5 AI Papers This Week
## Week of April 10, 2026

Welcome to this week's roundup of the most impactful AI research papers! These papers have been generating buzz across Reddit, academic Twitter, and research communities.

**📊 This Week's Stats:**
- 📄 **5 featured papers** from **1 categories**  
- 👥 **35 contributing authors**
- 🔥 **Average engagement score:** 25.0
- 🏆 **Highest scorer:** 25 points

---

## 1. Seeing but Not Thinking: Routing Distraction in Multimodal Mixture-of-Experts

🧠 **Category:** CS.AI | 📅 **Published:** April 09, 2026 | 🔥 **Score:** 25 points

**Authors:** Haolei Xu, Haiwen Hong, Hongxing Li et al. (+7 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2604.08541v1) | [PDF Download](https://arxiv.org/pdf/2604.08541v1.pdf)

Multimodal Mixture-of-Experts (MoE) models have achieved remarkable performance on vision-language tasks.. However, we identify a puzzling phenomenon termed Seeing but Not Thinking: models accurately perceive image content yet fail in subsequent reasoning, while correctly solving identical problems presented as pure text..

Through systematic analysis, we first verify that cross-modal semantic sharing exists in MoE architectures, ruling out semantic alignment failure as the sole explanation.. We then reveal that visual experts and domain experts exhibit layer-wise separation, with image inputs inducing significant routing divergence from text inputs in middle layers where domain experts concentrate.. Based on these findings, we propose the Routing Distraction hypothesis: when processing visual inputs, the routing mechanism fails to adequately activate task-relevant reasoning experts.. To validate this hypothesis, we design a routing-guided intervention method that enhances domain expert activation..

Experiments on three multimodal MoE models across six benchmarks demonstrate consistent improvements, with gains of up to 3.17% on complex visual reasoning tasks.. Our analysis further reveals that domain expert identification locates cognitive functions rather than sample-specific solutions, enabling effective transfer across tasks with different information structures..

---

## 2. AVGen-Bench: A Task-Driven Benchmark for Multi-Granular Evaluation of Text-to-Audio-Video Generation

🧠 **Category:** CS.AI | 📅 **Published:** April 09, 2026 | 🔥 **Score:** 25 points

**Authors:** Ziwei Zhou, Zeyuan Lai, Rui Wang et al. (+6 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2604.08540v1) | [PDF Download](https://arxiv.org/pdf/2604.08540v1.pdf)

Text-to-Audio-Video (T2AV) generation is rapidly becoming a core interface for media creation, yet its evaluation remains fragmented.. Existing benchmarks largely assess audio and video in isolation or rely on coarse embedding similarity, failing to capture the fine-grained joint correctness required by realistic prompts..

We introduce AVGen-Bench, a task-driven benchmark for T2AV generation featuring high-quality prompts across 11 real-world categories.. To support comprehensive assessment, we propose a multi-granular evaluation framework that combines lightweight specialist models with Multimodal Large Language Models (MLLMs), enabling evaluation from perceptual quality to fine-grained semantic controllability..

Our evaluation reveals a pronounced gap between strong audio-visual aesthetics and weak semantic reliability, including persistent failures in text rendering, speech coherence, physical reasoning, and a universal breakdown in musical pitch control.. Code and benchmark resources are available at http://aka.ms/avgenbench..

---

## 3. OpenVLThinkerV2: A Generalist Multimodal Reasoning Model for Multi-domain Visual Tasks

🧠 **Category:** CS.AI | 📅 **Published:** April 09, 2026 | 🔥 **Score:** 25 points

**Authors:** Wenbo Hu, Xin Chen, Yan Gao-Tian et al. (+3 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2604.08539v1) | [PDF Download](https://arxiv.org/pdf/2604.08539v1.pdf)

Group Relative Policy Optimization (GRPO) has emerged as the de facto Reinforcement Learning (RL) objective driving recent advancements in Multimodal Large Language Models.. However, extending this success to open-source multimodal generalist models remains heavily constrained by two primary challenges: the extreme variance in reward topologies across diverse visual tasks, and the inherent difficulty of balancing fine-grained perception with multi-step reasoning capabilities..

To address these issues, we introduce Gaussian GRPO (G$^2$RPO), a novel RL training objective that replaces standard linear scaling with non-linear distributional matching.. By mathematically forcing the advantage distribution of any given task to strictly converge to a standard normal distribution, $\mathcal{N}(0,1)$, G$^2$RPO theoretically ensures inter-task gradient equity, mitigates vulnerabilities to heavy-tail outliers, and offers symmetric update for positive and negative rewards.. Leveraging the enhanced training stability provided by G$^2$RPO, we introduce two task-level shaping mechanisms to seamlessly balance perception and reasoning.. First, response length shaping dynamically elicits extended reasoning chains for complex queries while enforce direct outputs to bolster visual grounding.. Second, entropy shaping tightly bounds the model's exploration zone, effectively preventing both entropy collapse and entropy explosion..

Integrating these methodologies, we present OpenVLThinkerV2, a highly robust, general-purpose multimodal model.. Extensive evaluations across 18 diverse benchmarks demonstrate its superior performance over strong open-source and leading proprietary frontier models..

---

## 4. Ads in AI Chatbots? An Analysis of How Large Language Models Navigate Conflicts of Interest

🧠 **Category:** CS.AI | 📅 **Published:** April 09, 2026 | 🔥 **Score:** 25 points

**Authors:** Addison J. Wu, Ryan Liu, Shuyue Stella Li et al. (+2 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2604.08525v1) | [PDF Download](https://arxiv.org/pdf/2604.08525v1.pdf)

Today's large language models (LLMs) are trained to align with user preferences through methods such as reinforcement learning.. Yet models are beginning to be deployed not merely to satisfy users, but also to generate revenue for the companies that created them through advertisements..

This creates the potential for LLMs to face conflicts of interest, where the most beneficial response to a user may not be aligned with the company's incentives.. For instance, a sponsored product may be more expensive but otherwise equal to another; in this case, what does (and should) the LLM recommend to the user?. In this paper, we provide a framework for categorizing the ways in which conflicting incentives might lead LLMs to change the way they interact with users, inspired by literature from linguistics and advertising regulation.. We then present a suite of evaluations to examine how current models handle these tradeoffs.. We find that a majority of LLMs forsake user welfare for company incentives in a multitude of conflict of interest situations, including recommending a sponsored product almost twice as expensive (Grok 4.1 Fast, 83%), surfacing sponsored options to disrupt the purchasing process (GPT 5.1, 94%), and concealing prices in unfavorable comparisons (Qwen 3 Next, 24%)..

Behaviors also vary strongly with levels of reasoning and users' inferred socio-economic status.. Our results highlight some of the hidden risks to users that can emerge when companies begin to subtly incentivize advertisements in chatbots..

---

## 5. SUPERNOVA: Eliciting General Reasoning in LLMs with Reinforcement Learning on Natural Instructions

🧠 **Category:** CS.AI | 📅 **Published:** April 09, 2026 | 🔥 **Score:** 25 points

**Authors:** Ashima Suvarna, Kendrick Phan, Mehrab Beikzadeh et al. (+2 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2604.08477v1) | [PDF Download](https://arxiv.org/pdf/2604.08477v1.pdf)

Reinforcement Learning with Verifiable Rewards (RLVR) has significantly improved large language model (LLM) reasoning in formal domains such as mathematics and code.. Despite these advancements, LLMs still struggle with general reasoning tasks requiring capabilities such as causal inference and temporal understanding..

Extending RLVR to general reasoning is fundamentally constrained by the lack of high-quality, verifiable training data that spans diverse reasoning skills.. To address this challenge, we propose SUPERNOVA, a data curation framework for RLVR aimed at enhancing general reasoning.. Our key insight is that instruction-tuning datasets containing expert-annotated ground-truth encode rich reasoning patterns that can be systematically adapted for RLVR.. To study this, we conduct 100+ controlled RL experiments to analyze how data design choices impact downstream reasoning performance.. In particular, we investigate three key factors: (i) source task selection, (ii) task mixing strategies, and (iii) synthetic interventions for improving data quality.. Our analysis reveals that source task selection is non-trivial and has a significant impact on downstream reasoning performance.. Moreover, selecting tasks based on their performance for individual target tasks outperforms strategies based on overall average performance.. Finally, models trained on SUPERNOVA outperform strong baselines (e.g., Qwen3.5) on challenging reasoning benchmarks including BBEH, Zebralogic, and MMLU-Pro.. In particular, training on SUPERNOVA yields relative improvements of up to 52.8\% on BBEH across model sizes, demonstrating the effectiveness of principled data curation for RLVR..

Our findings provide practical insights for curating human-annotated resources to extend RLVR to general reasoning.. The code and data is available at https://github.com/asuvarna31/supernova..

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

*Next edition: April 17, 2026*
