# omnilib-ml

Official repository for the paper **Hypervariable loop profiling decodes sequence determinants of antibody stability.**

This repository contains code and data to train and evaluate models for predicting the stability of nanobodies based on their CDR sequences. We also provide pretrained models for the same task, as well as code to run inference on new sequences.

In general, these models work best with the synthetic libraries described in this paper: [Yeast surface display platform for rapid discovery of conformationally selective nanobodies]( https://www.nature.com/articles/s41594-018-0028-6), as well as the current work. This is to ensure best compatibility with the framework used in these synthetic libraries - other frameworks may not work as well.

## Installation

Depending on your use case, you can do a package install, or just use the repository as a library (e.g. in a Jupyter/Colab notebook).

I would recommend creating a new virtual environment for this project, to avoid conflicts with other packages. We used `python==3.10.15`

First, install a version of pytorch that works on your system (GPU or CPU). We used torch 2.2.0, but more recent versions should also work. Since the models we trained are fairly small, the CPU version should still be very efficient.

### Using pixi (recommended)

[Pixi](https://pixi.sh/) is a modern package manager that replaces conda and pip for managing Python/Rust dependencies. It creates isolated environments using conda-forge packages.

#### Method 1: Full Environment Setup (Recommended)

```bash
# Install pixi (if not already installed)
curl -L https://pixi.sh/install.sh | bash

# Create and enter the environment
pixi create

# Start a shell with all dependencies activated
pixi shell

# Inside the shell, install the package in editable mode
pip install -e .
# Or run scripts directly
python scripts/train_lr.sh
```

#### Method 2: Using pixi run

```bash
# Create environment
pixi create

# Run Python with the environment's Python interpreter
pixi run python -m pip install -e .

# Or run scripts directly (using full path within pixi shell)
pixi run python scripts/train_lr.sh
```

#### Method 3: One-step environment creation and package install

```bash
# Create environment and immediately install package
pixi create && pixi shell -- pip install -e .
```

#### Method 4: Without pixi (fallback)

If pixi is not available, use the traditional approach:

```bash
# Create a conda environment
conda create -n omnilib python=3.10.15 -y

# Activate it
conda activate omnilib

# Install PyTorch (choose one based on your setup)
# CPU version
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

# Or CUDA 11.8 + PyTorch 2.2.0
# pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu118

# Install package dependencies
pip install -r requirements.txt

# Or install from this repository
pip install -e .
```

## Data

We provide preprocessed and generated data for model training, and evaluation. Data generated as part of the figures in the paper are also provided. The data folder is stored at the following [zenodo link](https://doi.org/10.5281/zenodo.18224780)

Once downloaded, the data can be extracted to the data folder in the root of the repository.

```bash
tar -xvf data.tar.gz
```

I set up paths assuming the following structure:

```bash
├── data
├── figures
├── model_checkpoints
│   ├── CNN
│   └── LR
├── nabstab
│   ├── datasets
│   ├── models
│   ├── tango.py
│   ├── constants.py
│   └── utils.py
├── README.md
├── requirements.txt
...
├── setup.py
```

## Models

### Data Format

The classifier models require a dataframe/csv with the following columns: cdr1, cdr2, cdr3, stability

example:

```txt
CDR1,CDR2,CDR3,stability
RTFTSYT,LVAAITSSGGST,AADYRASGPYCGYY,high
STFDSNA,LVAAISWSGTSTY,AADPGEPYAYGY,high
...
YIFDGYA,LVARITYSSGSTY,NAPAYWFRLRRYDS,low
SIFGVNA,LVASISSGGSTN,AAVLYRTSRYSQALNY,low
```

### Training a Model

We provide training scripts for both logistic regression and convolutional neural network models. To train a model, you can use the following command (after modiying the parameters as needed):

```bash
# Logistic Regression
bash scripts/train_lr.sh

# Convolutional Neural Network
bash scripts/train_cnn.sh
```
These models are fairly lightweight. On my machine (Apple M2 Pro - CPU), the LR model takes ~90 seconds to train over 10 epochs, using the full dataset (~1M samples). The CNN model, with the parameters we used, takes significantly longer.

If you're using CPU, we'd recommend maybe using a smaller dataset, which is provided in `data/model_training_data/train_subset.csv`. This subset has ~30k samples, and a CNN model (with the same architecture) trained on it takes about 90 seconds to train over 10 epochs.

### Running Inference

To run inference on a new set of sequences, you can use the `evaluate_fitness_scores.py` script. This script takes a fasta file with sequences, and a set of trained models, and outputs the fitness scores for each sequence. The output is a CSV file with the sequences and their corresponding fitness scores.

```bash
bash scripts/evaluate_fitness.sh
```

## Pretrained Model Checkpoints

As part of this work, we provide the following pretrained models, as well as code to train new models, as well as run inference.

### OmniLib Fitness Classifiers

| Model | Description | Parameters | Location |
| --- | --- | --- | --- |
|CNN| Convolutional Neural Network| 8k| `model_checkpoints/CNN/cnn_24_fc_8.pt`|
|LR| Logistic Regression| 1k| `model_checkpoints/LR/20231223_LR.pt`|

### Figures

All figures from the paper that use the datasets and models in this repository are provided in the `figures` directory. For each figure, there is a juptyer notebook that generates the figure. The notebooks are named according to the figure they generate. Furthermore, the outputs of the notebooks are provided in the `figures` directory as well.
