# 🤝 Contributing to Swahili PromptBank

Thank you for your interest in contributing to Swahili PromptBank!  
This project exists to improve Swahili representation in AI through high-quality, culturally accurate prompt datasets.  
We welcome new prompt contributions, reviews, and improvements to documentation or tooling.

---

## ✍️ What You Can Contribute

### ✅ 1. Add New Prompts
- Write high-quality Swahili prompts for the following categories:
  - `instruction-following`
  - `classification`
  - `summarization`
  - `conversational`
- Follow the [Prompt Format Guidelines](#prompt-format-guidelines)

### ✅ 2. Improve or Review Existing Prompts
- Fix typos, grammar, or unclear instructions
- Suggest better wording for tone or cultural alignment

### ✅ 3. Improve Tooling or Docs
- Update Python scripts in `/scripts/`
- Improve `README.md`, `LICENSE`, or examples

---

## 🧾 Prompt Format Guidelines

All prompts should be submitted in `.json` format with this structure:

```json
{
  "task": "instruction-following",
  "language": "Swahili",
  "prompt": "Eleza jinsi ya kupika ugali kwa mtu ambaye hajawahi kufanya hivyo.",
  "expected_output": "Hatua kwa hatua za kupika ugali, zikielezwa kwa lugha rahisi."
}
````

**Tips:**

* Use clear, neutral Swahili (no slang or code-switching).
* Target real-world or culturally relevant scenarios.
* Avoid bias, stereotypes, or sensitive content.

---

## 🛠 How to Contribute

1. **Fork** the repository
2. **Create a new branch**
   Example: `feature/add-summarization-prompts`
3. **Make your changes**
   Add prompt files to the appropriate folder under `/prompts/`
4. **Commit your changes**
   Write clear commit messages
5. **Open a Pull Request**
   Describe your contribution clearly in the PR description

---

## 📢 Code of Conduct

We follow a respectful, inclusive contributor environment.
Please be kind and constructive in discussions and reviews.

---

## 🙏 Attribution

Contributors will be listed in the `README.md` and recognized in dataset releases.

---

## 💡 Questions or Suggestions?

Open an [issue](https://github.com/iamMashel/swahili-promptbank/issues) or start a discussion.
We’d love to hear your ideas!

---

Asante sana for supporting Swahili in AI. 🌍
