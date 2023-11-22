

b站视频 ：

（一）安装与登录 ：https://www.bilibili.com/video/BV1Cu4y1a7qD

（二）基础使用与可视化： https://www.bilibili.com/video/BV1694y1G7dy





----



# 日志记录 - wandb <!-- {docsify-ignore} -->



## 简介

wandb 是一个用于跟踪、可视化和协作机器学习项目的工具。它可以帮助用户记录模型训练过程中的超参数和输出指标，然后可视化和比较结果，并快速与同事共享结果。

官网地址 ： https://wandb.ai/site

<img src="https://p.ipic.vip/ofw8wa.png" alt="image-20230924213456548" style="zoom:25%;" style="left;"/>



![image-20231025134249818](https://p.ipic.vip/s2yu6j.png)

----



## 安装  与 登录

### Step 1 : 安装

```Python
pip install wandb
```

### Step 2 : 注册账号并登录

在官网 https://wandb.ai/site ，注册一个账号并登录

<img src="https://p.ipic.vip/ofw8wa.png" alt="image-20230924213456548" style="zoom: 19%;" style="left;"/>



### Step 3 : 客户端登录

在你的项目的 shell 中输入 ：

```
wandb login
```

![image-20231025122004758](https://p.ipic.vip/52m8mw.png)

点击如上色框框起来的链接，会跳转到如下网页，点击复制 key

![image-20231025122317450](https://p.ipic.vip/klepaz.png)

回到 shell，control + v  并回车 

wandb 就会提示你，你的 key 已经被存到了 .netrc 的文件中，此时你就已经登录成功了

![image-20231025122835515](https://p.ipic.vip/9why7w.png)

接下来，你就可以在代码中直接调用 wandb 的 api，相关数据就会直接上传到 wandb 云端啦

<br />

---

<br />

### 运行中遇到错误

若代码运行时，遇到如下报错

```Python
wandb.errors.UsageError: api_key not configured (no-tty). call wandb.login(key=[your_api_key])
```

需要重新设置一下wandb，在终端输入如下命令：

```Python
wandb init
```

然后你会看到如下提示，点击红色框框起来的链接

<img src="https://p.ipic.vip/j72kq7.png" alt="img" style="zoom: 50%;" style="left;" />

按照提示 sign in 或 sign up，注册并且登录之后，重新点击上方链接，会看到如下的key，复制 key

<img src="https://p.ipic.vip/k45vem.png" alt="img" style="zoom:30%;" style="left;" />

然后回到终端 control+v 粘贴， 然后回车

接下来会提示你输入一个项目名，你自己起一个项目名，然后回车

<img src="https://p.ipic.vip/3uzkjh.png" alt="img" style="zoom:50%;" style="left;" />

如果碰到如下报错

![img](https://p.ipic.vip/plaf2d.png)

检查代码中是否有 `entity`  参数，若有，将 `entity` 参数注释掉 （ `entity` 是你的用户名/团队名，如果你没有该用户/团队权限，就会报如上的错误）

<img src="https://p.ipic.vip/cmc34w.png" alt="img" style="zoom:50%;" style="left;" />



<br />

-----



<br />

## 基础使用 与 可视化

### 1、举例

官网 Tutorials : https://docs.wandb.ai/tutorials/experiments

```python
import wandb
import random
import datetime


run_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
wandb.init(
    project="wandb_demo",       # 项目名
    name=f"run-{run_name}",     # 本次 run 的名称
    config={                    # 记录需要跟踪的超参数
        "learning_rate": 0.02,
        "architecture": "CNN",
        "dataset": "CIFAR-100",
        "epochs": 10,
    })

# 模拟训练过程，并记录相关指标 ： acc， loss
epochs = 10
offset = random.random() / 5
for epoch in range(2, epochs):
    acc = 1 - 2 ** -epoch - random.random() / epoch - offset
    loss = 2 ** -epoch + random.random() / epoch + offset

    # 记录相关指标
    wandb.log({"acc": acc, "loss": loss})

# 结束 wandb
wandb.finish()
```

- `wandb.init()`
- `wandb.log()`
- `wandb.finish()`



<br />

<br />



### 2、常用函数

官方文档地址 ： https://docs.wandb.ai/ref/python

#### 1）wandb.init()

这个函数的作用与平常定义类里面的init函数作用类似，都是起初始化的作用。

`wandb.init()` 中有20多个参数，这里只列出几个重要的，加以解释：

  ```python
wandb.init(project='project',
           entity='team_name',
           name='run_name',
           config=config)
  ```

1. `project`：用于指定项目名称

   wandb 在运行的过程中会自动帮你创建一个以此命名的项目文件，run 结果 都会存放在这个项目文件里。

   如果没有指定项目名称，run 结果 会放在一个 "Uncategorized" 未分类项目中

2. `entity` :  用户名或团队名称 (可以是团队或组织的名称，也可以是团队或组织的 ID)，你可以将本次run 的记录发送到这个指定的用户名下 或 团队下。如果没有指定 entity，则记录将被发送到 您的用户名下。

3. `name`：此次run的名称。不设置的话，默认情况下，会生成一个随机的两个单词的名称，

4. `conifg`： 用于记录训练配置、超参数。传入的数据格式为 字典



举例 ：

```python
wandb.init(
    project="wandb_demo",       # 项目名
    name=f"run-{run_name}",     # 本次 run 的名称
    config={                    # 记录需要跟踪的超参数
        "learning_rate": 0.02,
        "architecture": "CNN",
        "dataset": "CIFAR-100",
        "epochs": 10,
    })
```



![image-20231031134602980](https://p.ipic.vip/433cyr.png)



<br />

<br />

#### 2）wandb.config()

`wandb.config()` 用于保存训练配置，这些配置包含超参数、数据集名称、模型类型 等等

- 可以在 `wandb.init() ` 中对 config 进行定义
- 之后可以使用 `wandb.config.update()`  对 config 进行追加。它将传入的键值对追加到 config 中。如果传入的键值对中包含已经存在的键，则将新值覆盖旧值。

- 如果在`wandb.init() ` 中没有设置 conifg，那么就使用 `wandb.config.update()` 进行具体内容的输入。

举例：

```python
import wandb
import datetime

run_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
wandb.init(
    project="wandb_demo",       # 项目名
    name=f"run-{run_name}",     # 本次 run 的名称
    config={                    # 记录需要跟踪的超参数
        "learning_rate": 0.02,
        "architecture": "CNN",
        "dataset": "CIFAR-100",
        "epochs": 10,
    })

print(wandb.config.learning_rate)   # 0.02
print(wandb.config.epochs)   # 10

wandb.config.update({"batch_size": 64})
print(wandb.config.batch_size)

# 结束 wandb
wandb.finish()
```

![image-20231031140100126](https://p.ipic.vip/cpldrv.png)



<br />

<br />



#### 3）wandb.log() 

`wandb.log()` 会将数据记录到当前的历史记录，换句话说就是每次运行到这里，系统就会将log内的参数值自动上传更新，一般数据会直接绘制成表格。

```python
wandb.log({"acc": acc, 
           "loss": loss})
```

![image-20231031140150329](https://p.ipic.vip/tzxuuv.png)



![image-20231031140222588](https://p.ipic.vip/c51k43.png)

<br />

<br />

 #### 4）wandb.finish() 

用于通知 Wandb 服务器该运行已经结束，并将所有数据上传到服务器。

<br />

<br />





#### 5）wandb.watch()

```python
wandb.watch(model, log="gradients", log_freq=1000, log_graph=False)
```

- models：要监控的模型。可以是单个模型，也可以是多个模型的列表

- log：要记录的指标。可以是 "gradients"、"parameters"、"all" 或 None， 默认值为 "gradients"

  <img src="https://p.ipic.vip/xtxdnd.png" alt="image-20231105185220252" style="zoom:50%;" />

- log_freq：记录指标的频率，默认值为 1000

- log_graph：是否记录模型的图形，默认为 "False"

![image-20231105210155555](https://p.ipic.vip/uxi1of.png)



通过观察 (parameters 板块中) 参数值的分布是否趋于稳定，以及 梯度是否收敛到趋近于0，可以判断当前模型的收敛情况



代码 ： https://github.com/Enzo-MiMan/cv_related_collections/blob/main/deep_learning_basic/wandb/wandb_watch.py

<br />

<br />



#### 6）wandb.Artifact()

**版本管理、保存文件**

```python
# 将模型参数保存为本地 .pth 文件
torch.save(model.state_dict(), "lenet5.pth")

# 创建 artifact 对象
artifact = wandb.Artifact(name='lenet5-mnist', type='project')

# 通过对象, 向版本中添加 数据文件、代码文件 和 参数文件
artifact.add_dir('./MNIST')   # 添加文件夹
artifact.add_file('./wandb_artifact.py')   # 添加文件
artifact.add_file('./lenet5.pth')   # 添加文件

# 上传对象(包括代码文件 和 参数文件)
wandb.log_artifact(artifact)
```

![image-20231106221725348](https://p.ipic.vip/tnteco.png)

![image-20231107184617992](https://p.ipic.vip/g063fn.png)





**读取文件**

```python
import wandb
run = wandb.init()
artifact = run.use_artifact('enzo-mi0911/LeNet5/lenet5-mnist:v2', type='xxx')
artifact_dir = artifact.download()
```

![image-20231107184544114](https://p.ipic.vip/30uhfa.png)

<br />

<br />



----





### 3、实例 ：恢复训练

**1、重点代码片段：**

**1）初始化，指定之前的 run id，并且设置 resume = True**

```python
wandb.init(project='LeNet5', id='if8bjzd0', resume=True)
```



**2）加载模型参数**

```py
artifact = wandb.use_artifact("lenet5-mnist:v0")
model_dir = artifact.download()
model_path = os.path.join(model_dir, "lenet5.pth")
model.load_state_dict(torch.load(model_path))
```



```python
import numpy as np
import os
import torch
import torch.nn as nn
from torchvision.datasets import mnist
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import torch.optim as optim
import wandb

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
wandb.init(project='LeNet5', id='if8bjzd0', resume=True)

train_batch_size = 16
test_batch_size = 32
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize([0.5], [0.5])])

# 下载数据 & 导入数据
train_set = mnist.MNIST("./", train=True, download=True, transform=transform)
test_set = mnist.MNIST("./", train=False, transform=transform)

train_loader = torch.utils.data.DataLoader(train_set, batch_size=train_batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_set, batch_size=test_batch_size, shuffle=False)

class LeNet5(nn.Module):
    """ 使用sequential构建网络，Sequential()函数的功能是将网络的层组合到一起 """

    def __init__(self, in_channel, output):
        super(LeNet5, self).__init__()
        self.layer1 = nn.Sequential(nn.Conv2d(in_channels=in_channel, out_channels=6, kernel_size=5, stride=1, padding=2),  # (6, 28, 28)
                                    nn.Tanh(),
                                    nn.AvgPool2d(kernel_size=2, stride=2, padding=0))  # (6, 14, 14))
        self.layer2 = nn.Sequential(nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5, stride=1, padding=0),  # (16, 10, 10)
                                    nn.Tanh(),
                                    nn.AvgPool2d(kernel_size=2, stride=2, padding=0))  # (16, 5, 5)
        self.layer3 = nn.Conv2d(in_channels=16, out_channels=120, kernel_size=5)  # (120, 1, 1)
        self.layer4 = nn.Sequential(nn.Linear(in_features=120, out_features=84),
                                    nn.Tanh(),
                                    nn.Linear(in_features=84, out_features=output))

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = torch.flatten(input=x, start_dim=1)
        x = self.layer4(x)
        return x


model = LeNet5(1, 10)
model.to(device)
wandb.watch(model, log='all', log_graph=True)

lr = 0.01
num_epoches = 5
momentum = 0.8

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=lr, momentum=momentum)

artifact = wandb.use_artifact("lenet5-mnist:v0")
model_dir = artifact.download()
model_path = os.path.join(model_dir, "lenet5.pth")
model.load_state_dict(torch.load(model_path))

for epoch in range(num_epoches):

    if epoch % 5 == 0:
        optimizer.param_groups[0]['lr'] *= 0.1

    model.train()
    for i, (imgs, labels) in enumerate(train_loader):
        imgs, labels = imgs.to(device), labels.to(device)
        predict = model(imgs)
        loss = criterion(predict, labels)

        # back propagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # accurate rate
        result = torch.argmax(predict, dim=1)
        acc_num = (result == labels).sum().item()
        acc_rate = acc_num / imgs.shape[0]

        if i % 200 == 0:
            wandb.log({'epoch': epoch, 'loss': loss.item(), 'acc_rate': acc_rate})


# torch.save(model.state_dict(), "lenet5_v2.pth")
# artifact = wandb.Artifact('lenet5-mnist', type='model_param')
# artifact.add_file('./lenet5_v2.pth')
# wandb.log_artifact(artifact)
wandb.finish()
```















