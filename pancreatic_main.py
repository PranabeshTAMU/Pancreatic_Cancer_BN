import numpy as np
import pandas as pd
import itertools
from itertools import combinations
from pancreatic_single_fault import pancreatic_single_fault
from pancreatic_two_faults import pancreatic_two_faults
from pancreatic_three_faults import pancreatic_three_faults

drugs = ['palmatine', 'berberine', 'abraxane', 'gemcitabine', 'gefitinib', 'dacomitinib', 'afatinib', 'GANT61']

#num_drugs = int(input("Enter the number of drugs in each combination (0-4): "))
n = num_drugs = 4 #num_drugs=
A = np.zeros((50,256))

for i in range (50): # goes from fault 0 to 41
    for d1 in range(2):
        for d2 in range(2):
            for d3 in range(2):
                for d4 in range(2):
                    for d5 in range(2):
                        for d6 in range(2):
                            for d7 in range(2):
                                for d8 in range(2):
                                    m = 128 * d1 + 64 * d2 + 32 * d3 + 16 * d4 + 8 * d5 + 4 * d6 + 2 * d7 + d8 + 1
                                    if d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 <= n:
                                        A[i,m] = pancreatic_single_fault(i, d1, d2, d3, d4, d5, d6, d7, d8)
A = np.sum(A, axis=0)  # Summing the measures across all faults 
A = A[np.newaxis, :]  # Adding a new axis to make it 
A = A[:, np.any(A, axis=0)]  # Removing the zero columns 
A = A / np.max(np.abs(A))  # Normalizing the measure
A = np.transpose(A)  # Transposing to 

# Overall measure for two fault network
B = np.zeros((50, 50, 256))
for i in range (50): # goes from fault 0 to 41
    for j in range(50): # goes from fault 0 to 41
        for d1 in range(2):
            for d2 in range(2):
                for d3 in range(2):
                    for d4 in range(2):
                        for d5 in range(2):
                            for d6 in range(2):
                                for d7 in range(2):
                                    for d8 in range(2):
                                        m = 128 * d1 + 64 * d2 + 32 * d3 + 16 * d4 + 8 * d5 + 4 * d6 + 2 * d7 + d8 + 1
                                        if d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 <= n:                                                    
                                            B[i, j, m] = pancreatic_two_faults(i, j, d1, d2, d3, d4, d5, d6, d7, d8)
B = np.sum(np.sum(B, axis=0), axis=0)  # Summing the measures across all faults
B = B[np.newaxis, :]  # Adding a new axis to make it 
B = B[:, np.any(B, axis=0)]  # Removing the zero columns 
B = B / np.max(np.abs(B))  # Normalizing the measure
B = np.transpose(B)  # Transposing to 

C = np.zeros((50, 50, 50, 256))

# Generate all possible combinations of drugs
#drug_combinations = list(itertools.product([0, 1], repeat=12))

# "i", "j", "k" iterate over faults
for i in range(50):
    for j in range(50):
        for k in range(50):
            for d1 in range(2):
                for d2 in range(2):
                    for d3 in range(2):
                        for d4 in range(2):
                            for d5 in range(2):
                                for d6 in range(2):
                                    for d7 in range(2):
                                        for d8 in range(2):
                                            m = 128 * d1 + 64 * d2 + 32 * d3 + 16 * d4 + 8 * d5 + 4 * d6 + 2 * d7 + d8 + 1
                                            if d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 <= n:                                                                     
                                                C[i,j,k,m] = pancreatic_three_faults(i, j, k, d1, d2, d3, d4, d5, d6, d7, d8)

C = np.sum(np.sum(np.sum(C, axis=0), axis=0), axis=0)  # Summing the measures across different faults 
C = C[np.newaxis, :]  # Adding a new axis to make it 
C = C[:, np.any(C, axis=0)]  # Removing the zero columns 
C = C / np.max(np.abs(C))  # Normalizing the measure
C = np.transpose(C)  # Transposing 

if num_drugs < 0 or num_drugs > 8:
    print("Invalid input. Please enter a number between 0 and 8.")
else:
    # Define the drug names
# Initialize the output list with 'Untreated'
    output_list = ["Untreated"]

# Iterate through the nested loops to generate drug combinations
for d1 in range(2):
   for d2 in range(2):
       for d3 in range(2):
           for d4 in range(2):
               for d5 in range(2):
                   for d6 in range(2):
                       for d7 in range(2):
                           for d8 in range(2):
                                    # Create an empty combination
                                combination = []

                                # Append individual drugs if the corresponding variable is 1
                                if d1:
                                    combination.append(drugs[0])
                                if d2:
                                    combination.append(drugs[1])
                                if d3:
                                    combination.append(drugs[2])
                                if d4:
                                    combination.append(drugs[3])
                                if d5:
                                    combination.append(drugs[4])
                                if d6:
                                    combination.append(drugs[5])
                                if d7:
                                    combination.append(drugs[6])
                                if d8:
                                    combination.append(drugs[7])
                                                   
                                # Add the combination to the output list with formatting
                                if combination and len(combination) <= n:
                                    output_list.append("{}".format(' + '.join(combination)))
combo_array = np.array(output_list)
# Print the output list
    #for combo in output_list:
        #print(combo)
    #output_one_fault = np.column_stack((combo_array, A))
    #output_two_faults = np.column_stack((combo_array, B))
    #output_three_faults = np.column_stack((combo_array, C))
output = np.column_stack((combo_array, A, B, C))    
    
