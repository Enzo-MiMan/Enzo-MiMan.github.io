

##  Linux 命令基础格式

<br />

 命令通用格式 ：     `command   [-options]    [parameter]`
- `command`  :   命令本身
-   `[-options]` ：  命令的选项
-  `[parameter]`。： 命令的参数

$\quad$ <font color="red"> * 语法中的 [ ] ， 表示 可选、非必填 </font>

举例 ：
-  `ls -l /home/enzo`  ： `ls` 是命令本身，`-l`  是选项， `/home/enzo`  是参数
-   `cp -r test1 test2` ：  `cp` 是命令本身， `-r`  是选项，  `test1`、 `test2`  是参数

<br />

----

<br />

##  Linux 常用命令
$\quad$
### 1、ls : 列出目录下的 文件 和 文件夹
- 语法 ： `ls [-a, -l, -h] [Linux路径]`
  - `-a`  ： all， 展示所有文件/文件夹 ，包括隐藏文件 （以 .  开头的是隐藏文件）
  
  - `-l`  ： long ， 以列表（竖向排列）的形式展示内容，并展示更多信息
  
    
  
    <img src="https://p.ipic.vip/rrzr0j.png" alt="image-20231107213352797" style="zoom:45%;" />
  
  - `-h`  :  展示出文件的大小，如 ： k、M、G
    
    - `-h`  必须 和 `-l`  同时使用，否则不起作用
    - 不使用 `-h` 的话，文件大小的单位为 byte
  
  

  <img src="https://p.ipic.vip/f00a3y.png" alt="image-20231107214205533" style="zoom:33%;" />
  
  
  
- 语法中的选项是可以组合使用的，比如 -a 和 -l 可以组合使用， 以下4种写法都可以 ： 
  
  - `ls  -la`
  - `ls  -al`
  - `ls -l -a`
  - `ls -a -l`

<br /><br />

### 2、pwd :  Print work Directory 
语法 ： pwd

<br />

### 3、cd : Change Directory 
语法 ： `cd  [Linux路径]`

- 不写 Linux路径 参数，表示回到用户的HOME目录 



特殊路径符  ： 

- .  : 当前路径符
- ..  : 上级路径符号
- ～  ： home 路径

<br />

### 4、mkdir ： Make  Directory        创建新的文件夹（目录）
语法 ：`mkdir  [-p]  Linux路径`
- -p : 一次性创建多个层级的目录

举例 ：
- `mkdir  ../test`  :  在上级目录内创建 test文件夹
- `mkdir -p enzo/test` ： 会同时创建 enzo文件夹 和 test 文件夹

<br />

### 5、touch  创建文件   
- 语法 ： `touch  linux路径`
- 举例 ： `touch test.txt`

<br />

### 6、cat、more、less   查看文件
**1）cat**
  - 语法 ： `cat  linux路径`
  - 举例 ： cat test.txt

**2）more**
  - 语法 ： `more  linux路径`
- 通过 空格键 进行翻页
- 通过 q键 退出
- cat 与 more的区别
  -  cat 是直接将内容全部显示出来 ;  
	- more 一页一页的显示内容，支持翻页操作
	


**3）less : less is more**
  - 语法 ： `less  linux路径`
- more 与 less 的区别：
	- more 只能一页一页翻
	- less 既可以 一页一页翻，也可以一行一行翻

<br />



### 7、cp : copy  复制文件 /  文件夹
- 作用 ： 将文件1 中的内容，复制到文件2中
- 语法 ： `cp [-r]  参数1  参数2`  
  - -r ： 可选， 用于复制文件夹，表示 递归
  - 参数1  ：表示被复制的文件/文件夹
  - 参数2  ：表示要复制去的地方
- 举例
  - 复制文件 ： `cp  test1.txt  enzo/test2.txt`
  - 复制文件夹  :  `cp  -r  data1  data2`

<br />



### 8、mv  :  move   移动文件 /  文件夹
- 语法 ： `mv  参数1  参数2`  ，<sub>注意，该语法没有 - option， 也就是 移动文件夹的话，不需要参数 `-r`</sub>
  - 参数1  ： 表示被移动文及文件 / 文件夹 地址
  - 参数2  ： 表示要移动去的地方
  <br />
- 注意：
	- 若参数2 为文件夹，  注意 参数2 后面要不要带 /
  - 若参数1 和 参数2 在同级目录，且当前无参数2指定的文件/文件夹名称，那么执行该命令的效果为：将参数1的名称 改名为 参数2指定的名称

<br />



### 9、rm  :  remove   删除文件 /  文件夹
- 语法 ： `rm [-r -f] 参数1 参数2 ... 参数N` 
  - -r  ：同cp命令一样，-r 删除文件夹 (带参数 -r， 可同时删除文件和文件夹)
  - -f ： 表示强制删除 force，只有 root 用户（超级管理员用户），才会使用到 `-f`， 因为只有 root 用户在删除东西的时候，系统才会二次提示，是确认否要删除
