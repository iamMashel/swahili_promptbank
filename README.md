# 🇰🇪 Swahili PromptBank

A curated collection of 200+ high-quality Swahili prompts designed to improve the alignment, evaluation, and training of large language models (LLMs) in low-resource languages.

---

## 🌍 About

**Swahili PromptBank** is an open-source dataset of culturally relevant, linguistically accurate prompts written in Swahili. This project aims to enhance representation and model performance in Swahili by providing carefully reviewed prompts across a range of NLP tasks.

Each prompt is crafted to:
- Match natural Swahili tone and context
- Reflect culturally appropriate scenarios
- Be clear, instructive, and useful for alignment training

---

## 📦 Dataset Structure

```

swahili-promptbank/
├── prompts/
│   ├── classification/
│   ├── summarization/
│   ├── instruction-following/
│   └── conversational/
├── examples/
│   └── model\_responses\_comparison.md
├── scripts/
│   └── validation\_utils.py
├── README.md
└── CONTRIBUTING.md

````

---

## 🧠 Prompt Types

| Task Type             | Description |
|-----------------------|-------------|
| `instruction-following` | Prompts where the model is guided to complete a task, e.g., "Explain how to cook ugali." |
| `summarization`         | Prompts asking for summaries of Swahili text or stories |
| `classification`        | Prompts for categorizing emotions, topics, or sentiment in Swahili |
| `conversational`        | Roleplay and dialogue-style prompts in a Swahili cultural context |

---

## 🧪 Sample Prompt

```json
{
  "task": "instruction-following",
  "language": "Swahili",
  "prompt": "Eleza jinsi ya kupika ugali kwa mtu ambaye hajawahi kufanya hivyo.",
  "expected_output": "Hatua kwa hatua za kupika ugali, zikielezwa kwa lugha rahisi."
}
````

---

## ✅ Quality Criteria

All prompts were:

* **Peer-reviewed** for tone and clarity
* Designed with **cultural alignment** in mind
* Written in **native Swahili** without code-switching
* Labeled with clear metadata for task type and usage

---

## 📈 Use Cases

* Fine-tuning multilingual language models
* Alignment and safety training in Swahili
* Benchmarking model performance on East African language tasks
* Educational tools and datasets for Swahili NLP

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](./CONTRIBUTING.md) for details on how to submit prompts or improvements.

---

## 📜 License

This project is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.  
You are free to use, share, and remix this dataset — as long as you give credit.

**Attribution format:**
> “Odera Mashel, creator of Swahili PromptBank (2025) — [GitHub](https://github.com/iamMashel)”

🔗 [Read the full license here](https://creativecommons.org/licenses/by/4.0/)


---

## ✨ Acknowledgments

This project is part of a broader effort to expand **low-resource language access** in AI.
Special thanks to Swahili speakers, cultural reviewers, and the alignment research community.

---

