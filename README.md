# Personal Key Indicators of Heart Disease

**Exploratory data analysis in R and Python, with a reproducible logistic-regression evaluation.**

This collaborative educational project explores associations between survey responses and self-reported heart-disease history. It uses a cleaned dataset derived from the US **2020 Behavioral Risk Factor Surveillance System (BRFSS)**.

> **Important:** This is an educational data-science exercise, **not** a medical screening or diagnostic tool. Survey associations do not establish causation, and the model has not been clinically validated.

## Project at a glance

| | |
| --- | --- |
| **Data** | 319,795 survey records, 18 columns |
| **Tools** | R, R Markdown, tidyverse, Python, pandas, scikit-learn, matplotlib, seaborn |
| **EDA** | Data quality checks, descriptive summaries, distributions and visualizations |
| **Model experiment** | Logistic regression with train-only preprocessing and held-out evaluation |
| **Focus** | Reproducibility, class imbalance, correct interpretation of model metrics |

## Data and provenance

- Dataset: [Personal Key Indicators of Heart Disease](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease), published by Kamil Pytlak on Kaggle; its cleaned CSV is derived from **BRFSS 2020**.
- Input file: `heart_2020_cleaned.csv`.
- Target: `HeartDisease` (`Yes` / `No`), representing a survey response rather than an independently confirmed clinical diagnosis.
- **27,373 `Yes` records (8.56%)** and **292,422 `No` records (91.44%)**.
- The supplied file has **no missing field values**. Exactly repeated response combinations can occur in survey data; they should not be assumed to be duplicate people.

See [about_data.md](about_data.md) for a short dataset overview. Source preprocessing is documented in the [upstream notebook](https://github.com/kamilpytlak/data-science-projects/blob/main/heart-disease-prediction/2022/notebooks/data_processing.ipynb).

## Repository structure

| Path | Purpose |
| --- | --- |
| `heart.Rmd` | Collaborative R-based exploratory analysis and visualizations |
| `heart.html`, `heart-Max.html` | Historical HTML exports of the R analysis |
| `Andrei_Aliseiko.py`, `Andrei_Aliseiko.html` | Original collaborator's Python exploration and exported report |
| `analysis/evaluate_model.py` | **New** reproducible classification evaluation; does not overwrite original analysis |
| `reports/model_metrics.json` | Results reproduced from the full supplied dataset |
| `tests/test_evaluate_model.py` | Fast tests using synthetic observations |
| `heart_2020_cleaned.csv` | Dataset used by the project |
| `*.png` | Historical visualization exports; interpret with the limitations below |

## Reproduce the model evaluation (Python)

Requires Python 3.10+ and the dataset file at the repository root.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
pytest -q
python analysis/evaluate_model.py
```

The last command creates or refreshes `reports/model_metrics.json`. For a quick **smoke test only**, use:

```bash
python analysis/evaluate_model.py --sample 4000 --output /tmp/heart-smoke-metrics.json
```

The script uses an **80/20 stratified holdout** (`random_state=42`). A scikit-learn `Pipeline` fits numeric standardization and categorical one-hot encoding **on training data only**. It compares a majority-class baseline with ordinary and class-weighted logistic regression. No automatic removal of valid survey responses as "outliers" is performed.

### Reproduced results on all 319,795 records

| Test-set metric | Predict all `No` | Logistic regression | Balanced logistic regression |
| --- | ---: | ---: | ---: |
| Accuracy | 91.44% | 91.65% | 74.87% |
| Precision (`Yes`) | 0% | 56.48% | 22.23% |
| Recall (`Yes`) | 0% | 10.74% | 77.48% |
| F1 (`Yes`) | 0.000 | 0.180 | 0.345 |
| ROC-AUC | — | 0.837 | 0.837 |
| Average precision | — | 0.349 | 0.348 |

These figures were reproduced with Python, pandas and scikit-learn on a **63,959-row held-out test set** and are recorded in [`reports/model_metrics.json`](reports/model_metrics.json). The models use default probability thresholds. Class weighting improves recall but also substantially raises false-positive counts. **Accuracy alone is misleading** because only 8.56% of the records have the positive label. These figures are illustrative in-sample-dataset results, not evidence of suitability for healthcare decisions.

## Explore the original R analysis

Open `heart.Rmd` in RStudio. Install packages if missing:

```r
install.packages(c("tidyverse", "rstatix", "rmarkdown"))
rmarkdown::render("heart.Rmd")
```

Run it from the repository directory so the relative path to `heart_2020_cleaned.csv` resolves. The R report has **not** been independently rerun in a clean environment as part of the November 2026 review; the committed HTML files remain historical exports until regenerated.

The original `Andrei_Aliseiko.py` remains available for historical context. Its exploratory IQR filtering, integer-label encoding of nominal categories and unevaluated classifier are **not** the recommended model-evaluation workflow. Prefer the separate `analysis/evaluate_model.py` experiment for reproducible comparisons.

## Limitations

- The dataset is observational and self-reported; the project does not establish causal effects.
- Historical bar plots often show **raw counts**, not within-group disease rates.
- Categorical correlations in the historical Python analysis used arbitrary integer codes and should not be interpreted as effect sizes.
- Some historical IQR-based descriptive plots remove plausible self-reported observations; compare against the original data.
- The evaluation is a single train/test split, **not** cross-validation or external validation. Survey records do not include individual identifiers to assess respondent-level duplication.
- No clinical assessment, subgroup fairness evaluation or calibrated deployment workflow has been performed.

## Collaboration and attribution

This is a **team project**. GitHub's repository history records multiple contributors. The R Markdown file names **Janek Ciarka** as its author, while the historical Python analysis is in `Andrei_Aliseiko.py`. Do not infer sole authorship of the entire repository from one file; individual contributions should be attributed accurately. The later reproducibility/evaluation improvements are documented as separate commits.

## Licensing

The repository contains a **GNU GPL-3.0** software license. Third-party dataset, notebook, and generated-report reuse rights may differ; verify their terms before redistribution. The Kaggle dataset and its upstream processing work are credited above.
