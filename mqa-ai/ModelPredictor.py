import torch
import joblib
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

class ModelPredictor:
    def __init__(self, embedding_data, model_path):
        self.embedding_data = embedding_data
        self.model_path = model_path

    def predict_with_rf(self):
        model = joblib.load(self.model_path)
        return model.predict(self.embedding_data)

    def predict_with_mlp(self):
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model = nn.Sequential(
            nn.Linear(self.embedding_data.shape[1], 128), nn.ReLU(), nn.Dropout(0.5),
            nn.Linear(128, 64), nn.ReLU(), nn.Dropout(0.5),
            nn.Linear(64, 32), nn.ReLU(), nn.Dropout(0.5),
            nn.Linear(32, 2)
        ).to(device)
        model.load_state_dict(torch.load(self.model_path))
        model.eval()

        test_loader = DataLoader(TensorDataset(torch.tensor(self.embedding_data, dtype=torch.float32)), batch_size=32, shuffle=False)
        predictions = []
        with torch.no_grad():
            for batch in test_loader:
                predictions.extend(model(batch[0].to(device)).argmax(dim=1).cpu().tolist())
        return predictions
