import torch.nn as nn
import torchvision.models as models


alexnet = models.alexnet(weights=models.AlexNet_Weights.DEFAULT)


alexnet.pop()
print(alexnet)







