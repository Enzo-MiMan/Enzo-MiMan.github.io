

## TensorBoardX <!-- {docsify-ignore} -->



使用 `TensorBoardX` 查看网络结构，分为三个步骤：

1）实例化一个 `SummaryWriter` 对象

2）让 `SummaryWriter ` 对象调用 `add_graph` 方法来获取模型结构

3）打开浏览器查看 模型的可视化起结构



### 1）实例化 SummaryWriter

实例化 `SummaryWriter` 对象的时候，有三种指定参数的方式

```python
from tensorboardX import SummaryWriter

# 提供一个路径，将使用该路径来保存日志
writer1 = SummaryWriter(log_dir='./runs')

# 无参数，默认使用 runs/日期时间 路径来保存日志，比如：'runs/Aug20-17-20-33'
writer2 = SummaryWriter()

# 提供一个 comment 参数，将使用 runs/日期时间-comment 路径来保存日志，比如： 'runs/Aug20-17-20-33-resnet'
writer3 = SummaryWriter(comment='_resnet')

```



### 2）add_graph 函数介绍

```python
add_graph(model, input_to_model=None, verbose=False, **kwargs)
```

参数

- `model` : 待可视化的网络模型
- `input_to_model` : 待输入神经网络的变量或一组变量



### 3）浏览器查看结果

在终端 cd 到 logs目录所在的同级目录，输入如下命令

```
tensorboard --logdir ./logs --port 6006
```

注意：路径不要加双引号

在浏览器窗口输入地址：http://localhost:6006/   ， 查看模型网络结构



### 4）使用举例

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from tensorboardX import SummaryWriter

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)
        self.bn = nn.BatchNorm2d(20)
        
    def forward(self, x):
        x = F.max_pool2d(self.conv1(x), 2)
        x = F.relu(x) + F.relu(x)
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = self.bn(x)
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        x = F.softmax(x, dim=1)
        return x
    

input = torch.rand(32, 1, 28, 28)
    
model = Net()
with SummaryWriter(log_dir='logs', comment='Net') as w:
    w.add_graph(model, input)
```

![在这里插入图片描述](https://p.ipic.vip/r4y1sp.png)





