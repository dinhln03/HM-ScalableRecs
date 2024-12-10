import pandas as pd
from typing import List

def parse_dt(df: pd.DataFrame, cols: List = ["t_dat"]):
    return df.assign(
        **{
            col: lambda df: pd.to_datetime(df[col].astype(object))
            for col in cols
        }
    )
