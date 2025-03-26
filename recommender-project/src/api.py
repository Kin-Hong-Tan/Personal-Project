from fastapi import FastAPI
import numpy as np

app = FastAPI()

# Placeholder for trained model & data
model = None
user_mapping = None
item_mapping = None

@app.get("/recommend/{user_id}")
def recommend(user_id: int, n: int = 10):
    user_x = user_mapping[user_id]
    scores = model.predict(user_x, np.arange(len(item_mapping)))
    top_items = np.argsort(-scores)[:n]
    recommended_items = [item_mapping[i] for i in top_items]
    return {"user_id": user_id, "recommendations": recommended_items}