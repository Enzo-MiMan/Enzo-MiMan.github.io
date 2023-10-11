

b站视频 ：https://www.bilibili.com/video/BV1ew411k7UP

---





# torchvision.transforms 的使用 <!-- {docsify-ignore} -->

官方文档地址： https://pytorch.org/vision/stable/transforms.html



## 1、transforms.RandomResizedCrop  随机尺寸裁剪

```python
import torchvision.transforms as transforms

resized_crop = transforms.RandomResizedCrop(size=(224, 224),
                                            scale=(0.08, 1.0), 
                                            ratio=(0.75, 1.3333333333333333), 
                                            interpolation=transforms.InterpolationMode.BILINEAR)
```

参数：

- size：期望的输出图像尺寸， 可以是 int值，也可可以是元组（H, W）
- scale ：在调整大小之前指定裁剪的随机区域的下界和上界。尺度是根据原始图像的面积来定义的。
- ratio：在调整大小之前，裁剪的随机纵横比的下限和上限。
- InterpolationMode ： 插值方式 
  - InterpolationMode.NEAREST：最近邻插值。
  - InterpolationMode.BILINEAR：双线性插值 (默认)
  - InterpolationMode.BICUBIC：双三次插值。



上方代码解释：

$\qquad$ 1、将图像进行随机裁剪，裁剪满足以下条件：

$\qquad$ $\qquad$ 裁剪后的图像 面积 与原图像的面积的比例 在 0.08 ～ 1 

$\qquad$ $\qquad$ 裁剪后的图像高宽比范围在  0.75 ～ 1.33之间 

$\qquad$ 2、按照指定的插值方式， 将图像尺寸缩放到 （224， 224） 





<br />

<br />



## 2、水平翻转 与 垂直翻转

```python
horizontal_flip = transforms. RandomHorizontalFlip(0.5)
vertical_flip = transforms. RandomVerticalFlip(0.5)
```

<img src="https://p.ipic.vip/wh6b5i.png" alt="image-20231011174852541" style="zoom:50%;" />

<br />

<br />

## 3、ColorJitter

```python
color_jitter = transforms. ColorJitter(brightness=0,
                                       contrast=0, 
                                       saturation=0, 
                                       hue=0)
```

参数：

- brightness：亮度调整系数。 $\;$调整范围为 [ 1-brightness, 1+brightness ]，默认值为 0。
- contrast：对比度调整系数。 $\;$调整范国为 [ 1一 contrast, 1+contrast ]，默认值为 0。
- saturation：饱和度调整系数。 $\;$调整范围为 [ 1- saturation, 1+ saturation ]，默认值为 0。
- hue：色调调整系数。 $\;$调整范围为 [ -hue， hue ]，默认值为 0。



<br />

<br />

## 4、torchvision.transforms.ToTensor()

`torchvision.transforms.ToTensor()`  做了三件事：

$\qquad$ 1）将图像的数据格式由 nump.ndarray 或 PIL.Image 转为 tensor，数据类型为 torch.FloatTensor

$\qquad$ 2）将像素值范围从 0-255 转换到 0-1之间， 处理方式 ：直接除以255

$\qquad$ 3）将 shape=(H,W, C)  转换为 shape= (C, H, W)

<img src="https://p.ipic.vip/xksmgr.png" alt="image-20231011175602379" style="zoom:50%;" />



<br />

<br />

<br />

## 5、torchvision.transforms.Normalize()

作用：用均值和标准差对张量图像进行归一化，一般在 `torchvision.transforms.ToTensor()` 之后使用

在使用 `torchvision.transforms.ToTensor()`  之后，像素值取值范围会被转换到 [0, 1]之间，再使用 `transforms.Normalize(mean, std)` 进行归一化后，原像素值就被分布到了 [-1, 1] 之间：

公式：$image = \frac{image-mean}{std}$

- 原来的 0~1 最小值 0 则变成 (0 - mean) / std = -1
- 最大值1则变成  (1 - mean) / std = 1

<br />

一般 mean 和 std 会分别指定3个值，代表图像3个通道的均值和方差，比如`torchvision.transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])`

如果是单通道的灰度图，均值为0.5，方差为0.5，可以写成 `transforms.Normalize(mean=[0.5], std=[0.5])`

<br />

我们可能会看到很多代码里面是这样写的：

```python
normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
```

这一组值是怎么来的呢？ 答案就是 ：通过 ImageNet数据集，提前计算出来的。

因为  ImageNet数据集 是一个大型数据集，由一个大型数据集统计出来的均值和方差，基本符合所有数据集的像素值分布，所以可以直接使用。



<img src="https://p.ipic.vip/na1lz0.png" alt="image-20231011175858019" style="zoom:50%;" />

重新计算并使用自己数据集的均值和方差也是可以的，就是开销比较大，所以，一般直接使用 `mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]`





<br />

<br />

## 6、transforms.Compose()

**训练阶段**

使用情况类似：

```python
trans = transforms.Compose([transforms.RandomResizedCrop((640, 640)),
                            transforms.RandomHorizontalFlip(0.5),
                            transforms.ColorJitter(0.5),
                            transforms.ToTensor(),
                            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
```



<br />

**推理阶段**

推理阶段不会再对数据进行增强，只会做基础的预处理，比如：将尺寸处理到固定尺寸 ；使用 ToTensor 处理数据； Normalize 归一化

```python
trans = transforms.Compose([transforms.RE((640, 640)),
                            transforms.ToTensor(),
                            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
```













