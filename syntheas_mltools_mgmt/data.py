from zenml.client import Client


def get_df_train_onhot(excluded_columns = ['id', 'combined_tks']):
    artifact = Client().get_artifact_version(
        "231c9e02-0d29-41d3-b6f8-473216cfeaa2")
    df = artifact.load()
    return exclude_columns(df, excluded_columns)


def get_df_train(excluded_columns = ['id', 'combined_tks']):
    artifact = Client().get_artifact_version(
        "b2e8a3a7-2ef7-4366-a1e7-d66ed8e9eccc")
    df = artifact.load()
    return exclude_columns(df, excluded_columns)


def get_df_test_onehot(excluded_columns = ['id', 'combined_tks']):
    artifact = Client().get_artifact_version(
        "cc4de8d3-e8d3-41ca-8b31-190dcc165634")
    df = artifact.load()
    return exclude_columns(df, excluded_columns)


def get_metadata():
    """
    Get metadata artifact.
    last updated: 30.5.2025, 12:35:34
    """
    artifact = Client().get_artifact_version(
        "abdc2657-28be-4de9-89b7-b91fb18ed12a")
    o = artifact.load()
    return o


def get_vae_train_z():
    """
    Get metadata artifact.
    last updated: 30.5.2025, 12:35:34
    """
    artifact = Client().get_artifact_version(
        "abdc2657-28be-4de9-89b7-b91fb18ed12a")
    o = artifact.load()
    return o


def get_df_val_onehot(excluded_columns = ['id', 'combined_tks']):
    artifact = Client().get_artifact_version(
        "647b8521-2462-4a7b-bbb7-da4888f8ac85")
    df = artifact.load()
    return exclude_columns(df, excluded_columns)

def get_df_val(excluded_columns = ['id', 'combined_tks']):
    artifact = Client().get_artifact_version(
        "70a238a1-87c5-43f7-8f0f-369793066315")
    df = artifact.load()
    return exclude_columns(df, excluded_columns)


def exclude_columns(df, excluded_columns=['id', 'combined_tks']):
    """
    Exclude specified columns from the DataFrame.
    
    Args:
        df (pd.DataFrame): The DataFrame to modify.
        columns (list): List of column names to exclude.
    
    Returns:
        pd.DataFrame: DataFrame with specified columns excluded.
    """
    try:
        df.drop(columns=excluded_columns, inplace=True)
    except KeyError as e:
        print(f"Warning: {e}. Some columns may not exist in the DataFrame.")
    return df