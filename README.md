
# Predicting Price Moves with News Sentiment (FNSPID)
## Project Overview
This project aims to analyze financial news and stock price movements using the **FNSPID dataset**. The ultimate goal is to leverage news sentiment to predict price moves, supporting **Nova Financial Solutions** in enhancing predictive analytics for **financial forecasting accuracy** and **operational efficiency**.

## Business Objective
- Improve **forecasting accuracy** by integrating sentiment signals with price-based features.
- Support **operational efficiency** through automated data ingestion, processing, and reporting.
- Deliver actionable insights for **event-driven and momentum strategies**.


## Executive Summary
This interim report outlines progress on analyzing financial news and stock price movements using the FNSPID dataset. The project goal is explicitly tied to Nova Financial Solutions' business objective: enhancing predictive analytics for financial forecasting accuracy and operational efficiency.

Week-1 work includes:
- **EDA on news headlines**
- **Technical analysis on stock data**
- **Initial sentiment correlation findings**


## Methodology
The methodology aligns with the FNSPID dataset and project scope, ensuring clarity and relevance:
- **Environment Setup:** Python virtual environment with `pandas`, `numpy`, `matplotlib`, `seaborn`, `TA-Lib`, and `TextBlob` installed.
- **Repository Structure:** Organized into `data/`, `notebooks/`, and `scripts/` folders for reproducibility.
- **Data Loading & Cleaning:** Imported FNSPID dataset, standardized column names, parsed timestamps, and handled missing values.
- **News EDA:** Analyzed headline lengths, publisher activity, keyword frequency, and publication trends.
- **Stock Analysis:** Applied technical indicators (SMA, EMA, RSI, MACD) and calculated performance metrics (Annualized Return, Volatility, Sharpe Ratio).
- **Sentiment Analysis:** Computed polarity scores for headlines using TextBlob, aggregated daily sentiment, and merged with stock returns.
- **Correlation Analysis:** Calculated Pearson correlation between sentiment scores and daily returns for each ticker.

## Findings
### **Task 1: News EDA**
- Headlines are concise (40–100 characters).
- Publisher activity is concentrated, with **Benzinga Newsdesk** and **Paul Quintaro** dominating.
- Publication surged post-2019, peaking in 2020.
- Keywords like *stocks*, *market*, and *earnings* dominate, indicating strong equity market focus.

### **Task 2: Stock Technical Analysis**
- **AAPL** shows a strong upward trend from 2010–2024, confirmed by SMA and EMA.
- RSI oscillates between 30–70, signaling overbought/oversold conditions.
- MACD divergences highlight trend reversals during volatility spikes.
- **NVDA** leads in returns (~60%) but with high volatility (~45%).
- Sharpe ratios >1.2 for AAPL and NVDA indicate strong risk-adjusted performance.

### **Task 3: Sentiment Correlation Analysis**
- Initial sentiment analysis using TextBlob shows polarity scores mostly between -0.2 and 0.3.
- Correlation between daily sentiment and returns is weak overall (close to zero).
- META and NVDA exhibit slight positive correlation during high-volatility periods.
- Suggests sentiment alone is insufficient for predicting daily returns but may complement other signals.


## Repository Structure
```bash
fnspid/
├─ data/                     # Raw and processed datasets
├─ github/                   # GitHub workflows or related configs
├─ notebooks/                # Jupyter notebooks for analysis
│   ├─ __init__.py
│   ├─ correlation_analysis.ipynb      # Sentiment vs stock returns correlation
│   ├─ descriptive_analysis_eda.ipynb  # News EDA and descriptive statistics
│   ├─ quant_analysis.ipynb            # Stock technical indicators and metrics
│   └─ sentiment_stock_correlation.xlsx # Exported correlation results
├─ scripts/                  # Reserved for reusable scripts (currently empty)
├─ src/                      # Source code for data processing and utilities
│   ├─ __init__.py
│   ├─ data_cleaner.py       # Functions for cleaning datasets
│   ├─ data_load.py          # Data loading utilities
│   └─ data_loader.py        # Additional loader functions
├─ tests/                    # Unit tests for scripts and modules
├─ venv/                     # Virtual environment (excluded via .gitignore)
├─ vscode/                   # VS Code workspace settings
├─ .gitignore                # Ignore rules for unnecessary files
├─ README.md                 # Project documentation
└─ requirements.txt          # Python dependencies
```

## Setup & Installation
```bash
# 1) Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# .venv\Scripts\activate        # Windows

# 2) Install dependencies
pip install -r requirements.txt

# Optional: TA-Lib (if available in your environment)
# pip install TA-Lib
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