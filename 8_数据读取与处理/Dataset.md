Dataset 的基础使用

```python
import numpy as np
import torch
from torch.utils import data


class TestDataset(data.Dataset):
    def __init__(self):
        self.Data = np.asarray([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
        self.Label = np.asarray([9, 8, 7, 6, 5])

    def __getitem__(self, index):
        txt = torch.from_numpy(self.Data[index])
        label = torch.tensor(self.Label[index])
        return txt, label

    def __len__(self):
        return len(self.Data)


test = TestDataset()
print(test[2])
print(test.__len__())
# (tensor([3, 4]), tensor(7))
# 5

test_loader = data.DataLoader(test, batch_size=2, shuffle=False)
for i, testdata in enumerate(test_loader):
    print('i:', i)
    data, label = testdata
    print(data)
    print(label)
```







Dataset 的基础使用