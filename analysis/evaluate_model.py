"""Reproducible, educational baseline evaluation for the BRFSS 2020 dataset.

This is a separate experiment; it does not alter the original collaborative
R/Python analyses. It is not a clinical risk model.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    balanced_accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "heart_2020_cleaned.csv"
DEFAULT_OUTPUT = ROOT / "reports" / "model_metrics.json"
TARGET = "HeartDisease"


def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    if TARGET not in df.columns:
        raise ValueError(f"Missing target column: {TARGET}")
    if df.empty:
        raise ValueError("The input dataset is empty")
    if df[TARGET].isna().any() or not df[TARGET].isin(["No", "Yes"]).all():
        raise ValueError("HeartDisease must contain only 'No' and 'Yes' (no missing values)")
    if df[TARGET].nunique() != 2:
        raise ValueError("Both target classes are required")
    if df.drop(columns=[TARGET]).isna().any().any():
        raise ValueError("Missing predictor values: add a train-only imputer before fitting")
    return df


def build_model(features: pd.DataFrame, *, balance_classes: bool = False) -> Pipeline:
    numeric = features.select_dtypes(include="number").columns.tolist()
    categorical = [name for name in features.columns if name not in numeric]
    transformer = ColumnTransformer(
        transformers=[
            ("numeric", StandardScaler(), numeric),
            ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical),
        ],
        remainder="drop",
    )
    # Preprocessing is fitted inside the training pipeline: no fitting on the test set.
    return Pipeline(
        steps=[
            ("preprocessing", transformer),
            (
                "classifier",
                LogisticRegression(
                    max_iter=1000,
                    solver="lbfgs",
                    class_weight="balanced" if balance_classes else None,
                    random_state=42,
                ),
            ),
        ]
    )


def evaluate_predictions(y_true: pd.Series, predictions: np.ndarray, scores: np.ndarray | None) -> dict:
    result = {
        "accuracy": float(accuracy_score(y_true, predictions)),
        "balanced_accuracy": float(balanced_accuracy_score(y_true, predictions)),
        "precision_yes": float(precision_score(y_true, predictions, zero_division=0)),
        "recall_yes": float(recall_score(y_true, predictions, zero_division=0)),
        "f1_yes": float(f1_score(y_true, predictions, zero_division=0)),
        "confusion_matrix_no_yes": confusion_matrix(y_true, predictions, labels=[0, 1]).tolist(),
    }
    if scores is not None:
        result["roc_auc"] = float(roc_auc_score(y_true, scores))
        result["average_precision"] = float(average_precision_score(y_true, scores))
    return result


def run_evaluation(df: pd.DataFrame) -> dict:
    y = df[TARGET].map({"No": 0, "Yes": 1}).astype(int)
    X = df.drop(columns=[TARGET])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )
    # An explicit majority-class benchmark makes imbalanced accuracy interpretable.
    baseline = DummyClassifier(strategy="most_frequent")
    baseline.fit(X_train, y_train)
    results = {
        "dataset_rows": int(len(df)),
        "features": int(X.shape[1]),
        "train_rows": int(len(X_train)),
        "test_rows": int(len(X_test)),
        "positive_fraction": float(y.mean()),
        "method": "stratified 80/20 holdout; random_state=42; one-hot encoding; scaled numeric predictors",
        "majority_baseline": evaluate_predictions(
            y_test, baseline.predict(X_test), None
        ),
    }
    for name, balance in [
        ("logistic_regression", False),
        ("logistic_regression_class_weight_balanced", True),
    ]:
        model = build_model(X_train, balance_classes=balance)
        model.fit(X_train, y_train)
        result = evaluate_predictions(
            y_test, model.predict(X_test), model.predict_proba(X_test)[:, 1]
        )
        result["converged"] = bool(model.named_steps["classifier"].n_iter_[0] < 1000)
        results[name] = result
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--sample", type=int, default=None,
        help="Optional stratified sample size for a quick smoke test (not final reporting)",
    )
    args = parser.parse_args()
    df = load_data(args.data)
    if args.sample is not None:
        if not 20 <= args.sample <= len(df):
            parser.error("--sample must be between 20 and the dataset row count")
        df, _ = train_test_split(
            df, train_size=args.sample, stratify=df[TARGET], random_state=42
        )
    results = run_evaluation(df)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2, ensure_ascii=False))
    print(f"\nSaved: {args.output}")


if __name__ == "__main__":
    main()
