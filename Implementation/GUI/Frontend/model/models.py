import torch
import torch.nn as nn

# Attention Layer
class AttentionLayer(nn.Module):
    def __init__(self, num_state, input_dim):
        super(AttentionLayer, self).__init__()
        self.kernel = nn.Linear(input_dim, num_state)
        self.bias = nn.Parameter(torch.zeros(num_state))
        self.prob_kernel = nn.Linear(num_state, 1, bias=False)

    def forward(self, x):
        attention_state = torch.tanh(self.kernel(x) + self.bias)
        logits = self.prob_kernel(attention_state).squeeze(-1)
        probs = torch.softmax(logits, dim=1)
        weighted_feature = (x * probs.unsqueeze(-1)).sum(dim=1)
        return weighted_feature

# CSI Model
class CSIModel(nn.Module):
    def __init__(self, input_dim=51, lstm_units=64, atten_units=128, output_dim=3):
        super(CSIModel, self).__init__()
        self.bilstm1 = nn.LSTM(input_dim, lstm_units, batch_first=True, bidirectional=True)
        self.bilstm2 = nn.LSTM(lstm_units * 2, lstm_units, batch_first=True, bidirectional=True)
        self.attention = AttentionLayer(atten_units, lstm_units * 2)
        self.fc = nn.Linear(lstm_units * 2, output_dim)

    def forward(self, x):
        lstm_out1, _ = self.bilstm1(x)
        lstm_out2, _ = self.bilstm2(lstm_out1)
        att_out = self.attention(lstm_out2)
        return self.fc(att_out)
