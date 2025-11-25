# NOVA-FINANCIAL-SOLUTIONS-WEEK1  
**Predicting Stock Price Movements Using News Sentiment (FNSPID Dataset)**
## Project Overview
This repository contains **Week 1 deliverables** for analyzing the relationship between financial news sentiment and stock price movements using the **FNSPID (Financial News and Stock Price Integration Dataset)**.

The core objective is to determine whether news headline sentiment can serve as a predictive signal — alone or in combination with technical indicators — to improve short-term price forecasting accuracy.

## Business Value (Nova Financial Solutions)
- Enhance **predictive analytics** capabilities
- Support **event-driven** and **momentum-based** trading strategies
- Build a **reproducible, scalable analytics pipeline**

## Week 1 Accomplishments
- Exploratory Data Analysis (EDA) on 1.9M+ financial news headlines
- Technical analysis on major tickers (AAPL, NVDA, META, etc.)
- Initial sentiment scoring and correlation analysis with daily returns

## Key Findings (Week 1)
- News volume surged after 2019, peaking in 2020
- Top publishers: **Benzinga Newsdesk**, **Paul Quintaro**
- Dominant keywords: *stocks, earnings, shares, market*
- Strong long-term uptrends in **AAPL** and **NVDA** confirmed by SMA/EMA
- **NVDA** delivers highest returns (~60% annualized) but with high volatility (~45%)
- Daily sentiment–return correlation is **weak overall (~0 to ±0.08)**
- Slight positive correlation observed in **META** and **NVDA** during high-volatility periods → sentiment may act as a **complementary signal**

## Repository Structure
```bash
NOVA-FINANCIAL-SOLUTIONS-WEEK1/
├─ data/                     # Raw & processed data (not tracked in Git)
├─ github/                   # GitHub Actions / workflows
├─ notebooks/                # Week 1 Jupyter notebooks
│   ├─ __init__.py
│   ├─ correlation_analysis.ipynb
│   ├─ eda_analysis.ipynb
│   ├─ publisher_analysis.ipynb
│   ├─ quant_analysis.ipynb
│   ├─ text_analysis.ipynb
│   └─ time_series_analysis.ipynb
├─ scripts/                  # Automation scripts (future use)
│   ├─ __init__.py
│   └─ README.md
├─ src/                      # Reusable source code
│   ├─ __pycache__/
│   ├─ __init__.py
│   ├─ eda_processor.py
│   └─ README.md
├─ tests/                    # Unit tests (to be implemented)
├─ venv/                     # Virtual environment (gitignored)
├─ vscode/                   # VS Code settings
├─ .gitignore
├─ .settings.json
├─ LICENSE
├─ README.md                 # This file
├─ requirements.txt
└─ requirements.txt.txt      # (duplicate – can be deleted)



## Setup & Installation
```bash
# Clone repository
git clone https://github.com/gashawbekele06/NOVA-FINANCIAL-SOLUTIONS-WEEK1.git
cd NOVA-FINANCIAL-SOLUTIONS-WEEK1

# Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt
```

## Dependencies
- pandas, numpy, matplotlib, seaborn
- textblob (and/or nltk + vaderSentiment)
- openpyxl for Excel I/O
- python-docx for automated Word report generation
- TA-Lib (optional for technical indicators)


## Contributing
Contributions are welcome! A suggested contributing workflow:
1. Fork the repository.
2. Create a branch: git checkout -b feat/your-feature
3. Make changes, run tests, and ensure linter passes.
4. Submit a pull request describing your changes.

Add any repository-specific guidelines:
- Commit message format
- Branch naming conventions
- Issue templates or PR templates

## License

Specify the license used by this repository (e.g., MIT, Apache-2.0). Example:

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Contact

Maintainer: Gashaw Bekele (gashawbekele06 on GitHub)