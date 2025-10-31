# 🤖 Top 5 AI Papers This Week
## Week of October 31, 2025

Welcome to this week's roundup of the most impactful AI research papers! These papers have been generating buzz across Reddit, academic Twitter, and research communities.

**📊 This Week's Stats:**
- 📄 **5 featured papers** from **1 categories**  
- 👥 **35 contributing authors**
- 🔥 **Average engagement score:** 25.0
- 🏆 **Highest scorer:** 25 points

---

## 1. Defeating the Training-Inference Mismatch via FP16

🧠 **Category:** CS.AI | 📅 **Published:** October 30, 2025 | 🔥 **Score:** 25 points

**Authors:** Penghui Qi, Zichen Liu, Xiangxin Zhou et al. (+4 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2510.26788v1) | [PDF Download](https://arxiv.org/pdf/2510.26788v1.pdf)

Reinforcement learning (RL) fine-tuning of large language models (LLMs) often suffers from instability due to the numerical mismatch between the training and inference policies.. While prior work has attempted to mitigate this issue through algorithmic corrections or engineering alignments, we show that its root cause lies in the floating point precision itself..

The widely adopted BF16, despite its large dynamic range, introduces large rounding errors that breaks the consistency between training and inference.. In this work, we demonstrate that simply reverting to \textbf{FP16} effectively eliminates this mismatch.. The change is simple, fully supported by modern frameworks with only a few lines of code change, and requires no modification to the model architecture or learning algorithm..

Our results suggest that using FP16 uniformly yields more stable optimization, faster convergence, and stronger performance across diverse tasks, algorithms and frameworks.. We hope these findings motivate a broader reconsideration of precision trade-offs in RL fine-tuning..

---

## 2. AMO-Bench: Large Language Models Still Struggle in High School Math
  Competitions

🧠 **Category:** CS.AI | 📅 **Published:** October 30, 2025 | 🔥 **Score:** 25 points

**Authors:** Shengnan An, Xunliang Cai, Xuezhi Cao et al. (+8 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2510.26768v1) | [PDF Download](https://arxiv.org/pdf/2510.26768v1.pdf)

We present AMO-Bench, an Advanced Mathematical reasoning benchmark with Olympiad level or even higher difficulty, comprising 50 human-crafted problems.. Existing benchmarks have widely leveraged high school math competitions for evaluating mathematical reasoning capabilities of large language models (LLMs)..

However, many existing math competitions are becoming less effective for assessing top-tier LLMs due to performance saturation (e.g., AIME24/25).. To address this, AMO-Bench introduces more rigorous challenges by ensuring all 50 problems are (1) cross-validated by experts to meet at least the International Mathematical Olympiad (IMO) difficulty standards, and (2) entirely original problems to prevent potential performance leakages from data memorization.. Moreover, each problem in AMO-Bench requires only a final answer rather than a proof, enabling automatic and robust grading for evaluation.. Experimental results across 26 LLMs on AMO-Bench show that even the best-performing model achieves only 52.4% accuracy on AMO-Bench, with most LLMs scoring below 40%.. Beyond these poor performances, our further analysis reveals a promising scaling trend with increasing test-time compute on AMO-Bench..

These results highlight the significant room for improving the mathematical reasoning in current LLMs.. We release AMO-Bench to facilitate further research into advancing the reasoning abilities of language models. https://amo-bench.github.io/.

---

## 3. Unveiling Intrinsic Text Bias in Multimodal Large Language Models
  through Attention Key-Space Analysis

🧠 **Category:** CS.AI | 📅 **Published:** October 30, 2025 | 🔥 **Score:** 25 points

**Authors:** Xinhan Zheng, Huyu Wu, Xueting Wang et al. (+1 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2510.26721v1) | [PDF Download](https://arxiv.org/pdf/2510.26721v1.pdf)

Multimodal large language models (MLLMs) exhibit a pronounced preference for textual inputs when processing vision-language data, limiting their ability to reason effectively from visual evidence.. Unlike prior studies that attribute this text bias to external factors such as data imbalance or instruction tuning, we propose that the bias originates from the model's internal architecture..

Specifically, we hypothesize that visual key vectors (Visual Keys) are out-of-distribution (OOD) relative to the text key space learned during language-only pretraining.. Consequently, these visual keys receive systematically lower similarity scores during attention computation, leading to their under-utilization in the context representation.. To validate this hypothesis, we extract key vectors from LLaVA and Qwen2.5-VL and analyze their distributional structures using qualitative (t-SNE) and quantitative (Jensen-Shannon divergence) methods.. The results provide direct evidence that visual and textual keys occupy markedly distinct subspaces within the attention space..

The inter-modal divergence is statistically significant, exceeding intra-modal variation by several orders of magnitude.. These findings reveal that text bias arises from an intrinsic misalignment within the attention key space rather than solely from external data factors..

---

## 4. Evontree: Ontology Rule-Guided Self-Evolution of Large Language Models

🧠 **Category:** CS.AI | 📅 **Published:** October 30, 2025 | 🔥 **Score:** 25 points

**Authors:** Mingchen Tu, Zhiqiang Liu, Juan Li et al. (+4 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2510.26683v1) | [PDF Download](https://arxiv.org/pdf/2510.26683v1.pdf)

Large language models (LLMs) have demonstrated exceptional capabilities across multiple domains by leveraging massive pre-training and curated fine-tuning data.. However, in data-sensitive fields such as healthcare, the lack of high-quality, domain-specific training corpus hinders LLMs' adaptation for specialized applications..

Meanwhile, domain experts have distilled domain wisdom into ontology rules, which formalize relationships among concepts and ensure the integrity of knowledge management repositories.. Viewing LLMs as implicit repositories of human knowledge, we propose Evontree, a novel framework that leverages a small set of high-quality ontology rules to systematically extract, validate, and enhance domain knowledge within LLMs, without requiring extensive external datasets.. Specifically, Evontree extracts domain ontology from raw models, detects inconsistencies using two core ontology rules, and reinforces the refined knowledge via self-distilled fine-tuning..

Extensive experiments on medical QA benchmarks with Llama3-8B-Instruct and Med42-v2 demonstrate consistent outperformance over both unmodified models and leading supervised baselines, achieving up to a 3.7% improvement in accuracy.. These results confirm the effectiveness, efficiency, and robustness of our approach for low-resource domain adaptation of LLMs..

---

## 5. Normative Reasoning in Large Language Models: A Comparative Benchmark
  from Logical and Modal Perspectives

🧠 **Category:** CS.AI | 📅 **Published:** October 30, 2025 | 🔥 **Score:** 25 points

**Authors:** Kentaro Ozeki, Risako Ando, Takanobu Morishita et al. (+3 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2510.26606v1) | [PDF Download](https://arxiv.org/pdf/2510.26606v1.pdf)

Normative reasoning is a type of reasoning that involves normative or deontic modality, such as obligation and permission.. While large language models (LLMs) have demonstrated remarkable performance across various reasoning tasks, their ability to handle normative reasoning remains underexplored..

In this paper, we systematically evaluate LLMs' reasoning capabilities in the normative domain from both logical and modal perspectives.. Specifically, to assess how well LLMs reason with normative modals, we make a comparison between their reasoning with normative modals and their reasoning with epistemic modals, which share a common formal structure.. To this end, we introduce a new dataset covering a wide range of formal patterns of reasoning in both normative and epistemic domains, while also incorporating non-formal cognitive factors that influence human reasoning.. Our results indicate that, although LLMs generally adhere to valid reasoning patterns, they exhibit notable inconsistencies in specific types of normative reasoning and display cognitive biases similar to those observed in psychological studies of human reasoning..

These findings highlight challenges in achieving logical consistency in LLMs' normative reasoning and provide insights for enhancing their reliability.. All data and code are released publicly at https://github.com/kmineshima/NeuBAROCO..

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

*Next edition: November 07, 2025*
