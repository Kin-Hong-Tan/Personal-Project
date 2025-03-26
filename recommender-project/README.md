# 🛍️ **E-commerce Recommender System**

## 🚀 Overview
A recommender system using **LightFM** for personalized product recommendations. This repository provides a full pipeline from synthetic data generation to deployment.

## 🗃️ Dataset
Synthetic dataset simulating user-product interactions.

## 🛠️ Tech Stack
- **Modeling:** LightFM (WARP loss)
- **Deployment:** FastAPI, Streamlit
- **Evaluation:** Precision@K, Recall@K

## 🛣️ Architecture Diagram
```mermaid
graph LR;
A[Raw Data CSV] --> B[Data Preprocessing];
B --> C[Interaction Matrix];
C --> D[LightFM Model];
D --> E[FastAPI];
E --> F[Streamlit App];

## Skeleton

recommender-project/
├── data/
│   ├── interactions.csv
│   └── metadata.csv
├── notebooks/
│   └── recommender_walkthrough.ipynb
├── src/
│   ├── data_prep.py
│   ├── model.py
│   ├── evaluate.py
│   ├── api.py
│   └── utils.py
├── app/
│   └── streamlit_app.py
├── requirements.txt
├── Dockerfile
└── README.md
