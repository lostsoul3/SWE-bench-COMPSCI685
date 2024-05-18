import pandas as pd

# Load the CSV file
# f_name = 'outputs/gemma7b_finetuned_model_output-gemma7b_finetuned_model_output.csv'
f_name = 'outputs/swe_llama_outputs.csv'
df = pd.read_csv(f_name, delimiter=',')

# Extract the 'query' and 'generated_query' columns, ensuring they are treated as strings
queries = df['query'].astype(str).str.strip()
generated_queries = df['generated_query'].astype(str).str.strip()

no_join_count_queries = []
false_join_queries = []

# Initialize counters
no_join_count = 0
false_join_count = 0

# Iterate through the queries and count the occurrences
for i in range(len(queries)):
    if 'join' in (queries[i]).lower() and 'join' not in (generated_queries[i]).lower():
        no_join_count += 1
    elif 'join' not in (queries[i]).lower() and 'join' in (generated_queries[i]).lower():
        false_join_count += 1

# Print the results
print(false_join_count)
print(f"No join count: {no_join_count/1034}")
print(f"False join count: {false_join_count/1034}")