- rm 命令支持通配符 *
  - test*  ： 匹配任何以 test 开头的文件
  - *test  ： 匹配任何以 test 结尾的文件
  - \*test\*  ： 匹配任何包含 test 的文件

<br />



### 10、which :  查找程序文件
- 作用 ： 查看命令程序文件存放在哪里
- 语法 ： `which 要查找的命令`
- 举例 ： `which cp`

<img src="https://p.ipic.vip/zv7ftc.png" alt="image-20231107225024005" style="zoom:45%;" />

<br />



### 11、find : 查找文件 （按文件名/文件大小查找）
1） 按文件名查找

- 语法 ： `find  起始路径  -name  “被查找文件名”` 

- 注意：

  - 查找的文件名，需要带双引号 “”

  - 文件名支持 通配符查找

- 举例 ：
  -  `find  ~  -name  'test*'`  ：在 home目录下 查找以 test 开头的文件夹

<br />

2） 按文件大小查找
语法 ： `find  起始路径  -size  +|-n[kMG]` 

- +、 - 表示大于 和 小于
- n 表示 大小数字
- kMG 表示大小单位：
    - k(小写字母)表示kb；
    - M表示 MB
    - G表示 GB
- 举例：
  - 查找小于 10kb 的文件  ： `find ～ -size -10k`
  - 查找大于 100MB 的文件  ：  `find ～ size +100M`
  - 查找大于 1GB 的文件  ： `find ～ size +1G`


<br />



### 12、grep  ：过滤文件内容

- 作用：通过关键字，从文中查找出包含指定关键字的行

- 语法 ： `grep  [-n]  关键字  文件路径` 

    - -n  ：可选，表示在结果中 展示包含关键字的行号 

    - 关键字 ：必填， 表示 关键字，<sub>带有空格或其他特殊符号，建议使用 “ ” 将关键字包围起来</sub>

    - 文件路径  ： 必填，表示要在哪个文件中进行查找

    <img src="https://p.ipic.vip/31gbiy.png" alt="image-20231107232001311" style="zoom:45%;" />

    


<br />



### 13、wc  ：统计内容
作用 ： 统计 文件的行数，数量等
语法 ： `wc [-c -m -l -w]  文件路径`

  - -c  ： 统计 bytes 数量
  - -m  ： 统计 字符 数量
  - -l  ： 统计 行数
  - -w  ： 统计 单词数量
  - 文件路径  ： 被统计的文件

<img src="https://p.ipic.vip/wjhhbv.png" alt="image-20231107235128432" style="zoom:50%;" />

<br />

<br />



### 14、管道符  | ： 左边结果作为右边输入
管道符的含义  ：  将管道符左边命令的结果，作为右边命令的输入

<br />

<br />



### 15、echo ： 打印
作用  ：  类似 print 语句

语法  ： `echo  输出的内容`

<img src="https://p.ipic.vip/hh4fn7.png" alt="image-20231108125700344" style="zoom:50%;" />


<br />

<br />



### 16、反引号 ：文字 or 命令
作用  ： 反引号内的 东西会作为 命令去执行

<img src="https://p.ipic.vip/n5zwqu.png" alt="image-20231108112939473" style="zoom:50%;" />

<br />

<br />



### 17、重定向符  >  和 >> ： 往文件中写入
\>  : 将左侧命令的结果，<font color="red"> 覆盖 </font>写入到符号右侧指定的文件中

<img src="https://p.ipic.vip/ai2lql.png" alt="image-20231108131220927" style="zoom:50%;" />

\>>  : 将左侧命令的结果，<font color="red"> 追加 </font>的写到符号右侧指定的文件中

<img src="https://p.ipic.vip/2nuh9x.png" alt="image-20231108131410579" style="zoom:50%;" />

<br />

<br />



### 18、tail ：查看尾行
作用  ： 查看文件尾部内容，跟踪文件的最近更改
语法  ：  `tail  [-f -num]  Linux路径`

  - 被跟踪的文件路径
  - `-f`  ： 持续跟踪 ，f 为 follow
  - `-num`  ：  查看尾部多少行，不填默认10行

<img src="https://p.ipic.vip/xrnh64.png" alt="image-20231108131903290" style="zoom: 50%;" />

<br />

<br />



### 19、vi 编辑器

- vi 、vim 是 visual interface 的简称，是 Linux 中最经典的文本编辑器
- vim 是 vi 的加强版，兼容 vi 的所有指令，不仅能编辑文本，而且还具有 shell 程序编辑的功能，可以以不同的颜色的字体 来辨别语法的正确性，极大方便了程序设计和编辑性
- vi、vim 编辑器的 命令模式 与 编辑模式
  - 命令模式
    - 双击 d键盘 ： 删除光标所在的行
    - u键 ：撤销
    - 保存文件 ：:w
    - 退出文件：:q
    - 保存并退出： :wq
  - 编辑模式
    - i键 ： 从命令模式 进入编辑模式
    - esc键 ： 从编辑模式退出到命令模式

<br />

