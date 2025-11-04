#!/usr/bin/env python3
"""
test_installation.py - Verify all dependencies are installed correctly
Pancreatic Cancer Boolean Network Model
"""

import sys
import subprocess

def check_python_version():
    """Check if Python version meets requirements"""
    if sys.version_info < (3, 8):
        print("❌ Python version < 3.8. Please upgrade Python.")
        return False
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def check_packages():
    """Check if all required packages are installed"""
    packages = ['numpy', 'pandas', 'scipy', 'matplotlib', 'jupyter']
    all_ok = True
    
    for package in packages:
        try:
            __import__(package)
            print(f"✓ {package} installed")
        except ImportError:
            print(f"❌ {package} NOT installed")
            all_ok = False
    
    return all_ok

def check_data_files():
    """Check if required data files exist"""
    import os
    
    required_files = [
        'data/network_nodes.csv',
        'data/drug_combinations.csv',
        'data/fault_position_table_with_references-S2.csv',
        'data/drug_target_table_with_pathways-S1.csv'
    ]
    
    all_ok = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file} found")
        else:
            print(f"❌ {file} NOT found")
            all_ok = False
    
    return all_ok

def main():
    print("=" * 50)
    print("Pancreatic Cancer Boolean Network - Installation Check")
    print("=" * 50)
    print()
    
    results = []
    
    print("1. Checking Python version...")
    results.append(check_python_version())
    print()
    
    print("2. Checking required packages...")
    results.append(check_packages())
    print()
    
    print("3. Checking data files...")
    results.append(check_data_files())
    print()
    
    if all(results):
        print("✓ All checks passed! System is ready to run analyses.")
        return 0
    else:
        print("❌ Some checks failed. Please install missing components.")
        print("   Run: pip install -r requirements.txt")
        return 1

if __name__ == '__main__':
    sys.exit(main())
