# Usage Guide

## Basic Usage

### Running Complete Analysis

```bash
# Run all single, double, and triple fault combinations
python pancreatic_main.py

# Specify number of drugs in combinations (0-4)
python pancreatic_main.py --num-drugs 3
```

### Individual Module Usage

```python
# Single fault analysis
from pancreatic_single_fault import pancreaticsinglefault

# Test KRAS mutation (fault 7) with Berberine only
nmsd_score = pancreaticsinglefault(
    fault1=7,           # KRAS mutation
    x1=0, x2=1, x3=0,   # Berberine only (palmatine=0, berberine=1, abraxane=0)
    x4=0, x5=0, x6=0,   # No other drugs
    x7=0, x8=0          # No EGFR inhibitors
)
print(f"NMSD Score: {nmsd_score}")
```

```python
# Double fault analysis
from pancreatic_two_faults import pancreatictwofaults

# Test KRAS + TP53 mutations with Gemcitabine + Berberine
nmsd_score = pancreatictwofaults(
    fault1=7, fault2=36,  # KRAS + P53 mutations
    x1=0, x2=1, x3=0, x4=1,  # Berberine + Gemcitabine
    x5=0, x6=0, x7=0, x8=0   # No EGFR inhibitors
)
```

## Drug Encoding

Drugs are encoded as binary variables (0=absent, 1=present):

| Position | Drug | Target Pathways |
|----------|------|-----------------|
| x1 | Palmatine | PI3K-AKT, JAK-STAT |
| x2 | Berberine | PI3K-AKT, mTOR, MAPK |
| x3 | Abraxane | Cell Cycle, Apoptosis |
| x4 | Gemcitabine | DNA Repair, p53 |
| x5 | Gefitinib | EGFR, PI3K-AKT |
| x6 | Dacomitinib | EGFR, MAPK |
| x7 | Afatinib | EGFR, MAPK |
| x8 | GANT61 | Hedgehog, Cell Cycle |

## Fault Encoding

Key fault locations (1-49):

| Fault ID | Gene | Stuck-At | Pathway |
|----------|------|----------|---------|
| 1 | EGFR | 1 | ErbB/EGFR |
| 7 | RAS | 1 | KRAS-MAPK |
| 13 | PI3K | 1 | PI3K-AKT |
| 36 | P53 | 0 | p53 |
| 39 | mTOR | 1 | PI3K-AKT/mTOR |

See `data/network_nodes.csv` for complete list.

## Advanced Usage

### Custom Input States

```python
# Modify input states for different cellular contexts
# Default: Non-proliferative (healthy) state
inputs = {
    'P16': 1, 'KRAS': 0, 'EGF': 0, 'TGFalpha': 0,
    'HBEGF': 0, 'NRG1': 0, 'LKB1': 1, 'PTEN': 1,
    'IGF': 0, 'ALK': 0, 'DNADamage': 1, 'TGFbeta': 0
}
```

### Batch Analysis

```bash
# Run analysis for specific fault combinations
python batch_analysis.py --faults "1,7,13" --drugs "berberine,gemcitabine"

# Run with configuration file
python pancreatic_main.py --config config/custom_analysis.yaml
```

### Result Interpretation

NMSD scores range from 0.0 (perfect healthy state) to 1.0 (maximum deviation):

- **NMSD < 0.1**: Excellent network recovery
- **NMSD 0.1-0.3**: Good therapeutic effect  
- **NMSD 0.3-0.5**: Moderate therapeutic effect
- **NMSD > 0.5**: Poor therapeutic effect

### Visualization

```python
import matplotlib.pyplot as plt
import pandas as pd

# Load results
results = pd.read_csv('results/single_fault_results.csv')

# Plot drug efficacy comparison
plt.figure(figsize=(12, 6))
plt.boxplot([results[drug] for drug in drug_names])
plt.xlabel('Drug Combinations')
plt.ylabel('NMSD Score')
plt.title('Drug Efficacy Comparison')
plt.show()
```

## Output Files

Results are saved in CSV format:

- `results/single_fault_results.csv` - Single mutation analysis
- `results/double_fault_results.csv` - Double mutation analysis  
- `results/triple_fault_results.csv` - Triple mutation analysis

Each file contains:
- Drug combination names
- NMSD scores for each fault scenario
- Statistical summaries

## Configuration

Create custom analysis configurations:

```yaml
# config/custom_analysis.yaml
analysis:
  max_faults: 2
  drugs: ["berberine", "gemcitabine", "abraxane"]
  output_dir: "custom_results/"
  random_seed: 42

network:
  input_state: "non_proliferative"
  convergence_iterations: 15
```

## Performance Tips

1. **Memory Management**: For large analyses, process in batches
2. **Parallelization**: Use multiprocessing for independent fault scenarios  
3. **Caching**: Cache intermediate Boolean network states
4. **Profiling**: Use `cProfile` to identify bottlenecks

```bash
# Profile performance
python -m cProfile -s tottime pancreatic_main.py > profile.txt
```