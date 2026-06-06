<div align="center">

# 🖼️ Digital Image Processing

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![uv](https://img.shields.io/badge/uv-package%20manager-DE5FE9?style=for-the-badge&logo=python&logoColor=white)](https://docs.astral.sh/uv/)
[![License](https://img.shields.io/badge/License-All%20Rights%20Reserved-red?style=for-the-badge)](./LICENSE)
[![University](https://img.shields.io/badge/BS%20Software%20Engineering-UAF-006400?style=for-the-badge&logo=academia&logoColor=white)](https://uaf.edu.pk)

> *Implementations of classical and modern Digital Image Processing techniques — built from scratch with Python.*

</div>

---

## 📌 Overview

This repository contains hands-on implementations of **Digital Image Processing** concepts covered in the DIP course. Each script corresponds to specific textbook exercises or lab tasks, covering topics from basic intensity transformations to advanced spatial and frequency domain filtering.

All experiments are written in **Python**, managed with the blazing-fast **`uv`** package manager for reproducibility and ease of setup.

---

## 📂 Repository Structure

```
digital_image_processing/
│
├── 1_3and1_4.py           # Chapter 1 — Exercises 1.3 & 1.4
├── ...                    # More exercises per chapter
├── images/                # Sample input images used in scripts
├── outputs/               # Generated output images (auto-created)
├── pyproject.toml         # Project metadata & dependencies (uv)
├── uv.lock                # Locked dependency versions
└── README.md
```

> 📝 File naming convention follows the pattern `chapter_exercise.py` — for example, `1_3and1_4.py` covers exercises 1.3 and 1.4 from Chapter 1.

---

## 🧪 Topics Covered

| # | Topic |
|---|-------|
| 1 | Image fundamentals & pixel operations |
| 2 | Intensity transformations & spatial filtering |
| 3 | Histogram processing & equalization |
| 4 | Smoothing & sharpening filters |
| 5 | Frequency domain filtering (DFT, FFT) |
| 6 | Image restoration & noise models |
| 7 | Morphological image processing |
| 8 | Image segmentation & thresholding |

---

## ⚡ Quick Start

### Prerequisites

- **Python 3.10+** — [Download here](https://python.org/downloads)
- **uv** — Ultra-fast Python package manager

Install `uv` if you don't have it:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

### 🚀 Setup & Run

**Step 1 — Clone the repository**

```bash
git clone https://github.com/Uzair-Waseem-390/digital_image_processing.git
cd digital_image_processing
```

**Step 2 — Install dependencies**

```bash
uv sync
```

This will automatically create a virtual environment and install all required packages from `pyproject.toml`.

**Step 3 — Run any script**

```bash
uv run <file_name.py>
```

**Example:**

```bash
uv run 1_3and1_4.py
```

---

## 📖 Usage Examples

```bash
# Chapter 1 exercises
uv run 1_3and1_4.py

# Run any other exercise file the same way
uv run <chapter>_<exercise>.py
```

> 💡 **Tip:** Each script is self-contained. Just run it — input images are loaded from the `images/` folder, and outputs are saved to `outputs/` automatically.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `Python 3.10+` | Core language |
| `OpenCV` | Image I/O and processing |
| `NumPy` | Array & matrix operations |
| `Matplotlib` | Visualization & plotting |
| `uv` | Dependency & environment management |

---

## 🤝 Contributing

This is a personal academic project, but feel free to fork it, open issues, or suggest improvements via pull requests.

1. Fork the repo
2. Create your branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 👨‍💻 Author

<div align="center">

**Uzair Waseem**
Backend Developer | BS Software Engineering @ University of Agriculture, Faisalabad

[![GitHub](https://img.shields.io/badge/GitHub-Uzair--Waseem--390-0A0A0A?style=flat-square&logo=github&logoColor=white)](https://github.com/Uzair-Waseem-390)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-uzair--waseem--digital-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/uzair-waseem-digital/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-FF5733?style=flat-square&logo=vercel&logoColor=white)](https://portfolio-five-opal-76.vercel.app/)

</div>

---

<div align="center">

**Rights Reserved © 2026 Uzair Waseem**

*Designed with precision. Built with purpose.*

</div>