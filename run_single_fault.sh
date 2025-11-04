#!/bin/bash
# run_single_fault.sh - Execute single-fault Boolean network analysis

echo "=========================================="
echo "Single-Fault Analysis"
echo "Pancreatic Cancer Boolean Network Model"
echo "=========================================="

mkdir -p results/single_fault

python3 code/pancreatic_single_fault.py

echo "✓ Single-fault analysis complete"
echo "Results saved to: results/single_fault/"
