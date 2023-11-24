b站视频 ：

（一）记录训练数据指标 ：https://www.bilibili.com/video/BV18w411P75R

（二）模型可视化、图像可视化： https://www.bilibili.com/video/BV1BG411U7qb





# 日志记录 - tensorboard / tensorboardX <!-- {docsify-ignore} -->





## 1、实例化 SummaryWriter 类

```python
from torch.utils.tensorboard import SummaryWriter

# 不指定任何参数，默认日志路径为, "runs/CURRENT_DATETIME_HOSTNAME"
writer = SummaryWriter()

# 通过参数 log_dir 指定日志路径
writer = SummaryWriter(log_dir="./runs/version1")

# 通过参数 comment 指定日志路径名称后缀， 与参数log_dir 同时使用，不起作用
writer = SummaryWriter(comment="_resnet")
```

参数：

- `log_dir` ：保存日志文件的路径。 
  - 如果不指定，则将使用默认路径 `"runs/CURRENT_DATETIME_HOSTNAME"` ， 类似`"Nov22_17-54-55_EnzodeMBP"`
  - 若指定，则使用指定的路径作为日志路径

- `comment` ： 指定日志文件夹名称后缀，类似 `"runs/Aug20-17-20-33_resnet"`；  与参数log_dir 同时使用，不起作用

<br />

<br />

## 2、使用各种 add 方法记录数据

### 1）使用 add_scalar 记录数字常量

```bash
writer.add_scalar(tag, scalar_value, global_step=None, walltime=None)
```
参数：
- tag : (string) 数据图表名称
- scalar_value :  (float) 需要记录的数据，通常在图表中作为 y轴的数据

- global_step : (int, optional) 训练的 step，通常在图表中作为 x轴的数据
- walltime : (float, optional) 记录生成的时间，默认为 time.time()



我们一般会使用 add_scalar 方法来记录训练过程的 loss、accuracy 等数值的变化，直观地监控训练过程。



例 1

```bash
from tensorboardX import SummaryWriter

writer = SummaryWriter('runs/scalar_example')
for i in range(10):
    writer.add_scalar('quadratic', i**2, global_step=i)
    writer.add_scalar('exponential', 2**i, global_step=i)
writer.close()

# 查看方式
# step 1 ： cd 到生成的 runs 同级目录下
# step 2 ： 在终端输入 tensorboard --logdir ./runs --port 6006
# step 3 ： 再浏览器中输入地址： http://localhost:6006/ 

```
<img src="https://p.ipic.vip/gbs3z4.png" alt="在这里插入图片描述" style="zoom: 50%;" />

例 2

```python
import numpy as np
import torch.nn as nn
import torch.optim
import matplotlib.pyplot as plt
from tensorboardX import SummaryWriter

writer = SummaryWriter(log_dir='runs')
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
writer.close()
print('done')
```

<img src="https://p.ipic.vip/fx8r5q.png" alt="在这里插入图片描述" style="zoom:33%;" />


----

<br />

<br />

### 2）使用 add_graph 记录模型结构（计算图）

```python
writer.add_graph(model, input_to_model=None, verbose=False)
```
参数
- model : 待可视化的网络模型
- input_to_model : 待输入神经网络的变量或一组变量
- verbose : 是否在控制台中打印图形结构

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
with SummaryWriter(log_dir='runs', comment='Net') as w:
    w.add_graph(model, input)
        
```
![在这里插入图片描述](https://p.ipic.vip/x1qbko.png)

----

<br />

<br />

### 3）使用 add_image 记录图像

```python
writer.add_image(tag, img_tensor, global_step=None, walltime=None, dataformats='CHW')
```
参数
- tag (string): 图像窗口名称
- img_tensor (torch.Tensor / numpy.array): 图像数据
- global_step (int, optional): 训练的 step
- walltime (float, optional): 记录发生的时间，默认为 time.time()
- dataformats (string, optional): 图像数据的格式，默认为 'CHW'，还可以是  'HWC' 或 'HW' 等

我们一般会使用 add_image 来实时观察生成式模型的生成效果，或者可视化分割、目标检测的结果，帮助调试模型

```python
from tensorboardX import SummaryWriter
from PIL import Image
import numpy as np
import os


file_name = ['image1', 'image2', 'image3']
file_list = [os.path.join('./test_images', i+'.jpg') for i in file_name]
writer = SummaryWriter('runs/image_example')
for i in range(0, 3):
    writer.add_image('images',
                     np.array(Image.open(file_list[i])),
                     global_step=i,
                     dataformats='HWC')
writer.close()
```
![在这里插入图片描述](https://p.ipic.vip/ig5xtn.png)
add_image 方法只能一次插入一张图片。如果要一次性插入多张图片，有两种方法：

 1. 使用 torchvision 中的 make_grid 方法将多张图片拼合成一张图片后，再调用 add_image 方法。 【[torchvision.make_grid 介绍](https://blog.csdn.net/weixin_37804469/article/details/126348266)】 
 2. 使用 SummaryWriter 的 add_images 方法 [官方文档]，参数和 add_image类似，在此不再另行介绍。【[官方文档](https://tensorboardx.readthedocs.io/en/latest/tensorboard.html#tensorboardX.SummaryWriter.add_images)】



<br />

<br />

---



## 3、浏览器查看结果

step 1 ： 在终端 cd 到 runs 目录所在的同级目录，

step 2 ： 输入如下命令 ， <mark>注意：路径不要加双引号</mark>

```
tensorboard --logdir ./runs --port 6006
```


step 3：在浏览器窗口输入地址：http://localhost:6006/