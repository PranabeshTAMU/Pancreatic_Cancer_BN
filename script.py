
import json
import pandas as pd

# Create requirements.txt content
requirements_txt = """# Python Environment Requirements for Pancreatic Cancer Boolean Network Model
# Generated: October 2025
# Python Version: 3.8+

numpy>=1.21.0
pandas>=1.3.0
itertools-recipes>=0.0.3
scipy>=1.7.0
matplotlib>=3.4.0  # For visualization (if needed)

# Optional for enhanced performance
numba>=0.54.0  # JIT compilation for faster execution
tqdm>=4.62.0   # Progress bars for long-running simulations
"""

# Create environment.yml for conda
environment_yml = """name: pancreatic-cancer-boolean-network
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.9
  - numpy=1.21.0
  - pandas=1.3.0
  - scipy=1.7.0
  - matplotlib=3.4.0
  - jupyter=1.0.0
  - pip
  - pip:
    - itertools-recipes>=0.0.3
    - numba>=0.54.0
    - tqdm>=4.62.0
"""

# Create node list CSV
nodes_data = [
    {"Node_ID": 1, "Node_Name": "P16", "Type": "Input", "Initial_State": 1, "Description": "Tumor suppressor"},
    {"Node_ID": 2, "Node_Name": "KRAS", "Type": "Input", "Initial_State": 0, "Description": "Oncogene"},
    {"Node_ID": 3, "Node_Name": "EGF", "Type": "Input", "Initial_State": 0, "Description": "Growth factor"},
    {"Node_ID": 4, "Node_Name": "TGFalpha", "Type": "Input", "Initial_State": 0, "Description": "Growth factor"},
    {"Node_ID": 5, "Node_Name": "HBEGF", "Type": "Input", "Initial_State": 0, "Description": "Growth factor"},
    {"Node_ID": 6, "Node_Name": "NRG1", "Type": "Input", "Initial_State": 0, "Description": "Growth factor"},
    {"Node_ID": 7, "Node_Name": "LKB1", "Type": "Input", "Initial_State": 1, "Description": "Tumor suppressor"},
    {"Node_ID": 8, "Node_Name": "PTEN", "Type": "Input", "Initial_State": 1, "Description": "Tumor suppressor"},
    {"Node_ID": 9, "Node_Name": "IGF", "Type": "Input", "Initial_State": 0, "Description": "Growth factor"},
    {"Node_ID": 10, "Node_Name": "ALK", "Type": "Input", "Initial_State": 0, "Description": "Tyrosine kinase"},
    {"Node_ID": 11, "Node_Name": "DNA_Damage", "Type": "Input", "Initial_State": 1, "Description": "DNA damage signal"},
    {"Node_ID": 12, "Node_Name": "TGFbeta", "Type": "Input", "Initial_State": 0, "Description": "Growth factor"},
    {"Node_ID": 13, "Node_Name": "EGFR", "Type": "Intermediate", "Initial_State": "Computed", "Description": "EGFR receptor"},
    {"Node_ID": 14, "Node_Name": "ERBB2", "Type": "Intermediate", "Initial_State": "Computed", "Description": "ERBB2 receptor"},
    {"Node_ID": 15, "Node_Name": "IGFR", "Type": "Intermediate", "Initial_State": "Computed", "Description": "IGF receptor"},
    {"Node_ID": 16, "Node_Name": "ATM", "Type": "Intermediate", "Initial_State": "Computed", "Description": "DNA damage response"},
    {"Node_ID": 17, "Node_Name": "TGFBR1/2", "Type": "Intermediate", "Initial_State": "Computed", "Description": "TGF-beta receptor"},
    {"Node_ID": 18, "Node_Name": "SMAD", "Type": "Intermediate", "Initial_State": "Computed", "Description": "SMAD signaling"},
    {"Node_ID": 19, "Node_Name": "RAS", "Type": "Intermediate", "Initial_State": "Computed", "Description": "RAS signaling"},
    {"Node_ID": 20, "Node_Name": "RAF", "Type": "Intermediate", "Initial_State": "Computed", "Description": "RAF kinase"},
    {"Node_ID": 21, "Node_Name": "MEK", "Type": "Intermediate", "Initial_State": "Computed", "Description": "MEK kinase"},
    {"Node_ID": 22, "Node_Name": "JAK", "Type": "Intermediate", "Initial_State": "Computed", "Description": "JAK kinase"},
    {"Node_ID": 23, "Node_Name": "STAT", "Type": "Intermediate", "Initial_State": "Computed", "Description": "STAT transcription factor"},
    {"Node_ID": 24, "Node_Name": "IRS", "Type": "Intermediate", "Initial_State": "Computed", "Description": "Insulin receptor substrate"},
    {"Node_ID": 25, "Node_Name": "PI3K", "Type": "Intermediate", "Initial_State": "Computed", "Description": "PI3K kinase"},
    {"Node_ID": 26, "Node_Name": "PIP3", "Type": "Intermediate", "Initial_State": "Computed", "Description": "Phospholipid second messenger"},
    {"Node_ID": 27, "Node_Name": "PKB_AKT", "Type": "Intermediate", "Initial_State": "Computed", "Description": "AKT kinase"},
    {"Node_ID": 28, "Node_Name": "AMPK", "Type": "Intermediate", "Initial_State": "Computed", "Description": "Energy sensor"},
    {"Node_ID": 29, "Node_Name": "RacGEF", "Type": "Intermediate", "Initial_State": "Computed", "Description": "RAC activator"},
    {"Node_ID": 30, "Node_Name": "ERK", "Type": "Intermediate", "Initial_State": "Computed", "Description": "ERK kinase"},
    {"Node_ID": 31, "Node_Name": "PDPK", "Type": "Intermediate", "Initial_State": "Computed", "Description": "PDK1 kinase"},
    {"Node_ID": 32, "Node_Name": "JNK", "Type": "Intermediate", "Initial_State": "Computed", "Description": "JNK kinase"},
    {"Node_ID": 33, "Node_Name": "RalGDS", "Type": "Intermediate", "Initial_State": "Computed", "Description": "RAL activator"},
    {"Node_ID": 34, "Node_Name": "GLI1", "Type": "Intermediate", "Initial_State": "Computed", "Description": "Hedgehog transcription factor"},
    {"Node_ID": 35, "Node_Name": "DAXX", "Type": "Intermediate", "Initial_State": "Computed", "Description": "Death domain protein"},
    {"Node_ID": 36, "Node_Name": "ASK1", "Type": "Intermediate", "Initial_State": "Computed", "Description": "Apoptosis signal kinase"},
    {"Node_ID": 37, "Node_Name": "RAL", "Type": "Intermediate", "Initial_State": "Computed", "Description": "RAL GTPase"},
    {"Node_ID": 38, "Node_Name": "MKK", "Type": "Intermediate", "Initial_State": "Computed", "Description": "MAP kinase kinase"},
    {"Node_ID": 39, "Node_Name": "RalBP1", "Type": "Intermediate", "Initial_State": "Computed", "Description": "RAL binding protein"},
    {"Node_ID": 40, "Node_Name": "PLD1", "Type": "Intermediate", "Initial_State": "Computed", "Description": "Phospholipase D1"},
    {"Node_ID": 41, "Node_Name": "P38", "Type": "Intermediate", "Initial_State": "Computed", "Description": "P38 MAPK"},
    {"Node_ID": 42, "Node_Name": "RAC", "Type": "Intermediate", "Initial_State": "Computed", "Description": "RAC GTPase"},
    {"Node_ID": 43, "Node_Name": "IKK", "Type": "Intermediate", "Initial_State": "Computed", "Description": "IKK kinase"},
    {"Node_ID": 44, "Node_Name": "PA", "Type": "Intermediate", "Initial_State": "Computed", "Description": "Phosphatidic acid"},
    {"Node_ID": 45, "Node_Name": "NF-κB", "Type": "Intermediate", "Initial_State": "Computed", "Description": "NF-kappa B"},
    {"Node_ID": 46, "Node_Name": "TSC1/2", "Type": "Intermediate", "Initial_State": "Computed", "Description": "TSC complex"},
    {"Node_ID": 47, "Node_Name": "MDM2", "Type": "Intermediate", "Initial_State": "Computed", "Description": "p53 inhibitor"},
    {"Node_ID": 48, "Node_Name": "P53", "Type": "Intermediate", "Initial_State": "Computed", "Description": "Tumor suppressor"},
    {"Node_ID": 49, "Node_Name": "BRCA2", "Type": "Intermediate", "Initial_State": "Computed", "Description": "DNA repair protein"},
    {"Node_ID": 50, "Node_Name": "RHEB", "Type": "Intermediate", "Initial_State": "Computed", "Description": "mTOR activator"},
    {"Node_ID": 51, "Node_Name": "mTOR", "Type": "Intermediate", "Initial_State": "Computed", "Description": "mTOR kinase"},
    {"Node_ID": 52, "Node_Name": "RPS6KB", "Type": "Intermediate", "Initial_State": "Computed", "Description": "S6 kinase"},
    {"Node_ID": 53, "Node_Name": "GSK3", "Type": "Intermediate", "Initial_State": "Computed", "Description": "GSK3 kinase"},
    {"Node_ID": 54, "Node_Name": "BAD", "Type": "Intermediate", "Initial_State": "Computed", "Description": "Pro-apoptotic protein"},
    {"Node_ID": 55, "Node_Name": "CyclinD1", "Type": "Intermediate", "Initial_State": "Computed", "Description": "Cell cycle regulator"},
    {"Node_ID": 56, "Node_Name": "P21", "Type": "Intermediate", "Initial_State": "Computed", "Description": "CDK inhibitor"},
    {"Node_ID": 57, "Node_Name": "CDK4/1", "Type": "Intermediate", "Initial_State": "Computed", "Description": "Cyclin-dependent kinase"},
    {"Node_ID": 58, "Node_Name": "Rb", "Type": "Intermediate", "Initial_State": "Computed", "Description": "Retinoblastoma protein"},
    {"Node_ID": 59, "Node_Name": "RAD51", "Type": "Intermediate", "Initial_State": "Computed", "Description": "DNA repair protein"},
    {"Node_ID": 60, "Node_Name": "P48", "Type": "Intermediate", "Initial_State": "Computed", "Description": "Transcription factor"},
    {"Node_ID": 61, "Node_Name": "BCL-XL", "Type": "Intermediate", "Initial_State": "Computed", "Description": "Anti-apoptotic protein"},
    {"Node_ID": 62, "Node_Name": "SRFELK1", "Type": "Output", "Initial_State": "Computed", "Description": "Proliferation marker"},
    {"Node_ID": 63, "Node_Name": "SP1", "Type": "Output", "Initial_State": "Computed", "Description": "Proliferation marker"},
    {"Node_ID": 64, "Node_Name": "E2F", "Type": "Output", "Initial_State": "Computed", "Description": "Cell cycle marker"},
    {"Node_ID": 65, "Node_Name": "FOS_JUN", "Type": "Output", "Initial_State": "Computed", "Description": "Proliferation marker"},
    {"Node_ID": 66, "Node_Name": "BAX", "Type": "Output", "Initial_State": "Computed", "Description": "Apoptosis marker"},
    {"Node_ID": 67, "Node_Name": "SRFELK4", "Type": "Output", "Initial_State": "Computed", "Description": "Proliferation marker"},
    {"Node_ID": 68, "Node_Name": "VEGF", "Type": "Output", "Initial_State": "Computed", "Description": "Angiogenesis marker"},
    {"Node_ID": 69, "Node_Name": "DNA_Repair", "Type": "Output", "Initial_State": "Computed", "Description": "DNA repair marker"},
]

df_nodes = pd.DataFrame(nodes_data)
df_nodes.to_csv("network_nodes.csv", index=False)

print("Node list CSV created: network_nodes.csv")
print(f"Total nodes: {len(df_nodes)}")
print(f"Input nodes: {len(df_nodes[df_nodes['Type'] == 'Input'])}")
print(f"Intermediate nodes: {len(df_nodes[df_nodes['Type'] == 'Intermediate'])}")
print(f"Output nodes: {len(df_nodes[df_nodes['Type'] == 'Output'])}")
