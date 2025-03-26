\"\"\"FastAPI endpoint for recommender system.\"\"\"
from fastapi import FastAPI
import numpy as np

app = FastAPI()

model = None  # Load your trained model here
user_mapping = {}  # Your user mappings here
item_mapping = {}  # Your item mappings here

@app.get(\"/recommend/{user_id}\")
def recommend(user_id: int, n: int = 10):
    user_x = user_mapping.get(user_id, None)
    if user_x is None:
        return {\"error\": \"User ID not found.\"}
    scores = model.predict(user_x, np.arange(len(item_mapping)))
    top_items = np.argsort(-scores)[:n]
    recommended_items = [item_mapping[i] for i in top_items]
    return {\"user_id\": user_id, \"recommendations\": recommended_items}
