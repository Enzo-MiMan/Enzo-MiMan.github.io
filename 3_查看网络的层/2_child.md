b站视频 ： https://www.bilibili.com/video/BV1X8411f7q1/?p=2

----



##  net.children() 、net.named_children() <!-- {docsify-ignore} -->



### 1）net.children() 

`net.children() ` 只会输出 下一级的子层，不会再递归的输出子层的子层


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

# 查看网络的层
for layer in net.children():
    print(layer)
```

输出

```
Sequential(
  (0): Linear(in_features=3, out_features=4, bias=True)
  (1): Linear(in_features=4, out_features=3, bias=True)
)
Linear(in_features=3, out_features=6, bias=True)
Sequential(
  (0): Linear(in_features=6, out_features=7, bias=True)
  (1): Linear(in_features=7, out_features=5, bias=True)
)
```

<br />

<br />



### 2）net.named_children()

`net.named_children()` 会比 `net.children()` 多输出层名

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

# 查看网络的层，包括层名
for name, layer in net.named_children():
    print(name)
    print(layer)
    print("*"*30)
```

输出

```
layer1
Sequential(
  (0): Linear(in_features=3, out_features=4, bias=True)
  (1): Linear(in_features=4, out_features=3, bias=True)
)
******************************
layer2
Linear(in_features=3, out_features=6, bias=True)
******************************
layer3
Sequential(
  (0): Linear(in_features=6, out_features=7, bias=True)
  (1): Linear(in_features=7, out_features=5, bias=True)
)
******************************
```

