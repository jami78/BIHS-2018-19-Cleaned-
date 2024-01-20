import pandas as pd

we5a= pd.read_stata('mod_we5a.dta')

#Keeping the necessary columns
we51= we5a[['a01','we5a_02_a','we5a_02_b','we5a_02_c','we5a_02_d','we5a_02_e','we5a_02_f','we5a_02_g']]

#Mapping categories to numbers
mapping_dict = {
    'Not at all': 1,
    'Small extent': 2,
    'Medium extent': 3,
    'To a high extent': 4
}
for col in we51.columns:
    if col != 'a01':
        we51[col] = we51[col].map(mapping_dict)

#Calculating the score for autonomy in personal decision within households(A) so that A= average of the non-null values of the columns for a particular record

def calculate_weighted_average(row, columns_to_sum):
    """Calculates the weighted average, handling missing values."""
    valid_values = row[columns_to_sum].dropna()  # Extract valid values
    if len(valid_values) > 0:
        sum_of_values = valid_values.sum()  # Sum valid values
        num_values = len(valid_values)  # Count valid values
        return sum_of_values / num_values  # Calculate weighted average
    else:
        return pd.NA  # Return missing value if no valid values

columns_to_sum = ['we5a_02_a', 'we5a_02_b', 'we5a_02_c', 'we5a_02_d', 'we5a_02_e', 'we5a_02_f', 'we5a_02_g']
we51['Autonomy in personal decisions in household'] = we51.apply(calculate_weighted_average, axis=1, args=(columns_to_sum,))
we51

#Dropping records with missing values

we5a = we5a.dropna(subset=['Autonomy in personal decisions in household'])