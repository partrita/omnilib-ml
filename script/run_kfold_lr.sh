#!/bin/bash
# Run 5-fold cross validation for LR model
# Output saved to data/kfold/

set -e

# Activate conda environment (adjust PATH to your conda installation)
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
conda activate omnilib-stability || \
  (echo "Please activate the environment: conda activate omnilib-stability" && exit 1)

# Create output directory
mkdir -p data/kfold

# Run K-fold CV
python script/kfold_lr.py \
    --n-folds 5 \
    --epochs 10 \
    --output-dir data/kfold \
    2>&1 | tee data/kfold/kfold_lr.log

echo "Done. Output saved to data/kfold/"
