from datetime import datetime
import pandas as pd

from feast import FeatureStore

store = FeatureStore(repo_path="/home/dinhln/Desktop/MLOPS/recsys/HM-ScalableRecs/feature-pipeline/feature_store/staging")
entity_df = pd.DataFrame.from_dict(
    {
        "customer_id": ["9597d90d698f0d1d760eefdfc7c39809c5557108133b3b9c52b36351a6106296"],
        "event_timestamp": [
            datetime(2018, 9, 20, 0, 0, 0),
        ]
    }
)
training_df = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "user_item_interactions:article_id"
    ],
).to_df()
print(training_df)
print("Fetch with entity_df:\n",training_df.loc[lambda df: df["customer_id"] == "9597d90d698f0d1d760eefdfc7c39809c5557108133b3b9c52b36351a6106296"].loc[lambda df: df["article_id"] == 568861005])


entity_sql = f"""
    SELECT
        customer_id,
        t_dat AS event_timestamp
    FROM {store.get_data_source("user_item_interactions").get_table_query_string()}
    WHERE t_dat = '2018-9-20' 
"""

raw_df = store.get_historical_features(
    entity_df=entity_sql,
    features=["user_item_interactions:article_id"],
).to_sql()
print(raw_df)
print("Fetch with entity_sql to get interactions in a period:\n",raw_df.loc[lambda df: df["customer_id"] == "9597d90d698f0d1d760eefdfc7c39809c5557108133b3b9c52b36351a6106296"].loc[lambda df: df["article_id"] == 568861005])