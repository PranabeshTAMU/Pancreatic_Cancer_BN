
import pandas as pd
import json

# Create drug combinations CSV (all 162 combinations up to 4 drugs)
drugs = ['palmatine', 'berberine', 'abraxane', 'gemcitabine', 'gefitinib', 'dacomitinib', 'afatinib', 'GANT61']

# Generate all drug combinations
combinations_list = []
combo_id = 0

# Add untreated
combinations_list.append({
    "Combination_ID": combo_id,
    "Num_Drugs": 0,
    "Combination": "Untreated",
    "Binary_Encoding": "00000000",
    "palmatine": 0, "berberine": 0, "abraxane": 0, "gemcitabine": 0,
    "gefitinib": 0, "dacomitinib": 0, "afatinib": 0, "GANT61": 0
})
combo_id += 1

# Generate all combinations for 1-4 drugs
for d1 in range(2):
    for d2 in range(2):
        for d3 in range(2):
            for d4 in range(2):
                for d5 in range(2):
                    for d6 in range(2):
                        for d7 in range(2):
                            for d8 in range(2):
                                num_drugs = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8
                                if 1 <= num_drugs <= 4:
                                    combo = []
                                    if d1: combo.append(drugs[0])
                                    if d2: combo.append(drugs[1])
                                    if d3: combo.append(drugs[2])
                                    if d4: combo.append(drugs[3])
                                    if d5: combo.append(drugs[4])
                                    if d6: combo.append(drugs[5])
                                    if d7: combo.append(drugs[6])
                                    if d8: combo.append(drugs[7])
                                    
                                    binary = f"{d1}{d2}{d3}{d4}{d5}{d6}{d7}{d8}"
                                    
                                    combinations_list.append({
                                        "Combination_ID": combo_id,
                                        "Num_Drugs": num_drugs,
                                        "Combination": " + ".join(combo),
                                        "Binary_Encoding": binary,
                                        "palmatine": d1, "berberine": d2, "abraxane": d3, "gemcitabine": d4,
                                        "gefitinib": d5, "dacomitinib": d6, "afatinib": d7, "GANT61": d8
                                    })
                                    combo_id += 1

df_combos = pd.DataFrame(combinations_list)
df_combos.to_csv("drug_combinations.csv", index=False)

print(f"Drug combinations CSV created: drug_combinations.csv")
print(f"Total combinations (including untreated): {len(df_combos)}")
print(f"1-drug combinations: {len(df_combos[df_combos['Num_Drugs'] == 1])}")
print(f"2-drug combinations: {len(df_combos[df_combos['Num_Drugs'] == 2])}")
print(f"3-drug combinations: {len(df_combos[df_combos['Num_Drugs'] == 3])}")
print(f"4-drug combinations: {len(df_combos[df_combos['Num_Drugs'] == 4])}")
