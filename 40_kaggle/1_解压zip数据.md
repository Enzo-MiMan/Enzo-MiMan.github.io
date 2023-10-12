

```python
import zipfile
import os
from pathlib import Path


data_root = '/kaggle/input/carvana-image-masking-challenge/'
for filename in os.listdir(data_root):
    if os.path.splitext(filename)[-1] == '.zip':
        z = zipfile.ZipFile(data_root + filename, 'r')
        z.extractall(path=r"./")
        z.close()
```

