from tensorboardX import SummaryWriter
import torch
import torchvision.models as models

model = models.alexnet(weights=models.AlexNet_Weights.DEFAULT)

input = torch.rand(8, 3, 224, 224)
with SummaryWriter(log_dir='logs', comment='Net') as writer:
    writer.add_graph(model, input)

