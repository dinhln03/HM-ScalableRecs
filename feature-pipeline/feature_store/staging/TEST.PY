from datetime import datetime
import pandas as pd

from feast import FeatureStore

store = FeatureStore(repo_path=".")
import time
# Sleep 10 seconds to allow the feature store to start and print the time sleeped
print("Sleeping for 10 seconds to allow the feature store to start")
for i in range(10):
    print(f"Sleeped {i} seconds")
    time.sleep(1)

entity_rows = [
        # {join_key: entity_value}
        {"customer_id": "002f0f63ede7b86c5226830252ffc07c6790d0b7ce6857965a6986de66475497"},
        {"customer_id": "00354ba5a0a8d4841ed8629ddd90c2fe7955b54d78d994f4fe3574ecbfc7a9a3"},
        {"customer_id": "00584c1f1ccf82af69e5843539f311516c49cd4101d3d07ec787fdd908a356b8"},
        {"customer_id": "075b6dc9d06ac41d44f4f5a848888f47e4ae04db8aa90a6253a6a3ab652d69e9"},
        {"customer_id": "0c6a37c6008e0740828502652ab3c7120b68d27a26fee734a9dee0f121997924"},
        {"customer_id": "0c6a37c6008e0740828502652ab3c7120b68d27a26fee734a9dee0f121997924"}
    ]

features_to_fetch = [
            "user_item_interactions:price",
        ]
returned_features = store.get_online_features(
        features=features_to_fetch,
        entity_rows=entity_rows,
    ).to_dict()

print(returned_features)