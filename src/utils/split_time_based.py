from datetime import timedelta

from loguru import logger

def train_test_split_timebased(
        interaction_df,
        args,
        user_id_col="customer_id",
        timestamp_col="t_dat",
        remove_unseen_in_test = True,
):
    max_date = interaction_df[timestamp_col].max().date()
    val_date = max_date - timedelta(days=args.test_num_days)
    train_date = val_date - timedelta(days=args.val_num_days)

    val_date_str = val_date.strftime("%Y-%m-%d")
    train_date_str = train_date.strftime("%Y-%m-%d")

    test_df = interaction_df[interaction_df[timestamp_col] >= val_date_str]
    val_df = interaction_df.loc[lambda df: (df[timestamp_col] >= train_date_str) & (df[timestamp_col] < val_date_str)]
    train_df = interaction_df[interaction_df[timestamp_col] < train_date_str]

    if remove_unseen_in_test:
        logger.info("Removing users from val and test sets...")
        train_users = train_df[user_id_col].unique()
        val_user_origins = val_df[user_id_col].unique()
        test_user_origins = test_df[user_id_col].unique()
        val_df = val_df[val_df[user_id_col].isin(train_users)]

        # Do split
        val_df = val_df[val_df[user_id_col].isin(train_users)]
        test_df = test_df[test_df[user_id_col].isin(train_users)]

        logger.info(
            f"Removed {len(val_user_origins) - len(val_df[user_id_col].unique())} users from val set"
        )
        logger.info(
            f"Removed {len(test_user_origins) - len(test_df[user_id_col].unique())} users from test set"
        )
        logger.info(f"Train set has {len(train_users)} users")
        logger.info(f"Val set has {len(val_df[user_id_col].unique())} users")
        logger.info(f"Test set has {len(test_df[user_id_col].unique())} users")
        assert set(val_df[user_id_col].unique()).issubset(set(train_users)), "Val set has unseen users"
    return train_df, val_df, test_df