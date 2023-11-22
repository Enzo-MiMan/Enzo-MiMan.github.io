

## 1、实例化 SummaryWriter 类

```python
from tensorboardX import SummaryWriter

# 提供一个路径，将使用该路径来保存日志
writer1 = SummaryWriter(log_dir='./runs')

# 无参数，默认使用 runs/日期时间 路径来保存日志，比如：'runs/Aug20-17-20-33'
writer2 = SummaryWriter()

# 提供一个 comment 参数，将使用 runs/日期时间-comment 路径来保存日志，比如： 'runs/Aug20-17-20-33-resnet'
writer3 = SummaryWriter(comment='_resnet')
```

---

<br />

<br />

## 2、使用各种 add 方法记录数据

### 1）使用 add_scalar 记录数字常量（可视化损失值）

```bash
add_scalar(tag, scalar_value, global_step=None, walltime=None)
```
参数：
- tag (string): 数据名称，有点像是 excel 表中 sheet 的名称
- scalar_value (float): 数字常量值；图表展示时，会作为 y轴 的值
- global_step (int, optional): 训练的 step；图表展示时，会作为 x轴 的值
- walltime (float, optional): 记录发生的时间，默认为 time.time()

需要注意，这里的 scalar_value 一定是 float 类型，如果是 PyTorch scalar tensor，则需要调用 .item() 方法获取其数值。我们一般会使用 add_scalar 方法来记录训练过程的 loss、accuracy、learning rate 等数值的变化，直观地监控训练过程。

举例

```bash
from tensorboardX import SummaryWriter

writer = SummaryWriter('runs/scalar_example')
for i in range(10):
    writer.add_scalar('quadratic', i**2, global_step=i)
    writer.add_scalar('exponential', 2**i, global_step=i)

```
<img src="https://p.ipic.vip/gbs3z4.png" alt="在这里插入图片描述" style="zoom: 50%;" />

另一个例子

```python
import numpy as np
import torch.nn as nn
import torch.optim
import matplotlib.pyplot as plt
from tensorboardX import SummaryWriter

writer = SummaryWriter(log_dir='logs', comment='Linear')
np.random.seed(100)

x_train = np.linspace(-1, 1, 100).reshape(100, 1)
y_train = 3 * x_train ** 2 + 2 + 0.2 * np.random.randn(x_train.size).reshape(100, 1)


model = nn.Linear(1, 1)
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), momentum=0.5, lr=0.01)


for epoch in range(100):
    inputs = torch.from_numpy(x_train).type(torch.FloatTensor)
    targets = torch.from_numpy(y_train).type(torch.FloatTensor)
    
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    writer.add_scalar('训练损失值', loss, epoch)
    
print('done')
```

<img src="https://p.ipic.vip/fx8r5q.png" alt="在这里插入图片描述" style="zoom:33%;" />


----

<br />

<br />

### 2）使用 add_graph 记录模型结构（计算图）

```python
add_graph(model, input_to_model=None, verbose=False, **kwargs)
```
参数
- model : 待可视化的网络模型
- input_to_model : 待输入神经网络的变量或一组变量

举例
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
![在这里插入图片描述](https://p.ipic.vip/x1qbko.png)

----

<br />

<br />

### 3）使用 add_image 记录图像

```python
add_image(tag, img_tensor, global_step=None, walltime=None, dataformats='CHW')
```
参数
- tag (string): 数据名称
- img_tensor (torch.Tensor / numpy.array): 图像数据
- global_step (int, optional): 训练的 step
- walltime (float, optional): 记录发生的时间，默认为 time.time()
- dataformats (string, optional): 图像数据的格式，默认为 'CHW'，还可以是  'HWC' 或 'HW' 等

我们一般会使用 add_image 来实时观察生成式模型的生成效果，或者可视化分割、目标检测的结果，帮助调试模型

```python
from tensorboardX import SummaryWriter
from PIL import Image
import numpy as np


file_name = ['0a0b97441050bba8e733506de4655ea1', '00a3edd22dc7859c487a64777fc8d093', '0a5b12a0f9fe595d6db6ee36b43725df']
file_list = [os.path.join('./test_images', i+'.jpg') for i in file_name]
writer = SummaryWriter('runs/image_example')
for i in range(0, 3):
    writer.add_image('images',
                     np.array(Image.open(file_list[i])),
                     global_step=i,
                     dataformats='HWC')
```
![在这里插入图片描述](https://p.ipic.vip/ig5xtn.png)
add_image 方法只能一次插入一张图片。如果要一次性插入多张图片，有两种方法：

 1. 使用 torchvision 中的 make_grid 方法将多张图片拼合成一张图片后，再调用 add_image 方法。 【[torchvision.make_grid 介绍](https://blog.csdn.net/weixin_37804469/article/details/126348266)】 
 2. 使用 SummaryWriter 的 add_images 方法 [官方文档]，参数和 add_image类似，在此不再另行介绍。【[官方文档](https://tensorboardx.readthedocs.io/en/latest/tensorboard.html#tensorboardX.SummaryWriter.add_images)】



<br />

<br />

---



## 3、浏览器查看结果

在终端 cd 到 logs目录所在的同级目录，输入如下命令

```
tensorboard --logdir ./logs --port 6006
```
<mark>注意：路径不要加双引号</mark>

在浏览器窗口输入地址：http://localhost:6006/