

b站视频 ：https://www.bilibili.com/video/BV19L41187s4



# IOU <!-- {docsify-ignore} -->

 IoU : Intersection over Union

IoU 是计算两个检测框之间重叠程度的一种方式。

在目标检测任务中，IoU  也用于衡量模型预测的边界框与真实边界框之间的匹配程度。

![image-20231015083830664](https://p.ipic.vip/ynekcj.png)

```python
import torch


def box_iou(boxes1, boxes2):
    # bbox1 和 bbox2 的面积
    area1 = (boxes1[2] - boxes1[0]) * (boxes1[3] - boxes1[1])
    area2 = (boxes2[2] - boxes2[0]) * (boxes2[3] - boxes2[1])

    # 交集的坐上角点 和 右下角点的坐标
    lt = torch.max(boxes1[:2], boxes2[:2])
    rb = torch.min(boxes1[2:], boxes2[2:])

    # 交集的面积
    wh = (rb - lt).clamp(min=0)
    inter = wh[0] * wh[1]

    # 并集的面积
    union = area1 + area2 - inter

    # 交并比
    iou = inter / union
    return iou


boxes1 = torch.tensor([10, 10, 30, 30])
boxes2 = torch.tensor([20, 20, 40, 40])
iou1 = box_iou(boxes1, boxes2)
print(iou1)
```

