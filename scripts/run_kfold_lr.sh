#!/bin/bash
# Run 5-fold cross validation for LR model
# Output saved to data/kfold/

set -e

# Use pixi-activated Python if available, otherwise use system Python
which pixi && eval "$(pixi env activate)" || true

# Create output directory
mkdir -p data/kfold

# Run K-fold CV
python scripts/kfold_lr.py \
    --n-folds 5 \
    --epochs 10 \
    --output-dir data/kfold \
    2>&1 | tee data/kfold/kfold_lr.log

echo "Done. Output saved to data/kfold/"
