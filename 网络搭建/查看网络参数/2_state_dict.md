b站视频 ：https://www.bilibili.com/video/BV1X8411f7q1?p=2

---



## net.state_dict() <!-- {docsify-ignore} -->



`net.state_dict()`  会将网路中的 参数名 和参数 转换为 字典的格式

（我们经常用它 将参数转换为字典的格式，然后再保存起来）


```python
for key, value in net.state_dict().items():
    print(key, value.shape)
```

输出

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





