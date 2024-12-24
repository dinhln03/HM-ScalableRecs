from datetime import timedelta

from feast import Entity, FeatureService, FeatureView, Field, PushSource
from feast.infra.offline_stores.contrib.postgres_offline_store.postgres_source import (
    PostgreSQLSource,
)
from feast.types import Float32, Int64, String

# Define an entity for the user. You can think of an entity as a primary key used to
# fetch features.
user = Entity(name="user", join_keys=["customer_id"])

# Define the PostgreSQL source for the new data
user_item_interactions = PostgreSQLSource(
    name="user_item_interactions",
    query="SELECT * FROM oltp.transactions",
    timestamp_field="t_dat",
)

schema = [
    Field(name="article_id", dtype=String),
]

# Define the new Feature View for user rating stats
user_rating_stats_fv = FeatureView(
    name="user_item_interactions",
    entities=[user],
    ttl=timedelta(
        days=10000
    ),  # Define this to be very long for demo purpose otherwise null data
    schema=schema,
    online=True,
    source=user_item_interactions,
)

# Example FeatureService with the new Feature View
user_activity_v1 = FeatureService(
    name="user_item_interactions_v1",
    features=[
        user_rating_stats_fv,
    ],
)