"""Fast tests using synthetic observations; no real survey data required."""
from pathlib import Path
import sys

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "analysis"))
from evaluate_model import build_model, evaluate_predictions, load_data, run_evaluation


def test_rejects_invalid_target(tmp_path):
    path = tmp_path / "invalid.csv"
    pd.DataFrame({"HeartDisease": ["No", "Unknown"], "BMI": [23, 28]}).to_csv(path, index=False)
    with pytest.raises(ValueError, match="HeartDisease"):
        load_data(path)


def test_metrics_count_positive_class_correctly():
    result = evaluate_predictions(
        pd.Series([0, 0, 1, 1]), np.array([0, 1, 0, 1]), None
    )
    assert result["precision_yes"] == 0.5
    assert result["recall_yes"] == 0.5
    assert result["confusion_matrix_no_yes"] == [[1, 1], [1, 1]]


def test_pipeline_encodes_categories_and_scores_holdout():
    # Both classes and an unordered category; enough records for stratified split.
    n = 100
    frame = pd.DataFrame(
        {
            "HeartDisease": ["Yes" if i % 5 == 0 else "No" for i in range(n)],
            "BMI": [23.0 + (i % 9) for i in range(n)],
            "Race": ["A", "B", "C", "D"] * 25,
            "GenHealth": ["Good", "Fair"] * 50,
        }
    )
    result = run_evaluation(frame)
    assert result["test_rows"] == 20
    assert 0 <= result["logistic_regression"]["f1_yes"] <= 1
    assert "average_precision" in result["logistic_regression_class_weight_balanced"]
