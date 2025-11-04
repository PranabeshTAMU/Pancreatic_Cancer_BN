# pancreatic_main.py
## Main Controller Script for Boolean Network Analysis

This script coordinates the execution of single, double, and triple fault analyses for pancreatic cancer drug combination testing.

### Usage
```python
python pancreatic_main.py --mode all --output results/
```

### Features
- Loads network topology and drug configurations
- Executes fault scenario analyses in parallel
- Generates comprehensive results summaries
- Creates visualization plots
- Generates statistical reports

### Parameters
- `--mode`: Analysis type (single, double, triple, all)
- `--output`: Output directory for results
- `--verbose`: Enable detailed logging
- `--parallel`: Number of parallel processes

### Output
- Summary statistics CSV files
- Network state tables
- Drug efficacy rankings
- Comparison plots
