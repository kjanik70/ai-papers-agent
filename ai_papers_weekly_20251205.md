# 🤖 Top 5 AI Papers This Week
## Week of December 05, 2025

Welcome to this week's roundup of the most impactful AI research papers! These papers have been generating buzz across Reddit, academic Twitter, and research communities.

**📊 This Week's Stats:**
- 📄 **5 featured papers** from **1 categories**  
- 👥 **44 contributing authors**
- 🔥 **Average engagement score:** 25.0
- 🏆 **Highest scorer:** 25 points

---

## 1. DraCo: Draft as CoT for Text-to-Image Preview and Rare Concept Generation

🧠 **Category:** CS.AI | 📅 **Published:** December 04, 2025 | 🔥 **Score:** 25 points

**Authors:** Dongzhi Jiang, Renrui Zhang, Haodong Li et al. (+9 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2512.05112v1) | [PDF Download](https://arxiv.org/pdf/2512.05112v1.pdf)

Recent unified multimodal large language models (MLLMs) have shown impressive capabilities, incorporating chain-of-thought (CoT) reasoning for enhanced text-to-image generation.. However, existing approaches remain limited, either treating the model merely as a standalone generator or relying on abstract textual planning..

To this end, we propose Draft-as-CoT (DraCo), a novel interleaved reasoning paradigm that fully leverages both textual and visual contents in CoT for better planning and verification.. Our method first generates a low-resolution draft image as preview, providing more concrete and structural visual planning and guidance.. Then, we employ the model's inherent understanding capability to verify potential semantic misalignments between the draft and input prompt, and performs refinement through selective corrections with super-resolution.. In this way, our approach addresses two fundamental challenges: the coarse-grained nature of textual planning and the difficulty in generating rare attribute combinations..

To support training, we curate DraCo-240K, aiming to enhance three atomic capabilities spanning general correction, instance manipulation, and layout reorganization.. Supported by DraCo-CFG, a specialized classifier-free guidance (CFG) strategy for interleaved reasoning, DraCo achieves a tremendous increase on GenEval (+8%), Imagine-Bench (+0.91), and GenEval++ (+3%), significantly outperforming direct generation and other generation methods empowered by CoT..

---

## 2. Semantic Soft Bootstrapping: Long Context Reasoning in LLMs without Reinforcement Learning

🧠 **Category:** CS.AI | 📅 **Published:** December 04, 2025 | 🔥 **Score:** 25 points

**Authors:** Purbesh Mitra, Sennur Ulukus

**Links:** [ArXiv Paper](https://arxiv.org/abs/2512.05105v1) | [PDF Download](https://arxiv.org/pdf/2512.05105v1.pdf)

Long context reasoning in large language models (LLMs) has demonstrated enhancement of their cognitive capabilities via chain-of-thought (CoT) inference.. Training such models is usually done via reinforcement learning with verifiable rewards (RLVR) in reasoning based problems, like math and programming..

However, RLVR is limited by several bottlenecks, such as, lack of dense reward, and inadequate sample efficiency.. As a result, it requires significant compute resources in post-training phase.. To overcome these limitations, in this work, we propose \textbf{Semantic Soft Bootstrapping (SSB)}, a self-distillation technique, in which the same base language model plays the role of both teacher and student, but receives different semantic contexts about the correctness of its outcome at training time.. The model is first prompted with a math problem and several rollouts are generated.. From them, the correct and most common incorrect response are filtered, and then provided to the model in context to produce a more robust, step-by-step explanation with a verified final answer.. This pipeline automatically curates a paired teacher-student training set from raw problem-answer data, without any human intervention.. This generation process also produces a sequence of logits, which is what the student model tries to match in the training phase just from the bare question alone.. In our experiment, Qwen2.5-3B-Instruct on GSM8K dataset via parameter-efficient fine-tuning.. We then tested its accuracy on MATH500, and AIME2024 benchmarks..

Our experiments show a jump of 10.6%, and 10% improvements in accuracy, respectively, over group relative policy optimization (GRPO), which is a commonly used RLVR algorithm.. Our code is available at https://github.com/purbeshmitra/semantic-soft-bootstrapping, and the model, curated dataset is available at https://huggingface.co/purbeshmitra/semantic-soft-bootstrapping..

---

## 3. TV2TV: A Unified Framework for Interleaved Language and Video Generation

🧠 **Category:** CS.AI | 📅 **Published:** December 04, 2025 | 🔥 **Score:** 25 points

**Authors:** Xiaochuang Han, Youssef Emad, Melissa Hall et al. (+15 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2512.05103v1) | [PDF Download](https://arxiv.org/pdf/2512.05103v1.pdf)

Video generation models are rapidly advancing, but can still struggle with complex video outputs that require significant semantic branching or repeated high-level reasoning about what should happen next.. In this paper, we introduce a new class of omni video-text models that integrate ideas from recent LM reasoning advances to address this challenge..

More specifically, we present TV2TV, a unified generative modeling framework which decomposes video generation into an interleaved text and video generation process.. TV2TV jointly learns language modeling (next-token prediction) and video flow matching (next-frame prediction) using a Mixture-of-Transformers (MoT) architecture.. At inference time, TV2TV decides when to alternate between generating text and video frames, allowing the model to "think in words" about subsequent content before ``acting in pixels'' to produce frames.. This design offloads much of the responsibility for deciding what should happen next to the language modeling tower, enabling improved visual quality and prompt alignment of generated videos.. It also enables fine-grained controllability, allowing users to modify the video generation trajectory through text interventions at any point in the process.. In controlled experiments on video game data, TV2TV demonstrates substantial improvements in both visual quality and controllability.. TV2TV also scales to natural videos, as we show by augmenting sports videos with interleaved natural language action descriptions using vision-language models (VLMs)..

Training TV2TV on this corpus yields strong visual quality and prompt alignment, showcasing the model's ability to reason about and generate complex real-world action sequences.. Together, these results highlight TV2TV as a promising step toward video generation with open-ended textual reasoning and control..

---

## 4. Reflection Removal through Efficient Adaptation of Diffusion Transformers

🧠 **Category:** CS.AI | 📅 **Published:** December 04, 2025 | 🔥 **Score:** 25 points

**Authors:** Daniyar Zakarin, Thiemo Wandel, Anton Obukhov et al. (+1 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2512.05000v1) | [PDF Download](https://arxiv.org/pdf/2512.05000v1.pdf)

We introduce a diffusion-transformer (DiT) framework for single-image reflection removal that leverages the generalization strengths of foundation diffusion models in the restoration setting.. Rather than relying on task-specific architectures, we repurpose a pre-trained DiT-based foundation model by conditioning it on reflection-contaminated inputs and guiding it toward clean transmission layers..

We systematically analyze existing reflection removal data sources for diversity, scalability, and photorealism.. To address the shortage of suitable data, we construct a physically based rendering (PBR) pipeline in Blender, built around the Principled BSDF, to synthesize realistic glass materials and reflection effects.. Efficient LoRA-based adaptation of the foundation model, combined with the proposed synthetic data, achieves state-of-the-art performance on in-domain and zero-shot benchmarks..

These results demonstrate that pretrained diffusion transformers, when paired with physically grounded data synthesis and efficient adaptation, offer a scalable and high-fidelity solution for reflection removal.. Project page: https://hf.co/spaces/huawei-bayerlab/windowseat-reflection-removal-web.

---

## 5. STELLA: Guiding Large Language Models for Time Series Forecasting with Semantic Abstractions

🧠 **Category:** CS.AI | 📅 **Published:** December 04, 2025 | 🔥 **Score:** 25 points

**Authors:** Junjie Fan, Hongye Zhao, Linduo Wei et al. (+5 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2512.04871v1) | [PDF Download](https://arxiv.org/pdf/2512.04871v1.pdf)

Recent adaptations of Large Language Models (LLMs) for time series forecasting often fail to effectively enhance information for raw series, leaving LLM reasoning capabilities underutilized.. Existing prompting strategies rely on static correlations rather than generative interpretations of dynamic behavior, lacking critical global and instance-specific context..

To address this, we propose STELLA (Semantic-Temporal Alignment with Language Abstractions), a framework that systematically mines and injects structured supplementary and complementary information.. STELLA employs a dynamic semantic abstraction mechanism that decouples input series into trend, seasonality, and residual components.. It then translates intrinsic behavioral features of these components into Hierarchical Semantic Anchors: a Corpus-level Semantic Prior (CSP) for global context and a Fine-grained Behavioral Prompt (FBP) for instance-level patterns.. Using these anchors as prefix-prompts, STELLA guides the LLM to model intrinsic dynamics..

Experiments on eight benchmark datasets demonstrate that STELLA outperforms state-of-the-art methods in long- and short-term forecasting, showing superior generalization in zero-shot and few-shot settings.. Ablation studies further validate the effectiveness of our dynamically generated semantic anchors..

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

*Next edition: December 12, 2025*
