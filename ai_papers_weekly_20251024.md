# 🤖 Top 5 AI Papers This Week
## Week of October 24, 2025

Welcome to this week's roundup of the most impactful AI research papers! These papers have been generating buzz across Reddit, academic Twitter, and research communities.

**📊 This Week's Stats:**
- 📄 **5 featured papers** from **1 categories**  
- 👥 **28 contributing authors**
- 🔥 **Average engagement score:** 25.0
- 🏆 **Highest scorer:** 25 points

---

## 1. Empathic Prompting: Non-Verbal Context Integration for Multimodal LLM
  Conversations

🧠 **Category:** CS.AI | 📅 **Published:** October 23, 2025 | 🔥 **Score:** 25 points

**Authors:** Lorenzo Stacchio, Andrea Ubaldi, Alessandro Galdelli et al. (+3 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2510.20743v1) | [PDF Download](https://arxiv.org/pdf/2510.20743v1.pdf)

We present Empathic Prompting, a novel framework for multimodal human-AI interaction that enriches Large Language Model (LLM) conversations with implicit non-verbal context.. The system integrates a commercial facial expression recognition service to capture users' emotional cues and embeds them as contextual signals during prompting..

Unlike traditional multimodal interfaces, empathic prompting requires no explicit user control; instead, it unobtrusively augments textual input with affective information for conversational and smoothness alignment.. The architecture is modular and scalable, allowing integration of additional non-verbal modules.. We describe the system design, implemented through a locally deployed DeepSeek instance, and report a preliminary service and usability evaluation (N=5)..

Results show consistent integration of non-verbal input into coherent LLM outputs, with participants highlighting conversational fluidity.. Beyond this proof of concept, empathic prompting points to applications in chatbot-mediated communication, particularly in domains like healthcare or education, where users' emotional signals are critical yet often opaque in verbal exchanges..

---

## 2. User Perceptions of Privacy and Helpfulness in LLM Responses to
  Privacy-Sensitive Scenarios

🧠 **Category:** CS.AI | 📅 **Published:** October 23, 2025 | 🔥 **Score:** 25 points

**Authors:** Xiaoyuan Wu, Roshni Kaushik, Wenkai Li et al. (+2 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2510.20721v1) | [PDF Download](https://arxiv.org/pdf/2510.20721v1.pdf)

Large language models (LLMs) have seen rapid adoption for tasks such as drafting emails, summarizing meetings, and answering health questions.. In such uses, users may need to share private information (e.g., health records, contact details)..

To evaluate LLMs' ability to identify and redact such private information, prior work developed benchmarks (e.g., ConfAIde, PrivacyLens) with real-life scenarios.. Using these benchmarks, researchers have found that LLMs sometimes fail to keep secrets private when responding to complex tasks (e.g., leaking employee salaries in meeting summaries).. However, these evaluations rely on LLMs (proxy LLMs) to gauge compliance with privacy norms, overlooking real users' perceptions.. Moreover, prior work primarily focused on the privacy-preservation quality of responses, without investigating nuanced differences in helpfulness.. To understand how users perceive the privacy-preservation quality and helpfulness of LLM responses to privacy-sensitive scenarios, we conducted a user study with 94 participants using 90 scenarios from PrivacyLens.. We found that, when evaluating identical responses to the same scenario, users showed low agreement with each other on the privacy-preservation quality and helpfulness of the LLM response.. Further, we found high agreement among five proxy LLMs, while each individual LLM had low correlation with users' evaluations.. These results indicate that the privacy and helpfulness of LLM responses are often specific to individuals, and proxy LLMs are poor estimates of how real users would perceive these responses in privacy-sensitive scenarios..

Our results suggest the need to conduct user-centered studies on measuring LLMs' ability to help users while preserving privacy.. Additionally, future research could investigate ways to improve the alignment between proxy LLMs and users for better estimation of users' perceived privacy and utility..

---

## 3. Plan Then Retrieve: Reinforcement Learning-Guided Complex Reasoning over
  Knowledge Graphs

🧠 **Category:** CS.AI | 📅 **Published:** October 23, 2025 | 🔥 **Score:** 25 points

**Authors:** Yanlin Song, Ben Liu, Víctor Gutiérrez-Basulto et al. (+5 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2510.20691v1) | [PDF Download](https://arxiv.org/pdf/2510.20691v1.pdf)

Knowledge Graph Question Answering aims to answer natural language questions by reasoning over structured knowledge graphs.. While large language models have advanced KGQA through their strong reasoning capabilities, existing methods continue to struggle to fully exploit both the rich knowledge encoded in KGs and the reasoning capabilities of LLMs, particularly in complex scenarios..

They often assume complete KG coverage and lack mechanisms to judge when external information is needed, and their reasoning remains locally myopic, failing to maintain coherent multi-step planning, leading to reasoning failures even when relevant knowledge exists.. We propose Graph-RFT, a novel two-stage reinforcement fine-tuning KGQA framework with a 'plan-KGsearch-and-Websearch-during-think' paradigm, that enables LLMs to perform autonomous planning and adaptive retrieval scheduling across KG and web sources under incomplete knowledge conditions.. Graph-RFT introduces a chain-of-thought fine-tuning method with a customized plan-retrieval dataset activates structured reasoning and resolves the GRPO cold-start problem.. It then introduces a novel plan-retrieval guided reinforcement learning process integrates explicit planning and retrieval actions with a multi-reward design, enabling coverage-aware retrieval scheduling..

It employs a Cartesian-inspired planning module to decompose complex questions into ordered subquestions, and logical expression to guide tool invocation for globally consistent multi-step reasoning.. This reasoning retrieval process is optimized with a multi-reward combining outcome and retrieval specific signals, enabling the model to learn when and how to combine KG and web retrieval effectively..

---

## 4. The Shape of Reasoning: Topological Analysis of Reasoning Traces in
  Large Language Models

🧠 **Category:** CS.AI | 📅 **Published:** October 23, 2025 | 🔥 **Score:** 25 points

**Authors:** Xue Wen Tan, Nathaniel Tan, Galen Lee et al. (+1 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2510.20665v1) | [PDF Download](https://arxiv.org/pdf/2510.20665v1.pdf)

Evaluating the quality of reasoning traces from large language models remains understudied, labor-intensive, and unreliable: current practice relies on expert rubrics, manual annotation, and slow pairwise judgments.. Automated efforts are dominated by graph-based proxies that quantify structural connectivity but do not clarify what constitutes high-quality reasoning; such abstractions can be overly simplistic for inherently complex processes..

We introduce a topological data analysis (TDA)-based evaluation framework that captures the geometry of reasoning traces and enables label-efficient, automated assessment.. In our empirical study, topological features yield substantially higher predictive power for assessing reasoning quality than standard graph metrics, suggesting that effective reasoning is better captured by higher-dimensional geometric structures rather than purely relational graphs.. We further show that a compact, stable set of topological features reliably indicates trace quality, offering a practical signal for future reinforcement learning algorithms..

---

## 5. Why Did Apple Fall To The Ground: Evaluating Curiosity In Large Language
  Model

🧠 **Category:** CS.AI | 📅 **Published:** October 23, 2025 | 🔥 **Score:** 25 points

**Authors:** Haoyu Wang, Sihang Jiang, Yuyan Chen et al. (+2 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2510.20635v1) | [PDF Download](https://arxiv.org/pdf/2510.20635v1.pdf)

Curiosity serves as a pivotal conduit for human beings to discover and learn new knowledge.. Recent advancements of large language models (LLMs) in natural language processing have sparked discussions regarding whether these models possess capability of curiosity-driven learning akin to humans..

In this paper, starting from the human curiosity assessment questionnaire Five-Dimensional Curiosity scale Revised (5DCR), we design a comprehensive evaluation framework that covers dimensions such as Information Seeking, Thrill Seeking, and Social Curiosity to assess the extent of curiosity exhibited by LLMs.. The results demonstrate that LLMs exhibit a stronger thirst for knowledge than humans but still tend to make conservative choices when faced with uncertain environments..

We further investigated the relationship between curiosity and thinking of LLMs, confirming that curious behaviors can enhance the model's reasoning and active learning abilities.. These findings suggest that LLMs have the potential to exhibit curiosity similar to that of humans, providing experimental support for the future development of learning capabilities and innovative research in LLMs..

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

*Next edition: October 31, 2025*
