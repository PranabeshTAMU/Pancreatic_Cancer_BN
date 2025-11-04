#!/bin/bash
# Run Complete Pancreatic Cancer Boolean Network Analysis Pipeline
# This script executes single, double, and triple fault analyses
# Estimated runtime: 2-3 hours on standard workstation

echo "=================================================="
echo "Pancreatic Cancer Boolean Network Analysis"
echo "Version 1.0 | October 2025"
echo "=================================================="
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null
then
    echo "Error: Python 3 not found. Please install Python 3.8+"
    exit 1
fi

# Check if required packages are installed
echo "[1/5] Checking dependencies..."
python3 -c "import numpy, pandas" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Error: Required packages not installed."
    echo "Please run: pip install -r requirements.txt"
    exit 1
fi
echo "✓ All dependencies found"
echo ""

# Create output directory
mkdir -p results
mkdir -p results/single_fault
mkdir -p results/double_fault
mkdir -p results/triple_fault

# Record start time
START_TIME=$(date +%s)
echo "[2/5] Starting analysis at $(date)"
echo ""

# Run single fault analysis
echo "[3/5] Running single fault analysis (49 faults × 162 combinations)..."
echo "Estimated time: 5 minutes"
python3 pancreatic_main.py --num_drugs 4 --output_dir results/single_fault
if [ $? -ne 0 ]; then
    echo "Error: Single fault analysis failed"
    exit 1
fi
echo "✓ Single fault analysis complete"
echo ""

# Run double fault analysis  
echo "[4/5] Running double fault analysis (1,176 fault pairs × 162 combinations)..."
echo "Estimated time: 20 minutes"
python3 pancreatic_main.py --num_drugs 4 --fault_mode double --output_dir results/double_fault
if [ $? -ne 0 ]; then
    echo "Error: Double fault analysis failed"
    exit 1
fi
echo "✓ Double fault analysis complete"
echo ""

# Run triple fault analysis
echo "[5/5] Running triple fault analysis (18,424 fault triplets × 162 combinations)..."
echo "Estimated time: 2 hours"
echo "Note: This may take longer on slower systems"
python3 pancreatic_main.py --num_drugs 4 --fault_mode triple --output_dir results/triple_fault
if [ $? -ne 0 ]; then
    echo "Error: Triple fault analysis failed"
    exit 1
fi
echo "✓ Triple fault analysis complete"
echo ""

# Calculate runtime
END_TIME=$(date +%s)
RUNTIME=$((END_TIME - START_TIME))
HOURS=$((RUNTIME / 3600))
MINUTES=$(((RUNTIME % 3600) / 60))
SECONDS=$((RUNTIME % 60))

echo "=================================================="
echo "Analysis Complete!"
echo "=================================================="
echo ""
echo "Total runtime: ${HOURS}h ${MINUTES}m ${SECONDS}s"
echo ""
echo "Results saved to:"
echo "  - results/single_fault/"
echo "  - results/double_fault/"
echo "  - results/triple_fault/"
echo ""
echo "Next steps:"
echo "  1. Review output_one_fault.csv for single mutation results"
echo "  2. Review output_two_faults.csv for double mutation results"
echo "  3. Review output_three_faults.csv for triple mutation results"
echo "  4. Identify top drug combinations with lowest NMSD scores"
echo ""
echo "For visualization, run:"
echo "  python3 visualize_results.py --input results/"
echo ""