#!/bin/bash
# run_three_faults.sh - Execute triple-fault Boolean network analysis

echo "=========================================="
echo "Triple-Fault Analysis"
echo "Pancreatic Cancer Boolean Network Model"
echo "=========================================="

mkdir -p results/triple_fault

python3 code/pancreatic_three_faults.py

echo "✓ Triple-fault analysis complete"
echo "Results saved to: results/triple_fault/"
