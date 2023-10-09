b站视频 ：https://www.bilibili.com/video/BV1Bh4y1V7Sd

----

## register_buffer、register_parameter <!-- {docsify-ignore} -->



## 1、register_parameter()
register_parameter() 是 torch.nn.Module 类中的一个方法



### 1.1、 作用与性质
- 用于定义<mark>可学习参数</mark>
- 定义的参数可被保存到网络对象的参数中，可使用 `net.parameters()` 或 `net.named_parameters()` 查看
- 定义的参数可用 `net.state_dict()` 转换到字典中，进而 保存到网络文件 / 网络参数文件中



### 1.2、函数说明
```python
register_parameter(name，param)
```

参数：

- `name`：参数名称

- `param`：参数张量， 须是 `torch.nn.Parameter()` 对象 或 None ，否则报错如下

`TypeError: cannot assign 'torch.FloatTensor' object to parameter 'xx' (torch.nn.Parameter or None required) `



### 1.3、使用举例

```python
import torch
import torch.nn as nn


class MyModule(nn.Module):
    def __init__(self):
        super(MyModule, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=6, kernel_size=3, stride=1, padding=1, bias=False)
        self.conv2 = nn.Conv2d(in_channels=6, out_channels=9, kernel_size=3, stride=1, padding=1, bias=False)

        self.register_parameter('weight', torch.nn.Parameter(torch.ones(10, 10)))
        self.register_parameter('bias', torch.nn.Parameter(torch.zeros(10)))


    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x * self.weight + self.bias
        return x


net = MyModule()

for name, param in net.named_parameters():
    print(name, param.shape)

print('\n', '*'*40, '\n')

for key, val in net.state_dict().items():
    print(key, val.shape) 作者：Enzo_Mi https://www.bilibili.com/read/cv25270794/ 出处：bilibili
```

---

<br />

## 2、register_buffer()
register_buffer()是 torch.nn.Module() 类中的一个方法



### 2.1 、作用与性质
- 用于定义<mark>不可学习的参数</mark>
- 定义的参数<mark>不会被</mark>保存到网络对象的参数中，使用 `net.parameters()` 或 `net.named_parameters()` 查看不到
- 定义的参数可用 `net.state_dict()` 转换到字典中，进而 保存到网络文件 / 网络参数文件中



`register_buffer()` 用于在网络实例中 注册缓冲区，存储在缓冲区中的数据，类似于参数（但不是参数），它与参数的区别为：

- 参数：可以被优化器更新  （requires_grad=False / True）

- buffer 中的数据 ： 不会被优化器更新



### 2.2、函数说明
```python
register_buffer(name，tensor)
```

- `name`：参数名称

- `tensor`：张量



### 2.3、使用举例

```python
import torch
import torch.nn as nn


class MyModule(nn.Module):
    def __init__(self):
        super(MyModule, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=6, kernel_size=3, stride=1, padding=1, bias=False)
        self.conv2 = nn.Conv2d(in_channels=6, out_channels=9, kernel_size=3, stride=1, padding=1, bias=False)

        self.register_buffer('weight', torch.ones(10, 10))
        self.register_buffer('bias', torch.zeros(10))


    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x * self.weight + self.bias
        return x


net = MyModule()

for name, param in net.named_parameters():
    print(name, param.shape)

print('\n', '*'*40, '\n')

for key, val in net.state_dict().items():
    print(key, val.shape)
```

































