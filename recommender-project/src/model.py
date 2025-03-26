\"\"\"LightFM model training functions.\"\"\"
from lightfm import LightFM

def train_lightfm_model(interaction_matrix, loss='warp', epochs=30):
    model = LightFM(loss=loss)
    model.fit(interaction_matrix, epochs=epochs)
    return model
