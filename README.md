# Pancreatic Cancer Boolean Network Analysis

This repository contains the complete computational framework for analyzing drug combinations in pancreatic cancer using Boolean network modeling.

## Quick Start

```bash
# Clone repository
git clone https://github.com/PranabeshTAMU/PancreaticCancerBN.git
cd PancreaticCancerBN

# Setup environment
conda env create -f environment.yml
conda activate pancreatic-bn

# Or using pip
pip install -r requirements.txt

# Run complete analysis
python pancreatic_main.py
```

## Repository Structure

```
├── src/                          # Source code
│   ├── pancreatic_main.py        # Main analysis script
│   ├── pancreatic_single_fault.py   # Single mutation analysis
│   ├── pancreatic_two_faults.py     # Double mutation analysis
│   └── pancreatic_three_faults.py   # Triple mutation analysis
├── data/                         # Network and drug data
│   ├── network_nodes.csv         # Node specifications
│   ├── boolean_functions.json    # Network logic
│   ├── drug_targets.csv          # Drug-target mappings
│   ├── drug_combinations.csv     # All 162 combinations
│   └── input_states.csv          # Input node states
├── results/                      # Output files
│   ├── single_fault_results.csv
│   ├── double_fault_results.csv
│   └── triple_fault_results.csv
├── config/                       # Configuration files
├── docs/                         # Documentation
├── environment.yml               # Conda environment
└── requirements.txt              # Pip requirements
```

## Key Features

- **49 fault locations** representing pancreatic cancer mutations
- **162 drug combinations** (0-4 drugs from 8 available compounds)
- **19,649 total scenarios** (single, double, triple mutations)
- **Systematic NMSD scoring** for drug efficacy evaluation
- **Reproducible results** with fixed random seed (42)

## Usage Examples

### Run specific mutation analysis
```python
from pancreatic_single_fault import pancreaticsinglefault

# Test single KRAS mutation with Berberine
result = pancreaticsinglefault(7, 0, 1, 0, 0, 0, 0, 0, 0)
print(f"NMSD Score: {result}")
```

### Analyze drug combinations
```python
# Run comprehensive analysis
python pancreatic_main.py

# Results will be saved in results/ directory
```

## Data Files

All network topology, Boolean functions, and drug specifications are provided in structured CSV/JSON format for reproducibility.

## Citation

If you use this code, please cite:
```
Bhattacharjee et al. (2025). Computational Analysis of Palmatine and Berberine 
Efficacy in Drug Combinations for Pancreatic Cancer Using Boolean Network Modeling.
```

## License

MIT License - see LICENSE file for details.