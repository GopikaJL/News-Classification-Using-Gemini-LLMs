
def create_few_shot_dataset(dataframe, samples_per_category=5):
    """
    Creates a few-shot dataset by sampling a specified number of examples from each category.
    
    Parameters:
    - dataframe (pd.DataFrame): DataFrame containing 'category' and 'text' columns.
    - samples_per_category (int): Number of samples to select from each category.
    
    Returns:
    - pd.DataFrame: A new DataFrame containing the few-shot dataset.
    """
    few_shot_data = []

    categories = dataframe['category'].unique()
    for category in categories:
        # Select samples_per_category examples for the category
        sampled_data = dataframe[dataframe['category'] == category].sample(samples_per_category, random_state=42)
        few_shot_data.append(sampled_data)
    
    few_shot_dataset = pd.concat(few_shot_data).reset_index(drop=True)
    return few_shot_dataset

few_shot_df = create_few_shot_dataset(df, samples_per_category=5)

few_shot_output_path = "/kaggle/working/few_shot_dataset.csv"
few_shot_df.to_csv(few_shot_output_path, index=False)

print(f"Few-shot dataset saved to {few_shot_output_path}")
