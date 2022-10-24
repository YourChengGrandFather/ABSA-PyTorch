print([1]*2)
print([1,1,1]+[0,0,0])
import torch
import logging
device  = torch.device('mps')
memory = torch.cuda.memory_allocated(device)
max_memory = torch.cuda.max_memory_allocated(device)
a = torch.tensor([1,2,1,1], device=device)
print(a)
print('memory-->', memory)
print('max_memory-->', max_memory)
logger = logging.getLogger()
print('prod-->',torch.prod(a))
logger.info('> training arguments:')