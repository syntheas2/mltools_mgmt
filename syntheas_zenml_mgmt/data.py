from zenml.client import Client


def get_df_train():
    artifact = Client().get_artifact_version(
        "231c9e02-0d29-41d3-b6f8-473216cfeaa2")
    return artifact.load()


def get_df_test():
    artifact = Client().get_artifact_version(
        "cc4de8d3-e8d3-41ca-8b31-190dcc165634")
    return artifact.load()


def get_df_val():
    artifact = Client().get_artifact_version(
        "647b8521-2462-4a7b-bbb7-da4888f8ac85")
    return artifact.load()