#!/usr/bin/env python3
"""
Verification script to validate computational results against reference outputs.
Ensures reproducibility of Boolean network drug combination analysis.
"""

import numpy as np
import pandas as pd
import hashlib
import sys
from pathlib import Path

def verify_data_integrity():
    """Verify data file checksums."""
    expected_checksums = {
        'data/network_nodes.csv': 'a1b2c3d4e5f6',
        'data/boolean_functions.json': 'f6e5d4c3b2a1',
        'data/drug_combinations.csv': 'b2a1f6e5d4c3'
    }
    
    print("Verifying data integrity...")
    for file_path, expected_hash in expected_checksums.items():
        if Path(file_path).exists():
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()[:12]
            if file_hash == expected_hash:
                print(f"✓ {file_path}")
            else:
                print(f"✗ {file_path} - Hash mismatch")
                return False
        else:
            print(f"✗ {file_path} - File missing")
            return False
    return True

def compare_nmsd_results(computed_dir, reference_dir, tolerance=1e-6):
    """Compare computed NMSD results with reference values."""
    result_files = [
        'single_fault_results.csv',
        'double_fault_results.csv', 
        'triple_fault_results.csv'
    ]
    
    print(f"\nComparing results (tolerance: {tolerance})...")
    all_match = True
    
    for file_name in result_files:
        computed_path = Path(computed_dir) / file_name
        reference_path = Path(reference_dir) / file_name
        
        if not computed_path.exists():
            print(f"✗ {file_name} - Computed file missing")
            all_match = False
            continue
            
        if not reference_path.exists():
            print(f"✗ {file_name} - Reference file missing")
            all_match = False
            continue
        
        # Load data
        computed_df = pd.read_csv(computed_path)
        reference_df = pd.read_csv(reference_path)
        
        # Check shapes
        if computed_df.shape != reference_df.shape:
            print(f"✗ {file_name} - Shape mismatch: {computed_df.shape} vs {reference_df.shape}")
            all_match = False
            continue
        
        # Compare numeric columns
        numeric_cols = computed_df.select_dtypes(include=[np.number]).columns
        
        max_diff = 0
        mismatched_cells = 0
        
        for col in numeric_cols:
            if col in reference_df.columns:
                diff = np.abs(computed_df[col] - reference_df[col])
                max_col_diff = diff.max()
                col_mismatches = (diff > tolerance).sum()
                
                max_diff = max(max_diff, max_col_diff)
                mismatched_cells += col_mismatches
        
        if max_diff <= tolerance and mismatched_cells == 0:
            print(f"✓ {file_name} - Perfect match")
        elif max_diff <= tolerance * 10:
            print(f"⚠ {file_name} - Close match (max diff: {max_diff:.2e})")
        else:
            print(f"✗ {file_name} - Significant differences (max diff: {max_diff:.2e}, mismatches: {mismatched_cells})")
            all_match = False
    
    return all_match

def verify_statistical_properties(results_dir):
    """Verify key statistical properties of results."""
    print(f"\nVerifying statistical properties...")
    
    # Load single fault results
    single_fault_path = Path(results_dir) / 'single_fault_results.csv'
    if not single_fault_path.exists():
        print("✗ Cannot verify statistics - single_fault_results.csv missing")
        return False
    
    df = pd.read_csv(single_fault_path)
    
    # Expected properties based on paper results
    checks = []
    
    # Check if Palmatine is among best single drugs
    drug_columns = [col for col in df.columns if col != 'Untreated']
    if len(drug_columns) > 0:
        single_drug_means = df[drug_columns[:8]].mean()  # First 8 are single drugs
        best_single = single_drug_means.idxmin()
        checks.append(('Best single drug', 'palmatine' in best_single.lower(), 
                      f"Found: {best_single}"))
    
    # Check NMSD ranges
    all_values = df[drug_columns].values.flatten()
    all_values = all_values[~np.isnan(all_values)]
    
    checks.append(('NMSD range', 0.0 <= all_values.min() <= 1.0 and 0.0 <= all_values.max() <= 1.0,
                  f"Range: [{all_values.min():.3f}, {all_values.max():.3f}]"))
    
    checks.append(('Untreated baseline', df['Untreated'].iloc[0] == 1.0 if 'Untreated' in df.columns else True,
                  f"Untreated NMSD: {df['Untreated'].iloc[0] if 'Untreated' in df.columns else 'N/A'}"))
    
    # Print results
    all_passed = True
    for check_name, passed, details in checks:
        status = "✓" if passed else "✗"
        print(f"{status} {check_name}: {details}")
        if not passed:
            all_passed = False
    
    return all_passed

def main():
    """Main verification routine."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Verify computational results')
    parser.add_argument('--computed', default='results/', help='Computed results directory')
    parser.add_argument('--reference', default='reference_outputs/', help='Reference results directory')
    parser.add_argument('--tolerance', type=float, default=1e-6, help='Numerical tolerance')
    
    args = parser.parse_args()
    
    print("=== Pancreatic Cancer Boolean Network - Result Verification ===\n")
    
    # Step 1: Verify data integrity
    integrity_ok = verify_data_integrity()
    
    # Step 2: Compare results
    comparison_ok = compare_nmsd_results(args.computed, args.reference, args.tolerance)
    
    # Step 3: Verify statistical properties  
    stats_ok = verify_statistical_properties(args.computed)
    
    # Summary
    print(f"\n=== Verification Summary ===")
    print(f"Data integrity: {'PASS' if integrity_ok else 'FAIL'}")
    print(f"Result comparison: {'PASS' if comparison_ok else 'FAIL'}")
    print(f"Statistical properties: {'PASS' if stats_ok else 'FAIL'}")
    
    overall_status = integrity_ok and comparison_ok and stats_ok
    print(f"Overall: {'PASS - Results are reproducible' if overall_status else 'FAIL - Issues detected'}")
    
    sys.exit(0 if overall_status else 1)

if __name__ == "__main__":
    main()