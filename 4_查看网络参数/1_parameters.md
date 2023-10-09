b站视频 ：https://www.bilibili.com/video/BV1X8411f7q1?p=2

----



## net.parameters()、named_parameters() <!-- {docsify-ignore} -->

<br />

### 1）net.parameters()

`net.parameters()` 用于查看网络中的<mark>参数</mark>

```python
import torch

# 搭建网络
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = torch.nn.Sequential(
            torch.nn.Linear(3, 4),
            torch.nn.Linear(4, 3),
        )
        self.layer2 = torch.nn.Linear(3, 6)

        self.layer3 = torch.nn.Sequential(
            torch.nn.Linear(6, 7),
            torch.nn.Linear(7, 5),
        )

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        return x
      
# 构造网络对象
net = MyModel()

for param in net.parameters():
    print(param.shape)
```

输出

```
torch.Size([4, 3])
torch.Size([4])
torch.Size([3, 4])
torch.Size([3])
torch.Size([6, 3])
torch.Size([6])
torch.Size([7, 6])
torch.Size([7])
torch.Size([5, 7])
torch.Size([5])
```

<br />

<br />



### 2、net.named_parameters()

`net.parameters()` 用于查看网络中的参数名和 参数

```python
import torch

# 搭建网络
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = torch.nn.Sequential(
            torch.nn.Linear(3, 4),
            torch.nn.Linear(4, 3),
        )
        self.layer2 = torch.nn.Linear(3, 6)

        self.layer3 = torch.nn.Sequential(
            torch.nn.Linear(6, 7),
            torch.nn.Linear(7, 5),
        )

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        return x
      
# 构造网络对象
net = MyModel()

for name, param in net.named_parameters():
    print(name, param.shape)
```

```
layer1.0.weight torch.Size([4, 3])
layer1.0.bias torch.Size([4])
layer1.1.weight torch.Size([3, 4])
layer1.1.bias torch.Size([3])
layer2.weight torch.Size([6, 3])
layer2.bias torch.Size([6])
layer3.0.weight torch.Size([7, 6])
layer3.0.bias torch.Size([7])
layer3.1.weight torch.Size([5, 7])
layer3.1.bias torch.Size([5])
```



