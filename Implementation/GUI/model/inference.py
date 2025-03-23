
import torch
from torch.utils.data import DataLoader, Dataset
from model.models import CSIModel

class CSIDataset(Dataset):
    def __init__(self, dataframe):
        self.data = torch.tensor(dataframe.values, dtype=torch.float32)
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.data[idx], 0  # Add a dummy label if your model expects labels

class InferenceServer():
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model_path = './model/23K.pth'
        
        # Load the trained CSIModel
        self.model = CSIModel(input_dim=51, lstm_units=64, atten_units=128, output_dim=3).to(self.device)
        self.model.load_state_dict(torch.load(model_path, map_location=self.device))
        self.model.eval()

    def inference(self, dataframe, verbose=True):
        # Convert DataFrame to Dataset
        dataset = CSIDataset(dataframe)
        loader = DataLoader(dataset, batch_size=4, shuffle=False)
        pred_all = []

        with torch.no_grad():
            for data, _ in loader:
                data = data.to(self.device)
                if data.dim() == 2:  # Handle missing batch dimension
                    data = data.unsqueeze(0)
                output = self.model(data)
                pred = output.argmax(dim=1).cpu().numpy()
                pred_all.extend(pred)

        if verbose:
            print(f"Predictions: {pred_all[0]}")
            return pred_all[0]
        
