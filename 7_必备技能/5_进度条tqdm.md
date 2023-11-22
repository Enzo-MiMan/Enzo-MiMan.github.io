进度条 tqdm



## 1、tqdm 的基础使用

```python
import time
from tqdm import tqdm

for i in tqdm(range(100)):
    time.sleep(0.01)
```



- `tqdm(range(i))`的简约写法 ：`trange(i)`

```python
for t in trange(100):
    time.sleep(0.01)
```



<br />

<br />

## 2、手动更新进度条 （ `update()`方法）



```python
pbar = tqdm(total=200)

for i in range (20):
    time.sleep(1)
    pbar.update(10)

pbar.close()
```





<br />

<br />

## 3、实际应用 



```python
for i, (train_data, train_label) in tqdm(enumerate(train_dataloader), total=len(train_dataloader)):
		train_data, train_label = train_data.to(device), train_label.to(device)
```

