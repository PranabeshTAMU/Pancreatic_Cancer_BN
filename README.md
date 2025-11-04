Title:
Computational Analysis of Palmatine and Berberine Efficacy in Drug Combinations for Pancreatic Cancer Using Boolean Network Modeling - Reproducibility Package

Description:

This reproducibility package contains the complete computational implementation and datasets supporting the research article: "Computational Analysis of Palmatine and Berberine Efficacy in Drug Combinations for Pancreatic Cancer Using Boolean Network Modeling."

Overview:
Pancreatic ductal adenocarcinoma (PDAC) remains one of the most aggressive malignancies with limited effective therapeutic options. This study employs Boolean network modeling—a systems-level approach—to computationally explore the therapeutic potential of natural alkaloids (Berberine and Palmatine) in combination with established chemotherapeutic agents (Gemcitabine, Nab-paclitaxel) and targeted inhibitors (EGFR inhibitors, GANT61).

Contents:

Python Code (4 main scripts):

pancreatic_main.py: Main simulation controller

pancreatic_single_fault.py: Single mutation analysis (49 scenarios)

pancreatic_two_faults.py: Double mutation analysis (1,176 scenarios)

pancreatic_three_faults.py: Triple mutation analysis (18,424 scenarios)

Data Files (4 CSV datasets):

network_nodes.csv: 69-node Boolean network topology with 12 external inputs, 8 outputs, and 49 intermediate nodes

fault_position_table_with_references-S2.csv: 49 driver mutation positions (KRAS, TP53, SMAD4, LKB1, BRCA2)

drug_combinations.csv: 162 unique drug combinations tested

drug_target_table_with_pathways-S1.csv: Drug-target interactions and pathway affiliations

Documentation:

README.md: Quick-start guide and repository overview

USER_GUIDE.md: Detailed installation and usage instructions

requirements.txt: Python dependencies (NumPy, Pandas, SciPy, Matplotlib)

environment.yml: Conda environment specification

Execution Scripts:

Shell scripts for running individual or complete analyses

Python validation script for installation verification

Key Findings:

The top-ranked three-drug combination (Berberine + Nab-paclitaxel + Gemcitabine) demonstrated superior Boolean network restoration with NMSD = 0.02

Natural alkaloids show synergistic effects when combined with chemotherapy and targeted agents

Results indicate promising therapeutic avenues for further experimental validation

Methodology:

Network Model: 69-node Boolean regulatory network

Analysis Type: Fault tolerance analysis simulating driver mutations

Similarity Metric: Normalized Mean Square Deviation (NMSD)

Drug Screening: Systematic evaluation of 162 drug combinations across single, double, and triple fault scenarios

System Requirements:

Python 3.8 or higher

4 GB RAM (minimum)

Unix/Linux or macOS (Windows with WSL2)

Estimated runtime: 2-3 hours for complete analysis

Usage:


bash
# Quick start pip install -r requirements.txt bash scripts/run_all.sh

Keywords:
Boolean networks, systems biology, pancreatic cancer, drug combination, Berberine, Palmatine, computational modeling, network pharmacology, cancer therapeutics

License:
MIT License

Author:
Pranabesh Bhattacharjee¹*, Aniruddha Datta¹

¹ Department of Electrical and Computer Engineering, Texas A&M University, College Station, TX, USA

Contact:
p.bhattacharjee@tamu.edu
## Repository Structure

pancreatic-cancer-boolean-network/
├── README.md ✅
├── LICENSE ✅
├── .gitignore ✅
├── requirements.txt ✅
├── environment.yml ✅
│
├── code/
│   ├── pancreatic_main.py ✅
│   ├── pancreatic_single_fault.py ✅
│   ├── pancreatic_two_faults.py ✅
│   ├── pancreatic_three_faults.py ✅
│   └── utils.py (placeholder)
│
├── data/
│   ├── network_nodes.csv ✅
│   ├── fault_position_table_with_references-S2.csv ✅
│   ├── drug_combinations.csv ✅
│   └── drug_target_table_with_pathways-S1.csv ✅
│
├── scripts/
│   ├── run_all.sh ✅
│   ├── run_single_fault.sh ✅
│   ├── run_two_faults.sh ✅
│   ├── run_three_faults.sh ✅
│   └── test_installation.py ✅
│
└── docs/
    └── USER_GUIDE.md ✅


