import pandas as pd
we2= pd.read_stata("mod_we2.dta")

#Keep necessary columns only
columns_to_drop = ['we2_01_1', 'we2_01_2', 'we2_01_31', 'we2_01_32', 'we2_01_33', 'we2_01_4', 'we2_01_5', 'we2_01_6','hhid2','hh_type','round']
we21 = we2.drop(columns_to_drop, axis=1)

#Mapping categories to numbers
mapping_dict = {
    'No input': 1,
    'Input into very few decisions': 2,
    'Input into some decisions': 3,
    'Input into most decisions/ Input into all decisions': 4
}
for col in we21.columns:
    if col != 'a01':
        we21[col] = we21[col].map(mapping_dict)
        # Remove "Decision not made/not applicable" entries
        we21 = we21[we21[col] != pd.NA]
 
#Calculating score for input in decision making for economic activity

import pandas as pd
def calculate_weighted_average(row):
    """Calculates the weighted average, handling missing values."""
    columns_to_sum = ['we2_02_1', 'we2_02_2', 'we2_02_31', 'we2_02_32', 'we2_02_33', 'we2_02_4', 'we2_02_5', 'we2_02_6']
    valid_values = row[columns_to_sum].dropna()  # Extract valid values
    if len(valid_values) > 0:
        sum_of_values = valid_values.sum()  # Sum valid values
        num_values = len(valid_values)  # Count valid values
        return sum_of_values / num_values  # Calculate weighted average
    else:
        return pd.NA  # Return missing value if no valid values

we21['weighted_average'] = we21.apply(calculate_weighted_average, axis=1)

#Calculating score for input on use of generated income

def calculate_weighted_average(row, columns_to_sum):
    """Calculates the weighted average, handling missing values."""
    valid_values = row[columns_to_sum].dropna()  # Extract valid values
    if len(valid_values) > 0:
        sum_of_values = valid_values.sum()  # Sum valid values
        num_values = len(valid_values)  # Count valid values
        return sum_of_values / num_values  # Calculate weighted average
    else:
        return pd.NA  # Return missing value if no valid values

columns_to_sum = ['we2_03_1', 'we2_03_2', 'we2_03_31','we2_03_32','we2_03_33', 'we2_03_4', 'we2_03_5', 'we2_03_6']
we21['Input on use of generated income'] = we21.apply(calculate_weighted_average, axis=1, args=(columns_to_sum,))

#Renaming column
we21=we21.rename(columns={'weighted_average':'Input in economic activity'})

#Dropping records with missing values
we2 = we2.dropna(subset=['Input in economic activity','Input on use of generated income'])

