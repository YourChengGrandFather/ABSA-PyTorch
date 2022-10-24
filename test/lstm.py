import torch.nn as nn
import torch

class TD_LSTM(nn.Module):
	def __init__(self):
		super().__init__()
		self.rnn = nn.LSTM(10, 20, 3) # params: embedding, hidden_size, num_layers
	def forward(self):
		input = torch.randn(5, 3, 10)
		h0 = torch.randn(2, 3, 20)
		c0 = torch.randn(2, 3, 20)
		output, (hn, cn) = self.rnn(input, (h0, c0))
		print('output==hn', output[-1,:,:]==hn[-1])

model = TD_LSTM()
for i in model.parameters():
	print(i.size())














def _reset_params(model):
	for child in model.children():
		print('child-->', child, type(child))
		i = 0
		for p in child.parameters():
			i=i+1
			print('i-->',i)
			print('p-->', p)
	# 		if p.requires_grad:
	# 			if len(p.shape) > 1:
	# 				opt.initializer(p)
	# 			else:
	# 				stdv = 1. / math.sqrt(p.shape[0])
	# 				torch.nn.init.uniform_(p, a=-stdv, b=stdv)

# _reset_params(model)