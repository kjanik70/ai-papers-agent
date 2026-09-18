# 🤖 Top 5 AI Papers This Week
## Week of September 18, 2026

Welcome to this week's roundup of the most impactful AI research papers! These papers have been generating buzz across Reddit, academic Twitter, and research communities.

**📊 This Week's Stats:**
- 📄 **5 featured papers** from **2 categories**  
- 👥 **27 contributing authors**
- 🔥 **Average engagement score:** 25.0
- 🏆 **Highest scorer:** 25 points

---

## 1. Harm Laundering in GPT Models: Evidence That Gender Discrimination Is Transformed Rather Than Reduced Across Safety-Trained Generations

🧠 **Category:** CS.AI | 📅 **Published:** September 17, 2026 | 🔥 **Score:** 25 points

**Authors:** Sarah Wyer, Sue Black, Noura Al Moubayed

**Links:** [ArXiv Paper](https://arxiv.org/abs/2609.20779v1) | [PDF Download](https://arxiv.org/pdf/2609.20779v1.pdf)

Safety evaluations for large language models rely on surface-form classifiers that report declining harm scores across model generations.. We provide evidence that this methodology is systematically incomplete: explicit discriminatory content is transformed rather than removed..

We call this \emph{harm laundering}.. Analysing 450,000 gender-directed completions across 15 models spanning GPT-2 through to GPT-5 (OpenAI GPT lineage; three demographic conditions), we show that sexual violence clusters prevalent in GPT-2 women-directed output disappear by GPT-4, while men-directed completions gain positive representational territory (caregiving, emotional range, ally identity) that women-directed completions do not.. The pattern is most visible at GPT-5: Topic~5 (1,997~documents) frames breast cancer as a men's rights debate, while zero equivalent clusters appear in women-directed output.. Three independent classifiers score this content as non-toxic.. Sentiment scores invert at GPT-4: early models demean women; later models over-correct.. Topic diversity in women-directed completions falls 36\% relative to men at the GPT-4 alignment boundary (W/M~$= 0.58$, from $0.91$ at GPT-2).. REGARD representational harm disparity correlates with release date ($ρ= +0.55$, $p = .034$) while Detoxify does not ($ρ= -0.23$, $p = .42$): toxicity scores fall as representational harm grows..

We formalise harm laundering as a three-criteria test and provide a three-stage detection protocol applicable to any generative model.. Within the OpenAI GPT lineage, toxicity score reduction is not a sufficient proxy for harm reduction..

---

## 2. Fingerprinting Multimodal Large Language Models

🧠 **Category:** CS.AI | 📅 **Published:** September 17, 2026 | 🔥 **Score:** 25 points

**Authors:** Chao Huang, Meng Tong, Kejiang Chen

**Links:** [ArXiv Paper](https://arxiv.org/abs/2609.20457v1) | [PDF Download](https://arxiv.org/pdf/2609.20457v1.pdf)

While multimodal large language models (MLLMs) enable a wide range of image-text reasoning tasks, recent incidents indicate that they are vulnerable to illicit deployment and unauthorized distillation.. Existing solutions for model provenance are typically confounded by shared language backbones in MLLMs and struggle to detect violations of distillation..

To bridge this gap and safeguard model ownership, we present the first study on multimodal model fingerprinting.. Inspired by recent findings that self-attention acts as a low-pass filter and that its low-frequency components are informative, we develop AttnPrint for white-box provenance.. Specifically, we extract cross-modal attention distributions and isolate their low-frequency components to serve as model fingerprints.. To facilitate black-box auditing, we further introduce DistillTrace, which employs hypothesis testing of MLLM outputs to identify potential model infringement.. We conduct extensive experiments on 154 model instances across 19 multimodal architectures..

Notably, AttnPrint achieves strong derivative-model detection performance while remaining robust to five downstream modification techniques.. DistillTrace also provides evidence of distillation relationships under three parameter-independent techniques..

---

## 3. KoNeoBench: A Curated Evaluation Dataset for LLM Understanding of Korean Neologisms

🧠 **Category:** CS.AI | 📅 **Published:** September 17, 2026 | 🔥 **Score:** 25 points

**Authors:** Soha Lee, Soojin Lee, Heesung Yang et al. (+8 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2609.19916v1) | [PDF Download](https://arxiv.org/pdf/2609.19916v1.pdf)

Large language models (LLMs) are typically evaluated on static benchmarks, even though natural language constantly evolves through newly emerging words and meanings.. Existing Korean benchmarks are centered on established vocabulary and therefore provide limited coverage of such recent lexical change, and their English-oriented design makes it difficult to assess the typological properties of Korean, in which content words combine productively with functional morphemes..

In this paper, we introduce KoNeoBench, a benchmark for evaluating LLMs' understanding of Korean neologisms.. KoNeoBench is built on 1,785 Korean neologisms attested in online news since 2020 and curated through expert lexicographic review.. Each entry provides usage examples, word-formation analyses, and dictionary-style definitions.. Based on this resource, we define four tasks and report results on recent models, together with a human baseline.. Our experiments show that current LLMs exhibit clear limitations in recovering source components, distinguishing semantic categories, and generating accurate definitions..

These results reveal specific aspects of recent Korean lexical change that remain challenging for current LLMs.. KoNeoBench is available at https://github.com/bcmilab/ko-neobench/ ..

---

## 4. PetriBench: Benchmarking LLM Reasoning over Dynamic State Spaces

🧠 **Category:** CS.AI | 📅 **Published:** September 17, 2026 | 🔥 **Score:** 25 points

**Authors:** Pyrros Koussios, Benjamin Jäger, John Hua Yao et al. (+3 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2609.19883v1) | [PDF Download](https://arxiv.org/pdf/2609.19883v1.pdf)

Characterizing LLM reasoning remains an open challenge, as many existing benchmarks isolate specific reasoning skills, rely on external knowledge, or are costly to extend.. We introduce PetriBench, a compact, fully self-contained, and scalable benchmark for evaluating LLM reasoning over dynamic state spaces using Petri nets, a mature formalism for modeling real-world concurrent and distributed systems..

PetriBench organizes reasoning into four task families varying by scope and temporal horizon, with Easy, Medium, and Hard levels generated by increasing structural complexity and evaluated against exact ground truth.. Across a diverse set of proprietary and open-weight models, accuracy decreases consistently with difficulty, while harder instances expose increasingly distinct task-specific capability profiles..

Additional analyses show that test-time compute improves performance but interacts differently with different reasoning tasks, and that procedural generation yields smooth scaling with structural complexity.. Together, these results show that PetriBench provides a unified and extensible setting for probing the strengths, limits, and scaling behavior of LLM reasoning..

---

## 5. Digital Twins for Opinion Dynamics: A Generative LLM Framework for Social Networks

📈 **Category:** CS.LG | 📅 **Published:** September 17, 2026 | 🔥 **Score:** 25 points

**Authors:** Omran Berjawi, Giuseppe Fenza, Rida Khatoun et al. (+1 more)

**Links:** [ArXiv Paper](https://arxiv.org/abs/2609.19913v1) | [PDF Download](https://arxiv.org/pdf/2609.19913v1.pdf)

The study of opinion dynamics in social networks is one of the key challenges in computational social science with direct relevance to understanding political polarization, misinformation, and health responses.. Current approaches focus on simplified mathematical models that ignore linguistic and contextual factors related to belief updates or use Large Language Model (LLM)-based simulations that have not been validated against real data..

We present a framework based on the concept of a digital twin to simulate opinion dynamics in social networks.. The approach fills the gap by cloning a real-world Twitter network, assigns a set of attributes for agents (such as persona, emotions, centrality, stubbornness, and influence), and employs Mistral-7B to perform opinion update based on memory and social exposure.. To evaluate the proposed approach, we validate it against two real Twitter datasets (COVID-19 discourse and U.S elections 2020).. The results show that the capability of the proposed framework reproduces opinion trajectories and reduces individual prediction error by more than 50% compared to the best-performing classical baseline (Mistral-7B achieves Mean Absolute Error (MAE) = 0.150 and 0.121 on the COVID-19 and US Election 2020 datasets, respectively).. We observe similar improvements in structural alignment (Delta_r = 0.120 and 0.180) and polarization dynamics (Delta_Var = 0.106 and 0.115) on the two datasets, respectively..

Additionally, the ablation studies confirm that agent attributes, memory, and social exposure all contribute to the framework's predictive fidelity in reproducing opinion trajectories, with agent attributes being the most critical contributor.. Overall, our results demonstrate that grounding Mistral-7B within empirically cloned interaction networks produces a realistic simulation framework capable of reproducing complex social dynamics..

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

*Next edition: September 25, 2026*
