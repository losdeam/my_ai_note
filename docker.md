[问题目录](https://blog.csdn.net/MrChenLen/article/details/130277406?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522169828320416800182133541%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=169828320416800182133541&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-130277406-null-null.142^v96^pc_search_result_base4&utm_term=Docker%20Desktop%20is%20unable%20to%20detect%20a%20Hypervisor.&spm=1018.2226.3001.4187)
[解决Hypervisor找不到的问题](https://blog.csdn.net/weixin_37695006/article/details/91589895?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522169828329516800192279831%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=169828329516800192279831&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-91589895-null-null.142^v96^pc_search_result_base4&utm_term=hyper-v&spm=1018.2226.3001.4187).

window版本的docker还是有诸多问题，建议直接在windows下的wsl中安装Linux版本的
[Windows系统安装WSL，并安装docker服务](https://blog.csdn.net/xiaohuaidan007/article/details/130160286)
依照这个教程完成了安装，需要注意的是wsl1 和wsl2 的区别还是很大的，没有完整切换的话将会影响到docker的安装··
跟随博客[docker入门，这一篇就够了](https://blog.csdn.net/m0_61503020/article/details/125456520?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522169828105816800226540472%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=169828105816800226540472&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-2-125456520-null-null.142^v96^pc_search_result_base4&utm_term=docker&spm=1018.2226.3001.4187)进行学习
[一个Python项目（带前端），部署到Docker的完整过程](https://blog.csdn.net/u013282737/article/details/85233408)

```
    # 基于镜像基础
    #FROM python:3.9
    FROM python:3.9
    
    
    # 设置工作目录
    WORKDIR /app

    # 复制项目的依赖文件到容器里
    COPY requirements.txt requirements.txt

    # # 设置镜像源
    ENV PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple
    ENV PIP_TRUSTED_HOST=pypi.tuna.tsinghua.edu.cn

    # 安装项目依赖
    # RUN pip install opencv-python-headless -i https://pypi.douban.com/simple
    RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ 

    # 复制其他文件到容器里
    COPY . .

    # 设置环境变量
    ENV FLASK_APP=app.py
    ENV FLASK_RUN_HOST=0.0.0.0

    # 当容器启动时自动执行的语句
    CMD ["python", "app.py"]


```

## 常用指令

1. `docker build -t image . `
   
通过dockerfile构建镜像文件

3. `docker images `
   
显示当前所有的镜像文件

4. `docker ps `
   
显示当前所有的正在运行的docker容器 ， 需要显示包括未运行容器时需要添加 -a 参数

5. `docker run -it -p 9060:9060 --name containers_name  images_name `
使用images_name镜像创建一个名为containers_name的容器并运行，端口号映射为docker端口号9060（前）映射到当前主机的端口号9060（后）

docker run -it -p 50000:50000 --name zero zero:1
## 修改镜像内容
`docker run -it images_name /bin/bash`
使用该指令可以进入images_name镜像的虚拟机中。
但是此时vim多半是不能用的，而且apt install vim会出错
需要
```
echo "deb http://mirrors.163.com/debian/ jessie main non-free contrib" >/etc/apt/sources.list
echo "deb http://mirrors.163.com/debian/ jessie-proposed-updates main non-free contrib" >>/etc/apt/sources.list
echo "deb-src http://mirrors.163.com/debian/ jessie main non-free contrib" >>/etc/apt/sources.list
echo "deb-src http://mirrors.163.com/debian/ jessie-proposed-updates main non-free contrib" >>/etc/apt/sources.list
```
来进行换源
## 问题
Q: 配置环境时出现最后将已安装的库作为依赖项重新安装并且安装失败的情况。
W: 不造
S: 把被重装的库在requirments.txt中取消安装，让其作为依赖项安装

Q: ImportError: libGL.so.1: cannot open shared object file: No such file or ...
W: 缺少cv2的依赖
S: 在requirments.txt中使用opencv-python-headless来代替opencv-python,实测可以解决

T: 建议在出现报错后在处理后将未安装的库调整至上方优先进行安装，以方便发现错误，而不需要等待已经确认无误的库再次安装

