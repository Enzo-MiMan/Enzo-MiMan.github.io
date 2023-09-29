### 1、简介

1）nn.Sequential 、 nn.ModuleList 、 nn.ModuleDict 类都继承自 Module 类。

2）nn.Sequential、nn.ModuleList 和 nn.ModuleDict语法

```python
net = nn.Sequential(nn.Linear(32, 64), nn.ReLU())

net = nn.ModuleList([nn.Linear(32, 6)4, nn.ReLU()])

net = nn.ModuleDict({'linear': nn.Linear(32, 64), 'act': nn.ReLU()})
```



----



### 2、Sequential 、ModuleDict、 ModuleList 的区别

  1）ModuleList 仅仅是一个储存各种模块的列表，这些模块之间没有联系也没有顺序（所以不用保证相邻层的输入输出维度匹配），而且没有实现 forward 功能需要自己实现

  2）和 ModuleList 一样， ModuleDict 实例仅仅是存放了一些模块的字典，并没有定义 forward 函数需要自己定义

  3）而 Sequential 内的模块需要按照顺序排列，要保证相邻层的输入输出大小相匹配，内部 forward 功能已经实现，所以，直接如下写模型，是可以直接调用的，不再需要写forward，sequential 内部已经有 forward

```python
import torch
import torch.nn as nn

net1 = nn.Sequential(nn.Linear(32, 64), nn.ReLU())
net2 = nn.ModuleList([nn.Linear(32, 64), nn.ReLU()])
net3 = nn.ModuleDict({'linear': nn.Linear(32, 64), 'act': nn.ReLU()})

# print(net1)
# print(net2)
# print(net3)

x = torch.randn(8, 3, 32)
print(net1(x).shape)
# print(net2(x).shape)  # 会报错，提示缺少forward
# print(net3(x).shape)   # 会报错，提示缺少forward
```



为 nn.ModuleList 写 forward 函数

```python
import torch
import torch.nn as nn


class My_Model(nn.Module):
    def __init__(self):
        super(My_Model, self).__init__()
        self.layers = nn.ModuleList([nn.Linear(32, 64),nn.ReLU()])

    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

net = My_Model()

x = torch.randn(8, 3, 32)
out = net(x)
print(out.shape)
```



为 nn.ModuleDict 写 forward 函数

```python
import torch
import torch.nn as nn


class My_Model(nn.Module):
    def __init__(self):
        super(My_Model, self).__init__()
        self.layers = nn.ModuleDict({'linear': nn.Linear(32, 64), 'act': nn.ReLU()})

    def forward(self, x):
        for layer in self.layers.values():
            x = layer(x)
        return x

net = My_Model()
x = torch.randn(8, 3, 32)
out = net(x)
print(out.shape)
```



将 nn.ModuleList 转换成 nn.Sequential

```python
import torch
import torch.nn as nn

module_list = nn.ModuleList([nn.Linear(32, 64), nn.ReLU()])
net = nn.Sequential(*module_list)
x = torch.randn(8, 3, 32)
print(net(x).shape)
```



将 nn.ModuleDict 转换成 nn.Sequential

```python
import torch
import torch.nn as nn

module_dict = nn.ModuleDict({'linear': nn.Linear(32, 64), 'act': nn.ReLU()})
net = nn.Sequential(*module_dict.values())
x = torch.randn(8, 3, 32)
print(net(x).shape)
```



----



### 3、ModuleDict、 ModuleList 的区别

  1）ModuleDict 可以给每个层定义名字，ModuleList 不会

  2）ModuleList 可以通过索引读取，并且使用 append 添加元素

```python
import torch.nn as nn

net = nn.ModuleList([nn.Linear(32, 64), nn.ReLU()])
net.append(nn.Linear(64, 10))
print(net)
```

  3）ModuleDict 可以通过 key 读取，并且可以像 字典一样添加元素

```python
import torch.nn as nn

net = nn.ModuleDict({'linear1': nn.Linear(32, 64), 'act': nn.ReLU()})
net['linear2'] = nn.Linear(64, 128)
print(net)
```







### 4、nn.ModuleList 、 nn.ModuleDict 与 Python  list、Dict 的区别

加入到 ModuleList 、ModuleDict  里面的所有模块的参数会被自动添加到整个网络中。

```python
import torch.nn as nn

net = nn.ModuleList([nn.Linear(32, 64), nn.ReLU()])

for name, param in net.named_parameters():
    print(name, param.size())
```

```python
import torch.nn as nn

net = nn.ModuleDict({'linear': nn.Linear(32, 64), 'act': nn.ReLU()})

for name, param in net.named_parameters():
    print(name, param.size()) 
```

