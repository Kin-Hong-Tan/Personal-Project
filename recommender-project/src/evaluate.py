\"\"\"Evaluation functions for recommender models.\"\"\"
from lightfm.evaluation import precision_at_k, recall_at_k

def evaluate_model(model, interaction_matrix, k=10):
    precision = precision_at_k(model, interaction_matrix, k=k).mean()
    recall = recall_at_k(model, interaction_matrix, k=k).mean()
    print(f'Precision@{k}: {precision:.4f}')
    print(f'Recall@{k}: {recall:.4f}')
    return precision, recall
