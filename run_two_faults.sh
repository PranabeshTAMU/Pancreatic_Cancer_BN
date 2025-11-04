#!/bin/bash
# run_two_faults.sh - Execute double-fault Boolean network analysis

echo "=========================================="
echo "Double-Fault Analysis"
echo "Pancreatic Cancer Boolean Network Model"
echo "=========================================="

mkdir -p results/double_fault

python3 code/pancreatic_two_faults.py

echo "✓ Double-fault analysis complete"
echo "Results saved to: results/double_fault/"
