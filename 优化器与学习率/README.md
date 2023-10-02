

## **简介**

argparse 模块是 Python 标准库中提供的一个==命令行解析模块==，它可以让使用者以类似 Unix/Linux 命令参数的方式输入参数，并将参数解析为 Python 变量，从而方便使用者更加快捷的处理参数。


---



## **使用步骤**

### 1）导入argparse模块，并创建解释器 

```html
<p>This is a paragraph</p>
<a href="//docsify.js.org/">Docsify</a>
```




```python
import argparse

# 创建解释器
parser = argparse.ArgumentParser(description="可写可不写，只是在命令行参数出现错误的时候，随着错误信息打印出来。")
```

### 2）添加所需参数 

```python
parser.add_argument('-gf', '--girlfriend', choices=['jingjing', 'lihuan'])
# -gf 代表短选项，在命令行输入-gf和--girlfriend的效果是一样的，作用是简化参数输入
#--girlfriend 代表完整的参数名称，可以尽量做到让人见名知意，需要注意的是如果想通过解析后的参数取出该值，必须使用带--的名称
# choices 代表输入参数的只能是这个choices里面的内容，其他内容则会保错

parser.add_argument('--house', type=int, default=0)
# --house 代表参数名称
# type  代表输入的参数类型，从命令行输入的参数，默认是字符串类型
# default 代表如果该参数不输入，则会默认使用该值

parser.add_argument('food')
# 该种方式则要求必须输入该参数
# 输入该参数不需要指定参数名称，指定反而报错，解释器会自动将输入的参数赋值给food
```

### 3）解析参数
```python
# 进行参数解析
args = parser.parse_args() 
print('args-----:',args)
print('gf-------:', args.girlfriend)
print('food-----:', args.food)
```

在终端运行结果：
```python
(base) enzo@enzo-MBP test % python main.py apple -gf jingjing      
args-----: Namespace(girlfriend='jingjing', house=0, food='apple')
gf-------: jingjing
food-----: apple
```


## **其他参数说明**
### 参数：action 
向 `add_argument` 方法中传入参数 `action=‘store_true’/‘store_false’` ，解析出来就是 bool型参数 True/False，具体规则为:
- store_true：如果未指定该参数，默认状态下其值为False；若指定该参数，将该参数置为 True
- store_false：如果未指定该参数，默认状态下其值为True；若指定该参数，将该参数置为 False

```python
import argparse

parser = argparse.ArgumentParser(description="description")

parser.add_argument('--pa','-a',action='store_true')
parser.add_argument('--pb','-b',action="store_false")
```

```python
>> python test.py
Namespace(pa=False, pb=True)

>> python test.py -a -b
Namespace(pa=True, pb=False)
```


若 该参数 同时给了 action 和 default，在未指定该参数的情况下，以 default 值为准；在指定该参数的情况下，以 action 的值为准。


```python
import argparse

parser = argparse.ArgumentParser(description="description")

parser.add_argument('--pa','-a',action='store_true')
parser.add_argument('--pb','-b',action="store_true",default=True)
parser.add_argument('--pc','-c',action="store_true",default=False)

parser.add_argument('--pd','-d',action='store_false')
parser.add_argument('--pe','-e',action="store_false",default=True)
parser.add_argument('--pf','-f',action="store_false",default=False)

args = parser.parse_args()
print(args)
```

```python
>> python test.py
Namespace(pa=False, pb=True， pc=False, pd=True, pe=True, pf=False)

>> python test.py -a -b -c -d -e -f
Namespace(pa=True, pb=True， pc=True, pd=False, pe=False, pf=False)
```

---

## **使用 pycharm 传递参数给 argparse**
 上面的操作，我们是通过 命令行 给 python 程序传递参数，一般适合于我们在 GPU 等 linux 操作系统中训练模型使用。
但是在平时我们调试算法的时候就会很不方便，没有办法利用编译器进行debug，所以接下来介绍如何在 Pycharm 中传递参数给 argparse，方便 pycharm 进行运行这类python程序。

1、如下图，点击 Edit configurations

![在这里插入图片描述](https://img-blog.csdnimg.cn/4eb64aff092342e48cde8a8f6656fbba.png)

2、在Parameters中添加需要的参数（只写参数），多个参数之间用空格隔开

![在这里插入图片描述](https://img-blog.csdnimg.cn/4a3a56027243400f9b5b49376da07368.png)
3、最后直接运行，可以看到，把我们设置在Parameters里面设置的参数，会在Run的时候补全

![在这里插入图片描述](https://img-blog.csdnimg.cn/ee00cb19f7b44af4a41ccc0ea9f2606a.png)