b站视频 ：https://www.bilibili.com/video/BV1ZH4y1f7T1

---



## torchsummary.summary   <!-- {docsify-ignore} -->

<br />

### 1）函数介绍

作用 ： 通过指定输入尺寸，来查看网络每一层的输出尺寸 和 每一层的参数数量。 <mark>只需指定 input_size 即可，不需要实际的输入数据。</mark>

```python
torchsummary.summary(model, input_size=(3, 224, 224))
```

参数：

- `model` ：要查看的网络

- `input_size` ：指定网络输入尺寸，可以指定四个维度:（B, C, H, W），也可以只指定三个维度:（C, H, W）

  $\qquad \qquad \qquad$如果仅指定三个维度的尺寸（不指定batch_size），那么每一层的输出尺寸 `output shape` 都显示为 -1

<br />

<br />

### 2）使用举例

```python
from torchsummary import summary
import torchvision.models as models

model = models.alexnet(weights=models.AlexNet_Weights.DEFAULT)
print(summary(model, (3, 224, 224)))
```

输出

```
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 64, 55, 55]          23,296
              ReLU-2           [-1, 64, 55, 55]               0
         MaxPool2d-3           [-1, 64, 27, 27]               0
            Conv2d-4          [-1, 192, 27, 27]         307,392
              ReLU-5          [-1, 192, 27, 27]               0
         MaxPool2d-6          [-1, 192, 13, 13]               0
            Conv2d-7          [-1, 384, 13, 13]         663,936
              ReLU-8          [-1, 384, 13, 13]               0
            Conv2d-9          [-1, 256, 13, 13]         884,992
             ReLU-10          [-1, 256, 13, 13]               0
           Conv2d-11          [-1, 256, 13, 13]         590,080
             ReLU-12          [-1, 256, 13, 13]               0
        MaxPool2d-13            [-1, 256, 6, 6]               0
AdaptiveAvgPool2d-14            [-1, 256, 6, 6]               0
          Dropout-15                 [-1, 9216]               0
           Linear-16                 [-1, 4096]      37,752,832
             ReLU-17                 [-1, 4096]               0
          Dropout-18                 [-1, 4096]               0
           Linear-19                 [-1, 4096]      16,781,312
             ReLU-20                 [-1, 4096]               0
           Linear-21                 [-1, 1000]       4,097,000
================================================================
Total params: 61,100,840
Trainable params: 61,100,840
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.57
Forward/backward pass size (MB): 8.38
Params size (MB): 233.08
Estimated Total Size (MB): 242.03
----------------------------------------------------------------
None
```



