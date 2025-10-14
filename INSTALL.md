# Installation Guide

## System Requirements

- Python 3.9.12 or higher
- 8GB RAM minimum (16GB recommended)
- 2GB free disk space
- Unix/Linux/macOS/Windows 10+

## Method 1: Using Conda (Recommended)

1. **Install Anaconda/Miniconda**
   ```bash
   # Download Miniconda (if not installed)
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   bash Miniconda3-latest-Linux-x86_64.sh
   ```

2. **Create Environment**
   ```bash
   git clone https://github.com/PranabeshTAMU/PancreaticCancerBN.git
   cd PancreaticCancerBN
   conda env create -f environment.yml
   conda activate pancreatic-bn
   ```

3. **Verify Installation**
   ```bash
   python -c "import numpy, pandas, networkx; print('Installation successful')"
   ```

## Method 2: Using Pip

1. **Create Virtual Environment**
   ```bash
   git clone https://github.com/PranabeshTAMU/PancreaticCancerBN.git
   cd PancreaticCancerBN
   python -m venv pancreatic-env
   source pancreatic-env/bin/activate  # Linux/macOS
   # Or: pancreatic-env\Scripts\activate  # Windows
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Method 3: Using Poetry

1. **Install Poetry**
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Install Project**
   ```bash
   git clone https://github.com/PranabeshTAMU/PancreaticCancerBN.git
   cd PancreaticCancerBN
   poetry install
   poetry shell
   ```

## Verification

Run the test suite to verify installation:
```bash
python -m pytest tests/ -v
```

Or run a quick test:
```bash
python pancreatic_main.py --test
```

## Troubleshooting

**Common Issues:**

1. **ImportError: No module named 'networkx'**
   ```bash
   pip install networkx==2.7.1
   ```

2. **Memory Error during analysis**
   - Reduce number of fault combinations
   - Use system with more RAM
   - Run analysis in batches

3. **Permission denied errors**
   ```bash
   chmod +x *.py
   ```

## Hardware Recommendations

- **Minimum**: 4 cores, 8GB RAM, 50GB disk
- **Recommended**: 8+ cores, 16GB RAM, 100GB SSD
- **Optimal**: 16+ cores, 32GB RAM, 200GB NVMe SSD