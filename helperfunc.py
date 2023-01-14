# HelperFuncitons

def explore_df(df):    
    print("Dataset Length: ", len(df))
    print("Has Null:\n", df.isna().any())
    
    return df.head()
