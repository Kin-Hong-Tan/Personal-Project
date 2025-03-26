import pandas as pd
from scipy.sparse import coo_matrix

def load_data(interactions_path, metadata_path):
    interactions = pd.read_csv(interactions_path)
    metadata = pd.read_csv(metadata_path)
    return interactions, metadata

def create_interaction_matrix(interactions, user_col, item_col, rating_col=None):
    user_ids = interactions[user_col].astype('category').cat.codes
    item_ids = interactions[item_col].astype('category').cat.codes
    
    if rating_col:
        ratings = interactions[rating_col].astype(float)
    else:
        ratings = [1.0] * len(interactions)
    
    interaction_matrix = coo_matrix((ratings, (user_ids, item_ids)))
    return interaction_matrix, user_ids, item_ids