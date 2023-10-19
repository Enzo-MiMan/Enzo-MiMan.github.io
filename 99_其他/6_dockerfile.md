# Docker





## 1、Docker



![image-20231016110446778](/Users/enzo/Library/Application Support/typora-user-images/image-20231016110446778.png)











# 2、Dockerfile



FROM #基础镜像，一切从这里开始构建
MAINTAINER #镜像是谁写的，名字+邮箱
RUN #镜像构建的时候被需要运行的命令
ADD #步骤，tomcat镜像，这个tomcat压缩包，添加内容
WORKDIR #镜像的挂载目录
VOLUME #挂载的目录
EXPOST #保留端口配置
CMD #指定这个容器启动的时候要运行的命令，只有之后一个会生效，可被替代
ENTRYPOINT #指定这个容器启动的时候要运行的命令，可以追加命令
COPY #类似ADD，将我们文件拷贝到镜像中
ENV #构建的时候设置环境变量

![在这里插入图片描述](https://p.ipic.vip/wcsdcd.png)