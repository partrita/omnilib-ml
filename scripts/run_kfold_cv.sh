#!/bin/bash
# Run K-fold cross validation for LR and CNN models
# Uses clustering-based splits for better generalization evaluation
# Output saved to data/kfold/

set -e

# Use pixi-activated Python if available, otherwise use system Python
which pixi && eval "$(pixi env activate)" || true

# Create output directory
mkdir -p data/kfold

# Run K-fold CV for LR
echo "=========================================="
echo "Running K-fold CV for Logistic Regression"
echo "=========================================="
python scripts/kfold_cv.py \
    --model-type lr \
    --n-folds 5 \
    --epochs 10 \
    --output-dir data/kfold \
    2>&1 | tee data/kfold/kfold_lr.log

# Run K-fold CV for CNN
echo ""
echo "=========================================="
echo "Running K-fold CV for CNN"
echo "=========================================="
python scripts/kfold_cv.py \
    --model-type cnn \
    --n-folds 5 \
    --epochs 10 \
    --output-dir data/kfold \
    2>&1 | tee data/kfold/kfold_cnn.log

echo ""
echo "Done. Output saved to data/kfold/"
echo "  - kfold_lr_results.json"
echo "  - kfold_cnn_results.json"
echo "  - kfold_lr_coefficients.png"
