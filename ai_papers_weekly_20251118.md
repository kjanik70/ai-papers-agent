# 🤖 Top 5 AI Papers This Week
## Week of November 18, 2025

Welcome to this week's roundup of the most impactful AI research papers! These papers have been generating buzz across Reddit, academic Twitter, and research communities.

**📊 This Week's Stats:**
- 📄 **5 featured papers** from **1 categories**  
- 👥 **37 contributing authors**
- 🔥 **Average engagement score:** 25.0
- 🏆 **Highest scorer:** 25 points

---

## 1. SGuard-v1: Safety Guardrail for Large Language Models

🧠 **Category:** CS.AI | 📅 **Published:** November 16, 2025 | 🔥 **Score:** 25 points

**Authors:** JoonHo Lee, HyeonMin Cho, Jaewoong Yun et al. (+3 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2511.12497v1) | [PDF Download](https://arxiv.org/pdf/2511.12497v1.pdf)

We present SGuard-v1, a lightweight safety guardrail for Large Language Models (LLMs), which comprises two specialized models to detect harmful content and screen adversarial prompts in human-AI conversational settings.. The first component, ContentFilter, is trained to identify safety risks in LLM prompts and responses in accordance with the MLCommons hazard taxonomy, a comprehensive framework for trust and safety assessment of AI..

The second component, JailbreakFilter, is trained with a carefully designed curriculum over integrated datasets and findings from prior work on adversarial prompting, covering 60 major attack types while mitigating false-unsafe classification.. SGuard-v1 is built on the 2B-parameter Granite-3.3-2B-Instruct model that supports 12 languages.. We curate approximately 1.4 million training instances from both collected and synthesized data and perform instruction tuning on the base model, distributing the curated data across the two component according to their designated functions.. Through extensive evaluation on public and proprietary safety benchmarks, SGuard-v1 achieves state-of-the-art safety performance while remaining lightweight, thereby reducing deployment overhead..

SGuard-v1 also improves interpretability for downstream use by providing multi-class safety predictions and their binary confidence scores.. We release the SGuard-v1 under the Apache-2.0 License to enable further research and practical deployment in AI safety..

---

## 2. ARCHE: A Novel Task to Evaluate LLMs on Latent Reasoning Chain Extraction

🧠 **Category:** CS.AI | 📅 **Published:** November 16, 2025 | 🔥 **Score:** 25 points

**Authors:** Pengze Li, Jiaqi Liu, Junchi Yu et al. (+5 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2511.12485v1) | [PDF Download](https://arxiv.org/pdf/2511.12485v1.pdf)

Large language models (LLMs) are increasingly used in scientific domains.. While they can produce reasoning-like content via methods such as chain-of-thought prompting, these outputs are typically unstructured and informal, obscuring whether models truly understand the fundamental reasoning paradigms that underpin scientific inference..

To address this, we introduce a novel task named Latent Reasoning Chain Extraction (ARCHE), in which models must decompose complex reasoning arguments into combinations of standard reasoning paradigms in the form of a Reasoning Logic Tree (RLT).. In RLT, all reasoning steps are explicitly categorized as one of three variants of Peirce's fundamental inference modes: deduction, induction, or abduction.. To facilitate this task, we release ARCHE Bench, a new benchmark derived from 70 Nature Communications articles, including more than 1,900 references and 38,000 viewpoints.. We propose two logic-aware evaluation metrics: Entity Coverage (EC) for content completeness and Reasoning Edge Accuracy (REA) for step-by-step logical validity..

Evaluations on 10 leading LLMs on ARCHE Bench reveal that models exhibit a trade-off between REA and EC, and none are yet able to extract a complete and standard reasoning chain.. These findings highlight a substantial gap between the abilities of current reasoning models and the rigor required for scientific argumentation..

---

## 3. Assessing LLMs for Serendipity Discovery in Knowledge Graphs: A Case for Drug Repurposing

🧠 **Category:** CS.AI | 📅 **Published:** November 16, 2025 | 🔥 **Score:** 25 points

**Authors:** Mengying Wang, Chenhui Ma, Ao Jiao et al. (+6 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2511.12472v1) | [PDF Download](https://arxiv.org/pdf/2511.12472v1.pdf)

Large Language Models (LLMs) have greatly advanced knowledge graph question answering (KGQA), yet existing systems are typically optimized for returning highly relevant but predictable answers.. A missing yet desired capacity is to exploit LLMs to suggest surprise and novel ("serendipitious") answers..

In this paper, we formally define the serendipity-aware KGQA task and propose the SerenQA framework to evaluate LLMs' ability to uncover unexpected insights in scientific KGQA tasks.. SerenQA includes a rigorous serendipity metric based on relevance, novelty, and surprise, along with an expert-annotated benchmark derived from the Clinical Knowledge Graph, focused on drug repurposing.. Additionally, it features a structured evaluation pipeline encompassing three subtasks: knowledge retrieval, subgraph reasoning, and serendipity exploration..

Our experiments reveal that while state-of-the-art LLMs perform well on retrieval, they still struggle to identify genuinely surprising and valuable discoveries, underscoring a significant room for future improvements.. Our curated resources and extended version are released at: https://cwru-db-group.github.io/serenQA..

---

## 4. Personality-guided Public-Private Domain Disentangled Hypergraph-Former Network for Multimodal Depression Detection

🧠 **Category:** CS.AI | 📅 **Published:** November 16, 2025 | 🔥 **Score:** 25 points

**Authors:** Changzeng Fu, Shiwen Zhao, Yunze Zhang et al. (+3 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2511.12460v1) | [PDF Download](https://arxiv.org/pdf/2511.12460v1.pdf)

Depression represents a global mental health challenge requiring efficient and reliable automated detection methods.. Current Transformer- or Graph Neural Networks (GNNs)-based multimodal depression detection methods face significant challenges in modeling individual differences and cross-modal temporal dependencies across diverse behavioral contexts..

Therefore, we propose P$^3$HF (Personality-guided Public-Private Domain Disentangled Hypergraph-Former Network) with three key innovations: (1) personality-guided representation learning using LLMs to transform discrete individual features into contextual descriptions for personalized encoding; (2) Hypergraph-Former architecture modeling high-order cross-modal temporal relationships; (3) event-level domain disentanglement with contrastive learning for improved generalization across behavioral contexts.. Experiments on MPDD-Young dataset show P$^3$HF achieves around 10\% improvement on accuracy and weighted F1 for binary and ternary depression classification task over existing methods..

Extensive ablation studies validate the independent contribution of each architectural component, confirming that personality-guided representation learning and high-order hypergraph reasoning are both essential for generating robust, individual-aware depression-related representations.. The code is released at https://github.com/hacilab/P3HF..

---

## 5. MOON2.0: Dynamic Modality-balanced Multimodal Representation Learning for E-commerce Product Understanding

🧠 **Category:** CS.AI | 📅 **Published:** November 16, 2025 | 🔥 **Score:** 25 points

**Authors:** Zhanheng Nie, Chenghan Fu, Daoze Zhang et al. (+5 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2511.12449v1) | [PDF Download](https://arxiv.org/pdf/2511.12449v1.pdf)

The rapid growth of e-commerce calls for multimodal models that comprehend rich visual and textual product information.. Although recent multimodal large language models (MLLMs) for product understanding exhibit strong capability in representation learning for e-commerce, they still face three challenges: (i) the modality imbalance induced by modality mixed training; (ii) underutilization of the intrinsic alignment relationships among visual and textual information within a product; and (iii) limited handling of noise in e-commerce multimodal data..

To address these, we propose MOON2.0, a dynamic modality-balanced multimodal representation learning framework for e-commerce product understanding.. MOON2.0 comprises: (1) a Modality-driven Mixture-of-Experts (MoE) module that adaptively processes input samples by their modality composition, enabling Multimodal Joint Learning to mitigate the modality imbalance; (2) a Dual-level Alignment method to better leverage semantic alignment properties inside individual products; and (3) an MLLM-based Image-text Co-augmentation strategy that integrates textual enrichment with visual expansion, coupled with Dynamic Sample Filtering to improve training data quality.. We further introduce MBE2.0, a co-augmented multimodal representation benchmark for e-commerce representation learning and evaluation..

Experiments show that MOON2.0 delivers state-of-the-art zero-shot performance on MBE2.0 and multiple public datasets.. Furthermore, attention-based heatmap visualization provides qualitative evidence of improved multimodal alignment of MOON2.0..

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

*Next edition: November 25, 2025*
