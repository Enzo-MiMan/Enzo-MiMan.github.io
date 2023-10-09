b站视频 ： https://www.bilibili.com/video/BV14w411r7cx

---



## netron   <!-- {docsify-ignore} -->



netron 的两种使用方式：   1、使用在线版；   2、下载本地版

<br />

### 1）使用在线版

浏览器访问：[https://netron.app/](https://netron.app/)
点击 “Open Model” 按钮，选择要可视化的模型文件即可

<img src="https://p.ipic.vip/yp509b.png" alt="img" style="zoom:25%;" />

<br />

<br />

<br />

### 2）下载本地版

终端进行安装： `pip install netron`

安装完成后，在脚本中 调用包 `import netron`

运行程序  `netron.start("model.onnx")`， 会自动打开浏览器进行可视化 （最后有例子）

<br />

<br />

### 3）支持的网络框架 和 模型文件类型

<img src="https://p.ipic.vip/qph2mn.png" alt="image-20231002170425326" style="zoom: 49%;" />



我习惯用 pytorch，但是 netron 对 pytorch 的 `.pt` 和 `.pth` 文件不是很友好，所以，我都是先转换为 onnx 格式，再进行可视化，下面举例。

另外，netron 可以直接可视化 yolo  （DarkNet 框架）的 .cfg文件，非常方便

<br />

<br />

### 4）使用举例

一般情况下，netron 只展示最初的输入尺寸 和 最后的输出尺寸，中间层的尺寸都是不展示的（如下）。

<img src="https://p.ipic.vip/vrjo84.png" alt="img" style="zoom:33%;" />



可以通过 `onnx.save(onnx.shape_inference.infer_shapes(onnx.load("model.onnx")), "model.onnx")` 进行处理，

这样中间的每一层的输入输出就都会推理出 并可视化出来了。

```python
import torch
import torch.nn as nn
import netron
import onnx
from onnx import shape_inference


class My_Net(nn.Module):
    def __init__(self):
        super(My_Net, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(16),
            nn.LeakyReLU(),
        )

        self.layer2 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=1, bias=False),
            nn.BatchNorm2d(32),
            nn.LeakyReLU(),
        )

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        return x


net = My_Net()
img = torch.rand((1, 3, 224, 224))
torch.onnx.export(model=net, args=img, f='model.onnx', input_names=['image'], output_names=['feature_map'])
onnx.save(onnx.shape_inference.infer_shapes(onnx.load("model.onnx")), "model.onnx")
netron.start("model.onnx")
```



<img src="https://p.ipic.vip/izi7zp.png" alt="img" style="zoom:50%;" />



























