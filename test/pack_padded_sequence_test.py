import torch
a = torch.ones(25, 300)
b = torch.ones(22, 300)
c = torch.ones(15, 300)
x = [a,b,c]
data = torch.nn.utils.rnn.pad_sequence(x, batch_first=True)
len = [len(i) for i in x]
print(len)
print('data-->', data.shape)
a = torch.nn.utils.rnn.pack_padded_sequence(data,len,batch_first=True)
print('a-->',a[0].shape)
b = torch.nn.utils.rnn.pad_packed_sequence(a,batch_first=True)
print('b-->',b[0].shape)

x_len = torch.tensor([1,4,3])
x_sort_idx = torch.sort(x_len)[1].long()
print('x_sort_idx-->',x_sort_idx)
x_unsort_idx = torch.sort(x_sort_idx)[1].long()
print('x_unsort_idx-->',x_unsort_idx)