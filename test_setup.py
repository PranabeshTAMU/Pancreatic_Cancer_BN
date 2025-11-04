"""
Test script to verify all files and environment setup
Run: python test_setup.py
"""

import os
import sys

print("="*70)
print("PANCREATIC CANCER BOOLEAN NETWORK - SETUP VERIFICATION")
print("="*70)

# Check Python version
print(f"\n1. Python Version: {sys.version}")

# Check required packages
print("\n2. Checking required packages...")
packages_ok = True

try:
    import numpy as np
    print(f"   ✓ NumPy {np.__version__}")
except ImportError:
    print("   ✗ NumPy NOT FOUND - Run: pip install numpy")
    packages_ok = False

try:
    import pandas as pd
    print(f"   ✓ Pandas {pd.__version__}")
except ImportError:
    print("   ✗ Pandas NOT FOUND - Run: pip install pandas")
    packages_ok = False

try:
    import scipy
    print(f"   ✓ SciPy {scipy.__version__}")
except ImportError:
    print("   ✗ SciPy NOT FOUND - Run: pip install scipy")
    packages_ok = False

try:
    import matplotlib
    print(f"   ✓ Matplotlib {matplotlib.__version__}")
except ImportError:
    print("   ✗ Matplotlib NOT FOUND - Run: pip install matplotlib")

# Check for required files
print("\n3. Checking required files...")
required_files = [
    'pancreatic_main.py',
    'pancreatic_single_fault.py',
    'pancreatic_two_faults.py',
    'pancreatic_three_faults.py'
]

optional_files = [
    'network_nodes.csv',
    'drug_combinations.csv',
    'fault_position_table_with_references.csv',
    'drug_target_table_with_pathways.csv',
    'requirements.txt',
    'environment.yml'
]

files_ok = True
for file in required_files:
    if os.path.exists(file):
        size = os.path.getsize(file)
        print(f"   ✓ {file} ({size:,} bytes)")
    else:
        print(f"   ✗ {file} MISSING")
        files_ok = False

print("\n4. Optional data files:")
for file in optional_files:
    if os.path.exists(file):
        size = os.path.getsize(file)
        print(f"   ✓ {file} ({size:,} bytes)")
    else:
        print(f"   - {file} (not found - optional)")

# Check CSV files can be read
print("\n5. Checking CSV files (if present)...")
if os.path.exists('network_nodes.csv'):
    try:
        import pandas as pd
        df_nodes = pd.read_csv('network_nodes.csv')
        print(f"   ✓ network_nodes.csv: {len(df_nodes)} rows, {len(df_nodes.columns)} columns")
    except Exception as e:
        print(f"   ✗ Error reading network_nodes.csv: {e}")

if os.path.exists('drug_combinations.csv'):
    try:
        import pandas as pd
        df_combos = pd.read_csv('drug_combinations.csv')
        print(f"   ✓ drug_combinations.csv: {len(df_combos)} rows, {len(df_combos.columns)} columns")
    except Exception as e:
        print(f"   ✗ Error reading drug_combinations.csv: {e}")

# Test import of your modules
print("\n6. Testing Python module imports...")
try:
    from pancreatic_single_fault import pancreatic_single_fault
    print("   ✓ pancreatic_single_fault module imported successfully")
    
    # Test a simple function call
    print("   ✓ Testing function call...")
    result = pancreatic_single_fault(7, 0, 0, 1, 1, 0, 0, 0, 0)
    print(f"   ✓ Function call successful!")
    print(f"   ✓ Test: KRAS mutation (fault 7) with Abraxane+Gemcitabine")
    print(f"   ✓ Result: NMSD = {result:.6f} (efficacy = {(1-result)*100:.2f}%)")
except Exception as e:
    print(f"   ✗ Error with pancreatic_single_fault: {e}")

try:
    from pancreatic_two_faults import pancreatic_two_faults
    print("   ✓ pancreatic_two_faults module imported successfully")
except Exception as e:
    print(f"   ✗ Error with pancreatic_two_faults: {e}")

try:
    from pancreatic_three_faults import pancreatic_three_faults
    print("   ✓ pancreatic_three_faults module imported successfully")
except Exception as e:
    print(f"   ✗ Error with pancreatic_three_faults: {e}")

print("\n" + "="*70)
print("VERIFICATION SUMMARY")
print("="*70)

if packages_ok and files_ok:
    print("\n✓✓✓ ALL CHECKS PASSED! ✓✓✓")
    print("\nYour environment is ready to run the analysis!")
    print("\nNext steps:")
    print("  1. Run single fault analysis: python pancreatic_main.py")
    print("  2. Check the output files generated")
    print("  3. Analyze results in the CSV files")
else:
    print("\n⚠ SOME ISSUES FOUND")
    if not packages_ok:
        print("\n  Install missing packages:")
        print("    pip install numpy pandas scipy matplotlib")
    if not files_ok:
        print("\n  Make sure all .py files are in this directory:")
        print(f"    {os.getcwd()}")

print("="*70)
