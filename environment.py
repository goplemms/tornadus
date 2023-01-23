from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class Environment:
    gcloud_project_id: str
    gcloud_pubsub_topic_id: str
    gcloud_pubsub_subscription_id: str


def getEnvironment():
    import os
    from dotenv import load_dotenv
    load_dotenv()

    env_vars = {
        "gcloud_project_id": os.getenv("GCLOUD_PROJECT_ID"),
        "gcloud_pubsub_topic_id": os.getenv("GCLOUD_PUBSUB_TOPIC_ID"),
        "gcloud_pubsub_subscription_id": os.getenv(
            "GCLOUD_PUBSUB_SUBSCRIPTION_ID")
    }

    return Environment(**env_vars)
